#!/bin/bash

# Installs fish shell and sets it as the default shell

set -e

FISH_VERSION="3.1.2"

# Install dependencies
sudo apt-get install build-essential cmake ncurses-dev libncurses5-dev libpcre2-dev gettext

# Create a build directory
mkdir fish-install
cd fish-install

# Download and extract the latest build (could clone from git but that's less stable)
wget https://github.com/fish-shell/fish-shell/releases/download/$FISH_VERSION/fish-$FISH_VERSION.tar.gz
tar -xzvf fish-$FISH_VERSION.tar.gz
cd fish-$FISH_VERSION

# Build and install
cmake .
make
sudo make install

# Add to shells
echo /usr/local/bin/fish | sudo tee -a /etc/shells

# Set as user's shell
chsh -s /usr/local/bin/fish

# Delete build directory
cd ../../
rm -rf fish-install
