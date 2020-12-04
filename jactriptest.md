#initial testing

## choose master server
we pick choirbox1, running
 
`Linux choirbox1 4.19.71-rt24-v7l+ #1 SMP PREEMPT RT Wed Mar 11 17:15:58 EET 2020 armv7l GNU/Linux`

the 4.x branch RT kernel





## PD-patch for testing latency
- requires cyclone
- help > findexternals > cyclone



# test setups
## jack_iodelay

jack_iodelay is a standard tool included with jack to measure the delay in a asignal path. I ran the folowwing tests

### 2 RT kernel boxes
```
$ uname -a
Linux choirbox1 4.19.71-rt24-v7l+ #1 SMP PREEMPT RT Wed Mar 11 17:15:58 EET 2020 armv7l GNU/Linux
```
running jackserver on one box:
```jacktrip -S```
and also 
```jacktrip -C localhost --clientname choirbox1```

while on the other box
```jacktrip -C choirbox1 --clientname choirbox2```

results in 10.666 to 12ms delay when patching 
jack-iodelay out > choirbox2send > (jacktripserver receive) > (jacktripserver send choirbox2) > choirbox2 receive > jack_iodelay in
running 
``` jack_iodelay```
should give this output
```
   512.000 frames     10.667 ms total roundtrip latency
	extra loopback latency: 511 frames
	use 255 for the backend arguments -I and -O
   576.001 frames     12.000 ms total roundtrip latency
	extra loopback latency: 576 frames
	use 288 for the backend arguments -I and -O
 ```


patching an extra round to the jackserver over another channel gives:
```   
896.000 frames     18.667 ms total roundtrip latency
extra loopback latency: 895 frames
use 447 for the backend arguments -I and -O
```

