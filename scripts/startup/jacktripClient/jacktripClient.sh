#!/bin/sh

# Kasper Jordaens
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.
#

echo "starting Jacktrip Client in HUB mode"
nohup /usr/local/bin/jacktrip -C choirbox1.local --clientname $HOSTNAME --udprt -n2 -K $HOSTNAME


