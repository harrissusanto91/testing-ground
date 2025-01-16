#!/bin/bash  

# Customize the Bash prompt to show the current directory after 'workspaces'  
PS1='$(if [[ "$PWD" == /workspaces/* ]]; then  
          # Get the relative path after /workspaces/  
          REL_PATH="${PWD#/workspaces/}"  
          # Split the path into components and show the last one followed by $  
          LAST_DIR=$(echo "$REL_PATH" | awk -F '/' '{print $1}')  
          if [[ "$LAST_DIR" == "" ]]; then  
              echo "\$ "  
          else  
              echo "$LAST_DIR$ "  
          fi  
      else  
          # Show the full path for other directories  
          echo "$PWD$ "  
      fi)'  

# Add the customized PS1 to .bashrc for persistence  
echo "export PS1='$PS1'" >> ~/.bashrc  

# Optionally, source the .bashrc to apply changes immediately  
source ~/.bashrc
