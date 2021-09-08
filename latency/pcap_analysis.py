"""
Based on the pcap file provided in the pcapFileName var the script
analyse the packet latency.
Traffic generated with a modified version of UltraPing script
"""

import matplotlib.pyplot as plt
import pyshark
import numpy as np
import os
import sys
import csv
from datetime import datetime, date

cur_time = datetime.now().strftime("%H%M%S")
cur_date = date.today().strftime("%d%m%Y")

outputCsvFile = os.getcwd()+"/latency/out_"+cur_date+"_"+cur_time+".csv"
pcapFileName = os.getcwd()+"/latency/capture.pcapng"


def filter_csv(csvFileName, outputCsvFile):
    with open(csvFileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
    
        for row in csv_reader:
            if('UDP' in row):
                print(row)

def filter_cap(pcapFileName, outputCsvFile):
    capture = pyshark.FileCapture(pcapFileName)
    capture.set_debug()
    # capture.sniff(timeout=60)
    tmpSessions = {}
    sessions = []
    latency = []
    lastLatency = 0
# loop in the pcap capture file and analyse packet per packet
    for packet in capture:
        # filter only UDP (to do: filter the port)
        if 'udp' in packet:
            # print(packet)
            try:
                data = packet.data.data
                payload = data.rstrip('61')
                timestamp = packet.sniff_timestamp
                tmpSession = {payload: timestamp}
                visualize_packets(payload, 16)
                # check if packet is the first one (client to server)
                if tmpSessions.get(payload) is None:
                    # if packet is the first one append the info in the sessions variable
                    tmpSessions.update(tmpSession)
                else:
                    # if packet is the second one retrieve the info from sessions and calculate the latency
                    timestampOrig = tmpSessions.pop(payload)
                    lat = (float(timestamp)-float(timestampOrig))*1000
                    jitter = lastLatency - lat
                    lastLatency = lat
                    # add all info in the sessions variable (for future use?)
                    session = [timestampOrig, timestamp, str(lat), str(jitter)]
                    sessions.append(session)
            except:
                print("error: ", packet)
                pass

    capture.close()

    sessions = np.array(sessions)
    np.savetxt(outputCsvFile, sessions, delimiter=',', fmt='% s')

def visualize_packets(data, bitrate):
    n=int(bitrate/4)
    # payload= [data[i:i+n] for i in range(0, len(data), n)]
    payload = map(''.join, zip(*[iter(str(data))]*int(bitrate/4)))
    plt.plot(payload)

def main():
    # print command line arguments
    # Mac Os: Make sure Wireshark is on your PATH: 
    # export PATH=$PATH:/Applications/Wireshark.app/Contents/MacOS/
    for arg in sys.argv[1:]:
        print(arg)
    if(len(sys.argv) >= 3):
        if(sys.argv[1]=="cap"):
            filter_cap(pcapFileName=sys.argv[2], outputCsvFile=outputCsvFile)
        else:
            filter_csv(csvFileName=sys.argv[2], outputCsvFile=outputCsvFile)


if __name__ == '__main__':
    main()
