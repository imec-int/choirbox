# test day 1

> Date:
>
> number of people: 4 choir + 1 instructor
>
> locations: Krook +4

## tech constraints

1. VLANs:
   1. as all network ports in the krook +4 are enabled via VLANs, we have to make sure all of them are on the same VLAN in order for them to get an IP address in the same range and to be able to have bidirectional communication.
2. As all devices were on the same VLAN in the end, the test doesn't incorporate a lot of router or firewall hopping.
3. We used a buffersize of 128 (not the lowest) as to be able to go lower if needed.

## things we want to check

1. Is the **audio** latency sufficiently low to sing together?
   1. Does a singer prefer to hear themselves via headphones or rather not?
2. Is there a need for **visual** feedback?
3. How is the audio **quality**?
4. what are first things that need to be **improved**?

## conclusions

### Is the **audio** latency sufficiently low to sing together?

Yes, the singers had the **feeling** that their was possibly a slight delay on their own voice, but weren't 100% sure.

This could be something useful to test: for next test, implement the voice of the singer in a local feedback loop and have it removed from the mix he/she receives. Is this better than having their own voice being transmitted back and forth?

### Is there a need for visual feedback?

Yes, we used `whatsapp` in parallel, with its audio off. This proved to be a welcome combination, even though there was clearly more visual delay then auditive. The instructor made the comparison with instruments were there's a delay between touch (action) and auditive response (output): musicians adapt to the constraints as long as the auditive sync can be made.

### audio quality

there was 50Hz noise introduced by one of the devices.

Also, soundquality could drastically improved. The combination headphones (closed/semi-open/open?) and microphone need to be investigated.

### what are first things that need to be **improved**?

1. Audio quality

een dingetje dat nog niet op de github staat is hun bezorgdheid rond latency over reguliere wifi/de verschillende incoming audio streams vs. optie dirigent als centrale hub waar de verschillende audio streams tot een enkele worden gemixt en gedispatcht 