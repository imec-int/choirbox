#!/bin/bash

read -p "What's the new device name? " devicename
sudo hostname $devicename
sudo sed -i 's/patchbox/'"$devicename"'/g' /etc/hostname
sudo sed -i 's/patchbox/'"$devicename"'/g' /etc/hosts

sudo apt-get update && sudo apt-get upgrade -y

echo "installing jacktrip"
git clone https://github.com/jacktrip/jacktrip.git
sudo apt install -y --no-install-recommends build-essential librtaudio-dev qt5-default autoconf automake libtool make libjack-jackd2-dev qjackctl audacity git
cd jacktrip/src && ./build
cd ../builddir && sudo make install
cd

echo "installing jmess"
git clone https://github.com/jacktrip/jmess-jack.git
cd jmess-jack/jmess/src && ./build
sudo make install
cd

if [ -d "../choirbox" ]
then
    echo "copying the necessary scripts"
    echo "alias jackclient='$(pwd)/scripts/startup/jacktripClient/jacktripClient.sh'" >> /home/patch/.bash_aliases
    echo "alias jackserver='$(pwd)/scripts/startup/jacktripServer/jacktripServer.sh'" >> /home/patch/.bash_aliases
    echo "alias jackpatch='$(pwd)/scripts/startup/patching/patch.sh'" >> /home/patch/.bash_aliases
    source $HOME/.bashrc

    sudo cp -r ./pisound_pure_data_modules/* /usr/local/puredata-patches/

else
    echo "Error: Install must be executed from the git repo choirbox (with this exact name)"
fi

sudo reboot
