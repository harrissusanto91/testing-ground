#!/bin/bash  

# Customize the Bash prompt to reflect the desired directory structure  
PS1='$(if [[ "$PWD" == /workspaces ]]; then  
          echo "workspaces\$ "  # Show workspaces$ when in /workspaces  
      elif [[ "$PWD" == /workspaces/* ]]; then  
          # Remove the base /workspaces/ part to get the relative path  
          REL_PATH="${PWD#/workspaces/}"  
          
          # If in the base repository directory, show just $  
          if [[ "$REL_PATH" == *"/"* ]]; then  
              # Show the path relative to repositoryname  
              echo "${REL_PATH#*/}\$ "  # Remove the first directory  
          else  
              echo "\$ "  # Show just $ when directly in /workspaces/repositoryname  
          fi  
      else  
          # Default case for other directories outside /workspaces  
          echo "\w\$ "  
      fi)'  

# Export the PS1 variable for the current session  
export PS1  

# Append the export statement to .bashrc for future terminal sessions  
echo "export PS1='$PS1'" >> ~/.bashrc  

# Source .bashrc to apply changes immediately  
source ~/.bashrc
