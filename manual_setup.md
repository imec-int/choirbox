# Manual installation

## choirbox repo

```bash
git clone https://github.com/imec-int/choirbox.git
```

## change hostname to something sensible

```bash
sudo hostname <new hostname>

sudo nano /etc/hostname
sudo nano /etc/hosts
sudo apt-get update && sudo apt-get upgrade -y
```

We picked choirbox1 to choirbox5

## jack and jacktrip

changing fast due to high-paced development!

Steps to build jacktrip from git repo:

```bash
git clone https://github.com/jacktrip/jacktrip.git
sudo apt install -y --no-install-recommends build-essential librtaudio-dev qt5-default autoconf automake libtool make libjack-jackd2-dev qjackctl audacity git
cd jacktrip/src && ./build
cd ../builddir && sudo make install
cd
```

## jmess (patch connection state saving)

```bash
git clone https://github.com/jacktrip/jmess-jack.git
cd jmess-jack/jmess/src && ./build
sudo make install
cd
```

## kernel PREEMPT

is enabled by default on the patchbox OS
but not on newest image...
stick to stock 5.4.x kernel at the moment

```bash
uname -v
```

> \#1 SMP PREEMPT RT Wed Mar 11 17:15:58 EET 2020

### time for a backup maybe?

!!! check actual disk names !!!!

```bash
sudo dd if=/dev/rdisk2 | gzip > pisound-jacktrip-img.gz
```

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

### jacktrip

#### jacktrip server

open a terminal:

```bash
jacktrip -S
```

to start jacktrip in Hub server mode:
![server started](./images/server_start.png)

Once a client connects you should see him appearing on the server terminal:
![connected client](./images/client_connected.png)

### jacktrip clients

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

#### server

Important on the server (Qjackctl): the server is a client as well, yet does not receive its inputs via jacktrip, but from the system. So we have to connect system to the pure data input, instead of the jacktrip receives.

The remote clients, of course, come into the jacktrip receives and should be patched this way.

#### clients

On the clients, we patch the system inputs to the jacktrip sends, and the jacktrip receives to the system outputs.
