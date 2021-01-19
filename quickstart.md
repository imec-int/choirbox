
# quickstart raspberry pi setup
 
this is a shorter version of [setup](setup.md), focussing on the devices if the installation is already done.
 
## starting
 
There should be 1 RPi/computer serving as server, the others are clients.
As an example we'll take choirbox1 as server, 2 to 5 are clients (vocalists).

The server is also the one who uses the android application for mixing the sound.

### Qjackctl

On all devices, open qjackctl.

`qjackctl &`

### Jacktrip

Then, on the server, we start the jacktrip server in HUB server mode:
`jacktrip -S` 

On the clients, we'll use:
`jacktrip -C choirbox1.local --clientname $HOSTNAME --udprt -n2`

### Virtual patching in Qjackctl

In QJackctl, go to setup and make sure the settings correspond to [jack setup](#jack_setup)
Or load them via jmess:
`jmess -c choirbox1test.xml`


### patching
#### master 
Important on the master (Qjackctl): the master is a client as well, yet does not receive its inputs via jacktrip, but from the system. So we have to connect system to the pure data input, instead of the jacktrip receives. 

The remote clients, of course, come into the jacktrip receives and should be patched this way. 
#### clients
On the clients, we patch the system inputs to the jacktrip sends, and the jacktrip receives to the system outputs.


###hotspots
choirbox1:5 password blokaslabs
