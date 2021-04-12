
# phase 1 setup

## Hardware

## Software

[alternative: tpf-client](https://gitlab.zhdk.ch/TPF/tpf-client)

[paper tpf-client](https://lac.linuxaudio.org/2019/doc/haefeli.pdf)

Use VNC Viewer for viewing the raspberry pi screen

### Patchbox raspberry pi image

[patchbox OS base image](https://blokas.io/patchbox-os/)

starting settings:

|username|password|
|-|-|
|patch | blokaslabs|

### initial login

setup wizard:
| section |  choice |
| ---|---|
| update to latest | yes|
|soundcard| pisound|
| default boot option|desktop autologin|
|jack setup|48000/64/2 (check redundancy options if bandwith leaves some room.) |
| wifi setup|only for easy access, not for audio stream preferred|
| module|none: Default patchbox OS environment|

### change hostname to something sensible

```bash
sudo nano /etc/hostname
sudo nano /etc/hosts
```

We picked choirbox1 to choirbox5
<!-- 
### kernel PREEMPT

is enabled by default on the patchbox OS
but not on newest image...
stick to stock 5.4.x kernel at the moment

```bash
uname -v
```

> \#1 SMP PREEMPT RT Wed Mar 11 17:15:58 EET 2020 -->

### jack and jacktrip

changing fast due to high-paced development!

Steps to build jacktrip from git repo:

```bash
git clone https://github.com/jacktrip/jacktrip.git
sudo apt install -y --no-install-recommends build-essential librtaudio-dev qt5-default autoconf automake libtool make libjack-jackd2-dev qjackctl audacity git
cd jacktrip/src && ./build
cd ../builddir && sudo make install
cd
```

### jmess (patch connection state saving)

```bash
git clone https://github.com/jacktrip/jmess-jack.git
cd jmess-jack/jmess/src && ./build
sudo make install
cd
```

### choirbox repo

```bash
git clone https://github.com/imec-int/choirbox.git
cd choirbox
sudo chmod 755 install.sh
./install.sh
```

commands:

| command| alias for| adapt in script|
|-|-|-|
|jackclient| connect device as jackclient|[script location](./scripts/startup/jacktripClient/jacktripClient.sh)|
|jackserver| connect device as jackserver|[script location](./scripts/startup/jacktripServer/jacktripServer.sh)|
|jackpatch| patch device based on $HOSTNAME.xml, the xml is adapted for servers or clients separately|[script location](./scripts/startup/patching/patch.sh)|
<!-- 
### time for a backup maybe?

!!! check actual disk names !!!!

```
sudo dd if=/dev/rdisk2 | gzip > pisound-jacktrip-img.gz
``` -->

### connect

```bash
jacktrip -C <IP> --clientname $HOSTNAME -n 8
```

### port forwarding

on your router make sure port 4464 is forwarding for TCP, port 61002 for UDP

## debugging

[iperf](https://www.haven2.com/index.php/use-iperf-to-test-port-forwarding-and-network-performance-between-participants-in-an-online-jam-session)

## starting

There should be 1 RPi/computer serving as server, the others are clients.

### Server

On the server, we must make sure jackd is running.

#### Mac OS X

Open Jackpilot. Adapt the settings according to [jack_setup](#jack_setup)

![jack pref](./images/jackpilot_preferences.png)
Run Jackpilot, then QJackctl.

In QJackctl, go to setup and make sure the settings correspond to [jack setup](#jack_setup)

open a terminal:

```bash
jacktrip -S
```

to start jacktrip in Hub server mode:
![server started](./images/server_start.png)

Once a client connects you should see him appearing on the server terminal:
![connected client](./images/client_connected.png)

### clients

open a terminal and enter:

```bash
jacktrip -C <server IP> --clientname $HOSTNAME -n 2
e.g. jacktrip -C choirbox1.local --nojackportsconnect --clientname $HOSTNAME -n 2
```

open the pd patch on all clients

### save jacktrip connections

```bash
jmess -s choirbox_connections.xml
```

#### disconnect

```bash
jmess -D
```

#### reload

```bash
jmess -D
jmess -c choirbox_connections.xml
```

### patching

#### master

Important on the master (Qjackctl): the master is a client as well, yet does not receive its inputs via jacktrip, but from the system. So we have to connect system to the pure data input, instead of the jacktrip receives.

The remote clients, of course, come into the jacktrip receives and should be patched this way.

#### clients

On the clients, we patch the system inputs to the jacktrip sends, and the jacktrip receives to the system outputs.

### BPM tapping

[python3 script](metronome.py), necessary to install [gpiozero](https://gpiozero.readthedocs.io/en/stable/installing.html) via apt.

## testen in ASIL lab

Voorheen hadden tussen de muide en de krook 25ms roundtrip delay. In het ASIL lab liggen de waardes hoger.

![ASIL switch rechtstreeks](./images/ASIL_switch_rechtstreeks.png) Rechtstreeks op de grote switch van het ASIL lab verkrijgen we 48ms loopback delay.

Om gecontroleerd te kunnen testen verbinden we, via statisch IP adres, 2 raspberry pi's met elkaar. De loopback delay dan is
![]()

### hotspots

choirbox1:5 password blokaslabs
