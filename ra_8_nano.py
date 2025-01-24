# GPT Prompt for Scoring and Feedback
GPT_PROMPT = """
You are an advanced scoring assistant for PTE Read Aloud tasks. Analyze the following data and provide concise scores and feedback for the traits Content, Pronunciation, and Fluency. Your feedback must be actionable and to the point.

### Input Details:
1. **Task Text**: The text the speaker read aloud.
2. **Transcribed Text**: The speech-to-text output.
3. **Word Confidence Scores**: Per-word confidence values from the transcription system.
4. **Pause Information**: Total pause duration and effective speaking duration.

### Output Format:

Scores:
- Content: [X/3]
- Pronunciation: [X/5]
- Fluency: [X/5]

Feedback:
- Content: [Short, actionable feedback]
- Pronunciation: [Short, actionable feedback]
- Fluency: [Short, actionable feedback]

Additional Notes: [Optional, if critical]
```

### Scoring Logic:
- **Content**:
  - Match task text with transcribed text.
  - Penalize for omissions, replacements, or insertions.
  - Apply higher penalties for content words (nouns, verbs, adjectives).

- **Pronunciation**:
  - Use confidence scores to rate word accuracy.
  - Evaluate stress and intonation patterns.
  - Penalize for excessive pauses.

- **Fluency**:
  - Calculate pause-to-speaking ratio.
  - Deduct points for frequent or long pauses.

Focus on brevity and relevance in feedback.
"""

# Python Code Implementation
import json
from typing import Dict, List
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
import assemblyai as aai
import time
import difflib
from typing import List, Dict

# Set your AssemblyAI API key
ASSEMBLYAI_API_KEY = "42bbc9d4e57e4eb79a51a80b914e035c"
aai.settings.api_key = ASSEMBLYAI_API_KEY

class ContentForRA:
        def score_content(self, task_tokens: List[str], transcription_tokens: List[str], confidences: List[Dict]) -> Dict:
            """Compare tokens to calculate content score, omissions, insertions, and replacements using sequence alignment."""
            omissions = []
            insertions = []
            replacements = []
            low_confidence_matches = []
            matched_points = 0

            # Perform sequence alignment
            sequence_matcher = difflib.SequenceMatcher(None, task_tokens, transcription_tokens)
            alignment = sequence_matcher.get_opcodes()

            for tag, i1, i2, j1, j2 in alignment:
                if tag == "equal":  # Matched words
                    for i, j in zip(range(i1, i2), range(j1, j2)):
                        if confidences[j]["confidence"] >= 0.7:
                            matched_points += 1
                        else:
                            low_confidence_matches.append((task_tokens[i], transcription_tokens[j]))
                elif tag == "replace":  # Replacements
                    for i, j in zip(range(i1, i2), range(j1, j2)):
                        replacements.append((task_tokens[i], transcription_tokens[j]))
                elif tag == "delete":  # Omissions
                    omissions.extend(task_tokens[i1:i2])
                elif tag == "insert":  # Insertions
                    insertions.extend(transcription_tokens[j1:j2])

            # Updated Scoring Logic with Weights
            replacement_penalty = len(replacements) * 3.0  # Weight for replacements
            omission_penalty = len(omissions) * 3.0       # Weight for omissions
            insertion_penalty = len(insertions) * 3.0     # Weight for insertions
            low_confidence_penalty = len(low_confidence_matches) * 1.0  # Lower weight for low-confidence matches

            # Calculate total penalties
            total_penalty = replacement_penalty + omission_penalty + insertion_penalty + low_confidence_penalty

            # Matched points calculation
            matched_points = len(task_tokens) - total_penalty

            # Final score calculation with revised coefficient logic
            coefficient = (3 / len(task_tokens)) * (1 - (low_confidence_penalty / max(1, len(task_tokens)))) if task_tokens else 1
            score = max(0, coefficient * matched_points)

            # Calculate similarity percentage
            similarity_percentage = (matched_points / len(task_tokens)) * 100 if task_tokens else 0

            return {
                "score": score,
                "similarity_percentage": similarity_percentage,
                "omissions": omissions,
                "insertions": insertions,
                "replacements": replacements,
                "low_confidence_matches": low_confidence_matches
            }



# Initialize Content Scoring Class
content_scorer = ContentForRA()

