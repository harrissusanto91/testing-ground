#!/bin/bash  

# Customize the Bash prompt to show the current directory after 'workspaces'.  
PS1='$(if [[ "$PWD" == /workspaces/* ]]; then  
          # Get the relative path after /workspaces/  
          REL_PATH="${PWD#/workspaces/}"  
          # If REL_PATH is empty, we are at /workspaces, so just show $  
          if [[ -z "$REL_PATH" ]]; then  
              echo "\$ "  
          else  
              # Otherwise, display the last directory in REL_PATH  
              LAST_DIR=${REL_PATH%%/*}  # Get everything before the first '/'  
              echo "$LAST_DIR\$ "  
          fi  
      else  
          # Show the full path for other directories  
          echo "$PWD\$ "  
      fi)'  

# Add the customized PS1 to .bashrc for persistence  
echo "export PS1='$PS1'" >> ~/.bashrc  

# Optionally, source the .bashrc to apply changes immediately  
source ~/.bashrc
