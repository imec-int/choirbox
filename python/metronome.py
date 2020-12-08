import gpiozero
from gpiozero import Button, LED
from time import sleep, time
import socket
import sys
from signal import pause
# import thread module
import threading


import sys
sys.path +=['.']
from metronomeStates import BPMStateMachine
'''
In this script we want to light the LED at pin <> according to the signal coming from PD.
In another thread/process we want to alter the BPM of the pd patch by getting the input tapped tempo.

The available pins, not used by the pisound are GPIO:
2, 3, 4, 27, 22, 5, 7, 23, 14, 15

references:
https://github.com/defaultxr/taptempo.py


'''
button = Button('GPIO2')
led = LED('GPIO3')
bpm = 60.0
BPM_duration = 60.0/bpm
times = []


def addtime(times):
    if(type(times) != list):
        raise(TypeError)
    t = time()
    if(len(times) == 0):
        tdiff = 0  # initial seed
    else:
        tdiff = t - times[-1][0]
    return (t, tdiff)


def averagetimes(times):
    averagetime = sum([row[1] for row in times])/float(len(times))
    bpm = (1.0/(averagetime/60.0))
    return (averagetime, bpm)


def _button_callback():
    global t, BPM_duration, bpm
    #blink led on touches
    led.blink(on_time=0.01, off_time=0.01,n=2,background=True)
    #check which state we are in and go in to tapping state
    if(bpm_sm.is_pdSendsBPM):
        bpm_sm.tapped()
    # set a programming timer for deciding when programmed
    if(t.is_alive):
        t.cancel()
        t = threading.Timer(BPM_duration*2, sendBPM)
    t.start()
    #calculate the time difference between pushes
    timestamp, tdiff = addtime(times)
    times.append([timestamp, tdiff])
    if(len(times) > 1):
        # remove first element if it's either the initial seed
        # or when the list reaches max length
        if(times[0][1] == 0 or len(times) > 16):
            del(times[0])
        (BPM_duration, bpm) = averagetimes(times)
        # print(f'detected BPM: {bpm}, avg_time = {BPM_duration}')
'''
fake function, to be replaced with response from pd #TODO
go function needs to be implemented based on response from pd!
'''
def receiveACKfromPD():
    print(f"BPM PROGRAMMED {BPM_duration, bpm}")
    bpm_sm.go()

'''
sendBPM
transmits the amount of ms between each pulses to pd
'''
def sendBPM():
    print("send BPM")
    bpm_sm.tapStopped()
    # SEND BPM TO PD #TODO
    t.cancel()
    times.clear()
    # wait for response from pd to switch back to normal state
    t_ack_pd = threading.Timer(0.2, receiveACKfromPD)
    t_ack_pd.start()

'''
if we've programmed the BPM, then we blink the LED on the beats of the pd patch
'''
def rcvBEATfromPD():
    if(bpm_sm.is_pdSendsBPM):
        led.blink(on_time=0.005, off_time=0.005,n=1,background=True)
    #TODO program a fake beat again
    global t_fake_beat
    t_fake_beat = threading.Timer(BPM_duration, rcvBEATfromPD)
    t_fake_beat.start()

def Main():
    button.when_pressed = _button_callback
    t_fake_beat.start() #TODO
    pause()

bpm_sm = BPMStateMachine()
t = threading.Timer(1.5, sendBPM)
t_fake_beat = threading.Timer(BPM_duration, rcvBEATfromPD) #TODO

if __name__ == '__main__':
    Main()
