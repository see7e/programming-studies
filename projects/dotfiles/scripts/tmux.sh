#!/usr/bin/env bash

RESOURCES="$1"
cd $RESOURCES

@sudo apt install tmux
tmux -V # confirm if at least v3.2a

# Package Manager
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

tmux

tmux source ~/.tmux.conf

# TODO: check how to <prefix>I
