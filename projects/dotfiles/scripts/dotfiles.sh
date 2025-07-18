#!/usr/bin/env bash

RESOURCES="$1" # Resources location
cd $RESOURCES # just to be sure

# Backups
TIMESTAMP=$(date +%s)
BACKUP="../backups/$TIMESTAMP"
mkdir $BACKUP
# TODO: move the files listed in the 'dotlist' to the backup folder
# mv $SH_PATH "$BACKUP/$SH"

# Check what shell is being used
SH=".bashrc"
SH_PATH="${HOME}/${SH}"
if [ -f "${HOME}/.zshrc" ]; then
    SH=".zshrc"
    SH_PATH="${HOME}/${SH}"
fi

# Stow
STOW_PATH="../.stow-local-ignore"
@sudo apt install stow
# echo ".git" > $STOW_PATH
# echo ".gitignore" > $STOW_PATH
echo "./install.sh" > $STOW_PATH
echo "./TODO.md" > $STOW_PATH
echo "$RESOURCES/.dotlist.txt"
echo "$RESOURCES/.vscode" > $STOW_PATH # gonna leave this here just for now
echo "$RESOURCES/.dotlist.txt" $STOW_PATH
echo "$RESOURCES/backups" > $STOW_PATH # backups
echo "$RESOURCES/scripts/" > $STOW_PATH
echo "$RESOURCES/theme" > $STOW_PATH

# # alacritty
# if [ -f ~/.config/alacritty.tom ]; then
#     cp -r ~/.config/alacritty .config
# else
#     @echo "The .tom file of alacritty is not present"
# fi

git pull # in the moment i'm using "static" files, so it only requires a pull

stow .

@echo "----------------------------------------"

# Loop to check if every path in the txt file exists
non_existing_paths="" # Initialize a variable to store non-existing paths
while IFS= read -r path; do
    if [ ! -e "$path" ]; then
        non_existing_paths+="$path\n"  # Append the non-existing path to the list
    fi
done < "$RESOURCES/.dotlist.txt"
# Echo the non-existing paths
if [ -n "$non_existing_paths" ]; then
    echo "The following paths do not exist:"
    echo -e "$non_existing_paths"
    exit 1
else
    echo "All dotfiles (links) created."
fi

@echo "========================================"
