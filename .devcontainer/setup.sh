#!/bin/bash  

# Customize the Bash prompt to show the specified directory feedback  
PS1='$(if [[ "$PWD" == /workspace ]]; then  
          echo "/workspace\$ "  # Show /workspace$ when in /workspace  
      elif [[ "$PWD" == /workspace/* ]]; then  
          # In a subdirectory of workspace, show just $  
          echo "\$ "  
      else  
          # For any other directory, show the last folder name followed by $  
          echo "${PWD##*/}\$ "  
      fi)'  

# Export the PS1 variable for the current session  
export PS1  

# Append the export statement to .bashrc for future terminal sessions  
echo "export PS1='$PS1'" >> ~/.bashrc  

# Source .bashrc to apply changes immediately  
source ~/.bashrc
