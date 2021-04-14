#!/bin/bash
#colouring for easier readability
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

read -p "What's the new device name? " devicename
sudo hostname $devicename
sudo sed -i 's/patchbox/'"$devicename"'/g' /etc/hostname
sudo sed -i 's/patchbox/'"$devicename"'/g' /etc/hosts

sudo apt-get update && sudo apt-get upgrade -y

# change to home directory to check for git installations
cd

#check if jacktrip repo exists already, otherwise clone it
if [ ! -d "jacktrip" ]; then
    echo "{green}installing jacktrip{reset}"
    git clone https://github.com/jacktrip/jacktrip.git
else
    echo "{green}update jacktrip{reset}"
    cd jacktrip
    git pull
    cd
fi
sudo apt install -y --no-install-recommends build-essential librtaudio-dev qt5-default autoconf automake libtool make libjack-jackd2-dev qjackctl audacity git
cd jacktrip/src && ./build
cd ../builddir && sudo make install
cd

if [ ! -d "jmess-jack" ]; then
    echo "{green}installing jmess{reset}"
    git clone https://github.com/jacktrip/jmess-jack.git
else
    echo "{green}update jmess{reset}"
    cd jmess-jack
    git pull
    cd
fi
cd jmess-jack/jmess/src && ./build
sudo make install
cd

if [ -d "choirbox" ]; then
    cd choirbox
    echo "{green}copying the necessary scripts{reset}"
    echo "alias jackclient='$(pwd)/scripts/startup/jacktripClient/jacktripClient.sh'" >>/home/patch/.bash_aliases
    echo "alias jackserver='$(pwd)/scripts/startup/jacktripServer/jacktripServer.sh'" >>/home/patch/.bash_aliases
    echo "alias jackpatch='$(pwd)/scripts/startup/patching/patch.sh'" >>/home/patch/.bash_aliases
    source $HOME/.bashrc

    sudo cp -r ./pisound_pure_data_modules/* /usr/local/puredata-patches/

else
    echo "{red}Error: Install must be executed from the git repo choirbox (with this exact name){reset}"
fi

sudo reboot
