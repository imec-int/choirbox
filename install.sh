#!/bin/bash
echo "alias jackclient='$(pwd)/scripts/startup/jacktripClient/jacktripClient.sh'" >> /home/patch/.bash_aliases
echo "alias jackserver='$(pwd)/scripts/startup/jacktripServer/jacktripServer.sh'" >> /home/patch/.bash_aliases
source .bashrc

#TODO should be executed from the choirbox repo, can we instruct this?