def transcribe_audio_with_assemblyai(audio_path: str) -> Dict:
    """Transcribe audio using AssemblyAI SDK and return transcription details."""
    transcriber = aai.Transcriber()
    print("Uploading and transcribing audio with AssemblyAI...")

    transcript = transcriber.transcribe(audio_path)

    if transcript.status == aai.TranscriptStatus.error:
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    # Extract transcription and word confidence data
    transcribed_text = transcript.text
    word_confidences = [
        {
            "word": word.text,
            "confidence": word.confidence,
            "start_time": word.start / 1000,
            "end_time": word.end / 1000
        }
        for word in transcript.words
    ]
    # Compute content score once
    #task_tokens = task_text.split()
    #transcription_tokens = transcribed_text.split()
    #results = content_scorer.score_content(task_tokens, transcription_tokens, word_confidences)
    
    # Debugging Outputs
    
    print("\nTranscription Received:")
    print(transcribed_text)

    print("\nWord Confidence Scores:")
    for word_data in word_confidences:
        print(f"Word: {word_data['word']}, Confidence: {word_data['confidence']}")
    #print("\nScoring Results:")
    #print("Content Score:", results["score"])
    #print("Similarity Percentage:", results["similarity_percentage"])
    #print("Omissions:", results["omissions"])
    #print("Insertions:", results["insertions"])
    #print("Replacements:", results["replacements"])
    #print("Low Confidence Words:", results["low_confidence_matches"])
    
    return {
        "transcribed_text": transcribed_text,
        "word_confidences": word_confidences,
    }


def calculate_pause_info(word_confidences: List[Dict]) -> Dict:
    """Analyze the word timestamps to calculate pause information."""
    if not word_confidences:
        return {
            "audio_duration": 0,
            "initial_silence": 0,
            "final_silence": 0,
            "total_pause_duration": 0
        }

    audio_duration = word_confidences[-1]["end_time"]
    initial_silence = word_confidences[0]["start_time"]
    final_silence = audio_duration - word_confidences[-1]["end_time"]

    total_pause_duration = 0
    pauses = []  # For detailed pause information
    for i in range(1, len(word_confidences)):
        pause = word_confidences[i]["start_time"] - word_confidences[i - 1]["end_time"]
        if pause > 0.2:  # Consider pauses longer than 200ms
            total_pause_duration += pause
            pauses.append((word_confidences[i - 1]["word"], word_confidences[i]["word"], pause))

    return {
        "audio_duration": audio_duration,
        "initial_silence": initial_silence,
        "final_silence": final_silence,
        "total_pause_duration": total_pause_duration,
        "pauses": pauses
    }

def calculate_scores(task_text: str, transcribed_text: str, confidences: List[Dict], pause_info: Dict) -> Dict:
    """Calculate Content, Pronunciation, and Fluency scores."""
    # Content Scoring
    tokens_task = task_text.split()
    tokens_transcription = transcribed_text.split()
    content_results = content_scorer.score_content(tokens_task, tokens_transcription, confidences)

    # Pronunciation Scoring
    avg_confidence = sum(c["confidence"] for c in confidences) / len(confidences) if confidences else 0
    pronunciation_score = (
    5 if avg_confidence >= 0.93 else
    4.5 if avg_confidence >= 0.9 else
    4 if avg_confidence >= 0.85 else
    3.5 if avg_confidence >= 0.8 else
    3 if avg_confidence >= 0.7 else
    2 if avg_confidence >= 0.6 else
    1 if avg_confidence >= 0.5 else 0
)
    # Adjust Pronunciation Score Based on Content Score Thresholds (with Pronunciation Score Condition)
    content_score = content_results["score"]  # Content score already calculated
    if pronunciation_score > 3.5:
        if content_score < 1:
            weight = 0.50
        elif content_score < 2:
            weight = 0.70
        else:
            weight = 1.00
        # Apply Weight to Adjust Pronunciation Score
        pronunciation_score = pronunciation_score * weight
    
    # Fluency Scoring
    effective_speaking_duration = pause_info["audio_duration"] - (pause_info["initial_silence"] + pause_info["final_silence"])
    pause_ratio = pause_info["total_pause_duration"] / effective_speaking_duration if effective_speaking_duration > 0 else 1
    fluency_score = (
        5 if pause_ratio <= 0.1 else
        4 if pause_ratio <= 0.2 else
        3 if pause_ratio <= 0.3 else
        2 if pause_ratio <= 0.4 else
        1 if pause_ratio > 0.4 else 0
    )

    return {
        "scores": {
            "content": round(content_results["score"], 2),
            "pronunciation": pronunciation_score,
            "fluency": fluency_score,
        },
        "feedback": {
            "content": f"Ensure key words are read accurately. Omissions: {len(content_results['omissions'])}, Insertions: {len(content_results['insertions'])}, Replacements: {len(content_results['replacements'])}.",
            "pronunciation": "Focus on clearer articulation of challenging words.",
            "fluency": f"Detected {len(pause_info['pauses'])} pauses. Total pause duration: {pause_info['total_pause_duration']:.2f}s.",
        },
        "similarity_percentage": content_results["similarity_percentage"],
        "average_confidence": avg_confidence * 100,
        "pauses": pause_info["pauses"]
    }

