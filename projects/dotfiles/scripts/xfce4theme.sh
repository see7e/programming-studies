#!/usr/bin/env bash

THEME_RESOURCES="$1" # Resources location
cd $THEME_RESOURCES # just to be sure

# Backups
TIMESTAMP=$(date +%s)
BACKUP="../../backups/$TIMESTAMP"
mkdir $BACKUP

# manual steps? got covered in the resource files
# Desktop settings > Icons > Icon type: None
# Window Manager > Placement > At the center of the screen

git clone https://github.com/viceliuice/Orchis-theme.git
./Orchis-theme/install.sh
# install icon theme
git clone https://github.com/viceliuice/Tela-icon-theme.git
./Tela-icon-theme/install.sh

# fonts-pack.zip - Fonts
unzip .fonts-pack.zip -d fonts-pack
rsync -av fonts-pack/.local ~
if [ ! -e ~/.local/share/fonts ]; then
    echo "Failed to install fonts-pack.zip"
    exit 1
fi

# Wallpappers
unzip /alt-wallpappers.zip -d alt-wallpappers
sudo rsync -av alt-wallpappers/usr /usr/share/backgrounds

# xfce-config.zip - Xfce Desktop Environment
xfce4-panel --quit && pkill xconfd
mv ~/.config/xfce4 $BACKUP # create a backup
rsync -av xfce4/ $HOME

## Genmon -> Comand=/home/<user>/.genmon-plugin/cpu-panel.sh
unzip .genmon-plugin.zip -d genmon-plugin
rsync -av genmon-plugin $HOME

file_paths=(
    "$HOME/.config/xfce4/panel/genmon-3.rc"
    "$HOME/.config/xfce4/panel/genmon-6.rc"
    "$HOME/.config/xfce4/panel/genmon-9.rc"
    "$HOME/.config/xfce4/panel/genmon-15.rc"
)
for file_path in "${file_paths[@]}"; do
    if [ ! -f "$file_path" ]; then
        echo "$(basename "$file_path") file not found!"
        exit 1
    fi
done

# Update the information
for file in "${file_paths[@]}"; do
    echo "Processing file: $file"
    
    # Check if the file exists
    if [ ! -f "$file" ]; then
        echo "Error: File $file does not exist."
        continue
    fi
    
    # Select the portion of text to update
    old_line=$(grep "^Command=" "$file")

    # Check if the line was found
    if [ -z "$old_line" ]; then
        echo "Error: 'Command' line not found in the file."
        continue
    fi

    # Replace "<user>" with the current username
    new_line=$(echo "$old_line" | sed "s/\/home\/<user>/\/home\/$USER/")

    # Update the file with the new line
    # Use sed to replace the old line with the new line
    sed -i "s|$old_line|$new_line|" "$file"

    # echo "Old line: $old_line"
    # echo "New line: $new_line"
done

## 16955526721 -> Icon=/home/<user>/.assets/power-off.svg
file_path="$HOME/.config/xfce4/panel/launcner-2/16955526721.desktop"
if [ ! -f "$file_path" ]; then
    echo "$(basename "$file_path") file not found!"
    exit 1
fi

old_line=$(grep "^Icon=" "$file")
if [ -z "$old_line" ]; then
    echo "Error: 'Icon' line not found in the file."
    exit 1
fi

new_line=$(echo "$old_line" | sed "s/\/home\/<user>/\/home\/$USER/")
sed -i "s/$old_line/$new_line/" "$file_path"

@echo "----------------------------------------"

# Loop to check if every path in the txt file exists
non_existing_paths="" # Initialize a variable to store non-existing paths
while IFS= read -r path; do
    if [ ! -e "$path" ]; then
        non_existing_paths+="$path\n"  # Append the non-existing path to the list
    fi
done < "$THEME_RESOURCES/xfcelist.txt"
# Echo the non-existing paths
if [ -n "$non_existing_paths" ]; then
    echo "The following paths do not exist:"
    echo -e "$non_existing_paths"
    exit 1
else
    echo "All dotfiles (links) created."
fi

xfce4-panel &

@echo "========================================"
