
#!/bin/bash

# Copyright 2023, QaYe Dev.

# MetaTrader download url
URL="https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/mt5setup.exe"
# Wine version to install: stable or devel
WINE_VERSION="stable"

# Prepare: switch to 32 bit and add Wine key
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo mv winehq.key /usr/share/keyrings/winehq-archive.key

# Get Debian version and trim to major only
OS_VER=$(lsb_release -r |cut -f2 |cut -d "." -f1)
# Choose repository based on Debian version
if (( $OS_VER >= 12)); then
  wget -nc https://dl.winehq.org/wine-builds/debian/dists/bookworm/winehq-bookworm.sources
  sudo mv winehq-bookworm.sources /etc/apt/sources.list.d/
elif (( $OS_VER < 12 )) && (( $OS_VER >= 11 )); then
  wget -nc https://dl.winehq.org/wine-builds/debian/dists/bullseye/winehq-bullseye.sources
  sudo mv winehq-bullseye.sources /etc/apt/sources.list.d/
elif (( $OS_VER <= 10 )); then
  wget -nc https://dl.winehq.org/wine-builds/debian/dists/buster/winehq-buster.sources
  sudo mv winehq-buster.sources /etc/apt/sources.list.d/
fi


sudo mkdir -pm755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/debian/dists/bullseye/winehq-bullseye.sources
# Update package and install Wine
sudo apt update
sudo apt install --install-recommends winehq-stable -y


#sudo apt upgrade
#sudo apt install --install-recommends winehq-$WINE_VERSION
#sudo apt install wine wine32 wine64 libwine libwine:i386 fonts-wine -y
#init wine
#sudo rm -rf ~/.wine*
wine64 start


#init DISPLAY
#kill %

sudo apt update
sudo apt-get install xvfb -y
export DISPLAY=:1

Xvfb :1 -screen 0 1024x768x24 &


# Set environment to Windows 10
#WINEPREFIX=~/.mt5
winecfg -v=win10
sudo apt-get install cabextract -y

##download assinsials and install on Wine.
wget -O winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
sudo chmod +x ./winetricks
./winetricks -q --unattended gdiplus vcrun2010 corefonts dotnet40

#DotNet
#wget -O DNFInstaller.exe https://download.visualstudio.microsoft.com/download/pr/158dce74-251c-4af3-b8cc-4608621341c8/9c1e178a11f55478e2112714a3897c1a/.ndp472-devpack-enu.exe
#wine ./DNFInstaller.exe /quiet

#PowerShell
#wget -O PowerShellSetup.msi https://github.com/PowerShell/PowerShell/releases/download/v7.2.12/PowerShell-7.2.12-win-x64.msi
#wine64 msiexec /i ./PowerShellSetup.msi


# Download MetaTrader
wget -O mt5setup.exe $URL

# Start MetaTrader installer
#WINEPREFIX=~/.mt5
wine64 ./mt5setup.exe /auto

