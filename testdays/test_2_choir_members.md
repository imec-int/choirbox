# test day 2

> Date: TBD
> number of people: 4 choir + 1 instructor
> locations: de Krook?

## things to check

### additional jacktrip techniques

|technique|jacktrip argument| variable|help|
|--|--|--|--|
|redundancy|-r, --redundancy|# (1 or more)  |Packet Redundancy to avoid glitches with packet losses (default: 1)|
| network dropouts|-z|-|wavetable repeat last packet instead of muting with zeroes if network packet droput happens|
|round-trip audio delay|-x, --examine-audio-delay|print_interval_in_secs|Print round-trip audio delay statistics. See `-x help' for details.|

### comparison of microphones

- types
- stereo vs mono cables
- pisound: balanced audio input possible?

### OPTIONAL SIGNAL PROCESSING

|technique|jacktrip argument| variable|help|
|--|--|--|--|
|add effects|-f, --effects # | paramString |  Turn on incoming and/or outgoing compressor and/or reverb in Client - see `-f help' for details|
|audio limiter|-O, --overflowlimiting | i\|o[w]\|io[w]\|n|Use audio limiter(s) in Client, i=incoming from network, o=outgoing to network, io=both, n=no limiters, w=warn if limiting (default=n). Say -O help for more.|
| planned amount of sources|-a, --assumednumclients |# (1,2,...) |Assumed number of Clients (sources) mixing at Hub Server (otherwise 2 assumed by -O)|

### different VLANs

can we **easily** integrate jacktrip when people can't access their own routers external IP address? Port forwarding?

[useful setup link for port forwarding for jacktrip](https://docs.google.com/document/d/18pbu2xQRv521NKvHuYHjIVXRcLFqcDsqYnfKixyuyGg/edit)

### nss-mdns
[https://github.com/lathiat/nss-mdns](https://github.com/lathiat/nss-mdns)


