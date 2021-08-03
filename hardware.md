# hardware components

## compute engine

preferably use raspberry pi 4: gigabit ethernet

## soundcard

### goals

1. low latency
2. audio input as well as output
   1. XLR/jack combi prefered input
   2. headphone out
3. good integration with raspberry pi/linux
4. price
5. chipset used?

### pisound

[link](https://blokas.io/pisound/)

1. loopback latency: 2.092ms
2. stereo jack input & output
   1. no XLR input, only stereo jack. So no balanced signal as well (noise?)
   2. good
3. good integration (scripts presented)
4. expensive: Eur 99

### zero raspberry pi sound card

[link](https://www.audioinjector.net/rpi-zero)

1. latency?
2. stereo input & output
   1. via extension boards: RCA, stereo jack, volume meters
   2. No XLR (or balanced signal)
3. unknown
4. approx. Eur 14
5. [Cirrus Logic WM8731S](https://www.cirrus.com/products/wm8731/)

### audioinjector ultra 2

[link](https://shop.audioinjector.net/detail/Sound_Cards/Ultra+2)

1. latency?
2. stereo input & output
   1. via extension boards: RCA, stereo jack, volume meters
   2. No XLR (or balanced signal), yet capable!
3. unknown
4. approx. Eur 60
5. [Cirrus Logic cs4265](https://www.cirrus.com/products/cs4265/) + balanced to mono chip [TI OPA1692](https://www.ti.com/product/OPA1692)

### HifiBerry DAC+ ADC

[link](https://www.hifiberry.com/shop/boards/hifiberry-dac-adc/)

1. Latency ?
2. RCA output, 3.5mm input jack
   1. No balanced input
3. linux kernel > 4.18
4. approx Eur 42
5. [TI PCM1851 ADC](https://www.ti.com/product/PCM1851) + [TI PCM5122 audio DAC](https://www.ti.com/product/PCM5122)

- To get XLR input: you can not get balanced audio, you can get semi-balanced though (possibly more noise)
- To get stereo jack output, connect stereo Male RCA to stereo Female jack connector

### HiFiBerry DAC+ ADC Pro

[link](https://www.hifiberry.com/shop/boards/hifiberry-dac-adc-pro/)

1. latency?
2. RCA output, 3.5mm input jack
   1. No balanced input
3. linux kernel > 4.19.60
4. approx Eur 55
5. [TI PCM1863 ADC](https://www.ti.com/product/PCM1851) + [TI PCM5122 audio DAC](https://www.ti.com/product/PCM5122)

- To get XLR input: you can not get balanced audio, you can get semi-balanced though (possibly more noise)
- To get stereo jack output, connect stereo Male RCA to stereo Female jack connector