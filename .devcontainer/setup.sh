#!/bin/bash  

# Customize the Bash prompt to show the directory structure as you specified  
PS1='$(if [[ "$PWD" == /workspace/* ]]; then  
          # Check if we are directly in /workspace  
          if [[ "$PWD" == /workspace ]]; then  
              echo "/workspace\$ "  # Show /workspace$ when in /workspace  
          else  
              # Show the last part of the path for any other subdirectory  
              echo "${PWD##*/}\$ "  # Get the last directory name and add $  
          fi  
      else  
          # For anything outside of /workspace, show the full path (optional)  
          echo "\w\$ "  
      fi)'  

# Export the PS1 variable for the current session  
export PS1  

# Append the export statement to .bashrc for future terminal sessions  
echo "export PS1='$PS1'" >> ~/.bashrc  

# Source .bashrc to apply changes immediately  
source ~/.bashrc
