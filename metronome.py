import gpiozero
from gpiozero import Button, LED
from time import sleep, time
import socket
import sys
from signal import pause

# import thread module 
from _thread import *
import threading
# or will we use asyncio? 
import asyncio

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

BPM = 60 
times = []

print_lock = threading.Lock() 

def addtime(times):
    if(type(times)!=list):
        raise(TypeError)
    t = time()
    if(len(times)==0):
        tdiff = 0 # initial seed
    else:
        tdiff = t - times[-1][0]
        
    return (t,tdiff)
def averagetimes(times):
    averagetime = sum([row[1] for row in times])/float(len(times))
    bpm = (1.0/(averagetime/60.0))
    return (averagetime, bpm)

def _button_callback():
    timestamp, tdiff = addtime(times)
    if(tdiff>2):
            print('renew')
            times.clear()
            tdiff = 0
    times.append([timestamp,tdiff])
    if(len(times)>1):
        # remove first element if it's either the initial seed 
        # or when the list reaches max length
        if(times[0][1] == 0 or len(times)>16):
            del(times[0])
        (averagetime, bpm) = averagetimes(times)
        print(f'detected BPM: {bpm}, times = {times}')

# thread function 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            print_lock.release() 
            break
  
        # reverse the given string from client 
        data = data[::-1] 
  
        # send back reversed string to client 
        c.send(data) 
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    # we open a socket connection to send our tapped tempo to pd, and receive the pulses from pd
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_address=('localhost',13001)
    # print(f'starting up on {server_address[0]} port {server_address[1]}')
    # sock.bind(server_address)
    # sock.listen(1)
    
    button.when_pressed = _button_callback

    # # a forever loop until client wants to exit 
    # while True: 
  
    #     # establish connection with client 
    #     c, addr = s.accept() 
  
    #     # lock acquired by client 
    #     print_lock.acquire() 
    #     print('Connected to :', addr[0], ':', addr[1]) 
  
    #     # Start a new thread and return its identifier 
    #     start_new_thread(threaded, (c,)) 
    # s.close() 
    pause()

  
  
if __name__ == '__main__': 
    Main() 