def create_gui():
    """Create a GUI for displaying results."""
    def upload_audio_file():
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3 *.m4a")])
        audio_path_entry.delete(0, tk.END)
        audio_path_entry.insert(0, file_path)

    def process_audio():
        audio_file_path = audio_path_entry.get()
        task_text = task_text_entry.get("1.0", "end-1c")

        # Transcribe Audio using AssemblyAI
        transcription = transcribe_audio_with_assemblyai(audio_file_path)

        # Calculate Pause Information
        pause_info = calculate_pause_info(transcription["word_confidences"])

        # Calculate Scores
        results = calculate_scores(
            task_text,
            transcription["transcribed_text"],
            transcription["word_confidences"],
            pause_info
        )

        # Extract similarity percentage and average confidence
        similarity_percentage = results["similarity_percentage"]
        average_confidence = results["average_confidence"]

        # Update GUI with Results
        content_score_label["text"] = f"Content: {results['scores']['content']} / 3"
        pronunciation_score_label["text"] = f"Pronunciation: {results['scores']['pronunciation']} / 5"
        fluency_score_label["text"] = f"Fluency: {results['scores']['fluency']} / 5"
        content_feedback_label["text"] = f"Feedback: {results['feedback']['content']} (Similarity: {similarity_percentage:.2f}%)"
        pronunciation_feedback_label["text"] = f"Feedback: {results['feedback']['pronunciation']} (Avg Confidence: {average_confidence:.2f}%)"
        fluency_feedback_label["text"] = f"Feedback: {results['feedback']['fluency']}"

        # Display Pause Information
        pause_details_display.delete("1.0", "end")
        pause_details_display.insert("end", "Detailed Pauses:\n")
        for pause in results["pauses"]:
            pause_details_display.insert("end", f"Pause between '{pause[0]}' and '{pause[1]}': {pause[2]:.2f}s\n")

        # Update Transcribed Text with Confidence Colors
        transcribed_text_display.delete("1.0", "end")
        for word_data in transcription["word_confidences"]:
            word, confidence = word_data["word"], word_data["confidence"]
            color = ("green" if confidence >= 0.93 else
                     "yellow" if confidence >= 0.75 else
                     "red")
            transcribed_text_display.insert("end", word + " ", (color,))

    # GUI Setup
    root = tk.Tk()
    root.title("PTE Read Aloud Scorer")

    # Input Fields
    tk.Label(root, text="Audio File Path:").grid(row=0, column=0, sticky="w")
    audio_path_entry = tk.Entry(root, width=50)
    audio_path_entry.grid(row=0, column=1, padx=10, pady=5)
    upload_button = tk.Button(root, text="Upload", command=upload_audio_file)
    upload_button.grid(row=0, column=2, padx=10, pady=5)

    tk.Label(root, text="Task Text:").grid(row=1, column=0, sticky="nw")
    task_text_entry = tk.Text(root, width=50, height=10)
    task_text_entry.grid(row=1, column=1, padx=10, pady=5)

    # Process Button
    process_button = tk.Button(root, text="Process", command=process_audio)
    process_button.grid(row=2, column=0, columnspan=3, pady=10)

    # Output Fields
    content_score_label = tk.Label(root, text="Content: ")
    content_score_label.grid(row=3, column=0, sticky="w", padx=10)
    pronunciation_score_label = tk.Label(root, text="Pronunciation: ")
    pronunciation_score_label.grid(row=4, column=0, sticky="w", padx=10)
    fluency_score_label = tk.Label(root, text="Fluency: ")
    fluency_score_label.grid(row=5, column=0, sticky="w", padx=10)

    content_feedback_label = tk.Label(root, text="Feedback: ")
    content_feedback_label.grid(row=3, column=1, sticky="w", padx=10)
    pronunciation_feedback_label = tk.Label(root, text="Feedback: ")
    pronunciation_feedback_label.grid(row=4, column=1, sticky="w", padx=10)
    fluency_feedback_label = tk.Label(root, text="Feedback: ")
    fluency_feedback_label.grid(row=5, column=1, sticky="w", padx=10)

    tk.Label(root, text="Transcribed Text with Confidence Colors:").grid(row=6, column=0, sticky="nw", padx=10)
    transcribed_text_display = ScrolledText(root, width=50, height=10, wrap="word")
    transcribed_text_display.grid(row=6, column=1, padx=10, pady=5)

    # Define Tags for Colors
    transcribed_text_display.tag_config("green", foreground="green")
    transcribed_text_display.tag_config("yellow", foreground="orange")
    transcribed_text_display.tag_config("red", foreground="red")

    # Pause Details Section
    tk.Label(root, text="Pause Details:").grid(row=7, column=0, sticky="nw", padx=10)
    pause_details_display = ScrolledText(root, width=50, height=10, wrap="word")
    pause_details_display.grid(row=7, column=1, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()



# Instructions to Implement
"""
1. Install dependencies:
    pip install requests tkinter assemblyai

2. Set up AssemblyAI API key:
    - Sign up at https://www.assemblyai.com/ to get your API key.
    - Replace `your_assemblyai_api_key` with your API key in the script.

3. Run locally:
    - Save this script as `pte_read_aloud.py`.
    - Use `python pte_read_aloud.py` to launch the GUI.

4. Input:
    - Provide task text and audio file path via the GUI.

5. Output:
    - Scores and feedback displayed in the GUI.
    - Transcribed text displayed with word-level confidence colors.
    - Detailed pause information displayed in the GUI.
"""




