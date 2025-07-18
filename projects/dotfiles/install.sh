# fetch the user name
USER=$(whoami)
INSTALLER_PATH="$(realpath "${BASH_SOURCE[0]}")"
SCRIPTS_PATH="$INSTALLER_PATH/scripts"
RESOURCE_PATH="$INSTALLER_PATH/res"
PACKAGE_PATH="$INSTALLER_PATH/pkg"

function ask() {
    read -p "$1 (Y/n): " resp
    if [ -z "$resp" ]; then
        response_lc="y" # empty is Yes
    else
        response_lc=$(echo "$resp" | tr '[:upper:]' '[:lower:]') # case insensitive
    fi

    [ "$response_lc" = "y" ]
}

# greetings
# @echo "Hello, $USER! this script will configure your XFCE DE, alongside with the dotfiles configurations."

@echo "Checking for required packages..."
@sudo apt update && @sudo apt upgrade -y
@sudo apt install git curl rsync tree -y

# Installing the fonts
wget -P ~/.local/share/fonts https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/JetBrainsMono.zip \
&& cd ~/.local/share/fonts \
&& unzip JetBrainsMono.zip \
&& rm JetBrainsMono.zip \
&& fc-cache -fv

# Program installation
# if ask "'Install' the dotfiles? (Y/n)"; then
#     source "$SCRIPTS_PATH/dotfiles.sh" $RESOURCE_PATH
#     dotfiles_exit=$?  # Capture the exit code of the sourced script
#     if [ $dotfiles_exit -ne 0 ]; then
#         echo "We had some problem with the dotfiles.sh script: $dotfiles_exit"
#         # Handle the error or exit gracefully
#         exit $dotfiles_exit  # Optionally exit the main script with the same exit code
#     fi
# fi

# Install apps
## Latest NeoVim
curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim.appimage ~/pkg/nvim.appimage
chmod u+x ~/pkg/nvim.appimage
~/pkg/nvim.appimage --appimage-extract
~/pkg/squashfs-root/AppRun --version

# Optional: exposing nvim globally.
sudo mv ~/pkg/squashfs-root /
sudo ln -s /squashfs-root/AppRun /usr/bin/nvim

## NVChad (dont forget to open nvim to finish the configuration)
git clone https://github.com/NvChad/starter ~/.config/nvim

## Other apps
sudo apt install fzf fd-find bat eza tmux -y
# sudo apt install yazi -y

# Configure Tmux
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm


# Copy the files (replace later with Stow)
mv ~/.zshrc ~/.zshrc.bak
cp $RESOURCE_PATH/.zshrc ~/.zshrc
cp $RESOURCE_PATH/.config ~/.config

# Install zsh
sudo apt install zsh -y
chsh $USER

@echo "======================================================================"
@echo "All done! Note that some changes may require a reload of the session"
@echo "to persist. The script will try to automatically do that for you!"
@echo "If it doesn't, please do it manually. Enjoy your new setup! :)"
@echo "======================================================================"
if [ $theme_exit -eq 0 ]; then
    @echo "To apply the new theme, this script will atempt to log you out."
    pkill -u $USER
fi
