
# phase 1 setup

## Hardware
## Software

 
### image
patchbox OS base image https://blokas.io/patchbox-os/
 
### username/password
patch / blokaslabs
 
### initial login
setup wizard
update to latest
 
### jack setup
48000/128/2
 
### wifi setup
only for easy access
 
### change hostname to something sensible
> nano /etc/hostname

I picked choirbox1 to choirbox3

### kernel PREEMPT
is enabled by default on the patchbox OS

> uname -v 
> #1 SMP PREEMPT RT Wed Mar 11 17:15:58 EET 2020
 
### jack and jacktrip
changing fast due to high-paced development!

### dev env
> sudo apt install -y --no-install-recommends build-essential \ 
> librtaudio-dev qt5-default autoconf automake libtool make \ 
> libjack-jackd2-dev qjackctl audacity git

### jacktrip
> git clone https://github.com/jacktrip/jacktrip.git

To compile using the build script:
> cd jacktrip/src
> ./build
> cd ../builddir
> sudo make install
> cd

### jmess (patch connection state saving)

> git clone https://github.com/jacktrip/jmess-jack.git
> cd jmess-jack/jmess/src
> ./build
> sudo make install

### time for a backup maybe?

!!! check actual disk names !!!!

> sudo dd if=/dev/rdisk2 | gzip > pisound-jacktrip-img.gz
 

 

 
 
 

