#!/bin/bash

# Kasper Jordaens
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
#

echo "starting Jacktrip Client in HUB mode"
/usr/local/bin/jacktrip -C choirbox1.local --clientname $HOSTNAME --udprt -n2 -K $HOSTNAME &
/usr/bin/jmess -D 
/usr/bin/jmess -c /home/patch/$HOSTNAME.xml



