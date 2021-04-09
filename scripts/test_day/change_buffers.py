"""
A file to quickly alter the buffer sizes of ALL choirbox devices
"""
import netifaces as ni
from paramiko import SSHClient, AutoAddPolicy
import threading
import subprocess
from termcolor import colored
import argparse
from time import sleep
"""
first connect to all choirboxes
then check if jacktrip is running in server mode or client mode, if so stop.
alter the buffer size
restart jacktrip
"""

choirbox_list = [
    {
        "name": "choirbox1",
        "ip": "choirbox1.local",
        "type": "server",
        "status": {"ip": None,
                   "msg": None, }
    },
    {
        "name": "choirbox2",
        "ip": "choirbox2.local",
        "type": "client",
        "status": {"ip": None,
                   "msg": None, }
    },
    {
        "name": "choirbox3",
        "ip": "choirbox3.local",
        "type": "client",
        "status": {"ip": None,
                   "msg": None, }
    },
    {
        "name": "choirbox4",
        "ip": "choirbox4.local",
        "type": "client",
        "status": {"ip": None,
                   "msg": None, }
    },
    {
        "name": "choirbox5",
        "ip": "choirbox5.local",
        "type": "client",
        "status": {"ip": None,
                   "msg": None, }
    },
]


class choirbox():
    def __init__(self, device):
        self.name = device["name"]
        self.ip = device["ip"]
        self.type = device["type"]
        self.status = None
        pass

    def update_choirbox(self):
        self.check_gw()

    def check_gw(self):
        res = subprocess.call(['ping', '-c', '3', '-W', '1000', self.ip])
        if res == 0:
            color = 'green'
            print(colored(str("ping to "+self.ip+" OK"), color))
        elif res == 2:
            color = 'red'
            print(colored(str("no response from " +
                  self.ip+" "+self.type), color))
        else:
            color = 'red'
            print(colored(str("ping to "+self.ip+" failed!"), color))
        self.status = res

    def execute_cmd(self, cmd):
        client = SSHClient()
        if(self.status == None):
            self.check_gw()
            self.execute_cmd(cmd)
        elif(self.status == 0):
            client.load_system_host_keys()
            client.set_missing_host_key_policy(AutoAddPolicy())

            client.connect(self.ip, username="patch")
            stdin, stdout, stderr = client.exec_command(
                cmd, get_pty=True)  # , timeout=4
            exit_status = stdout.channel.recv_exit_status()          # Blocking call
            if(exit_status == 0):
                print("***DONE***")
                for line in stdout:
                    text = line.strip('\n')
                    print(text)
                    # gateway["status"]["msg"] = text
            else:
                print("***Error***", exit_status)
                for line in stdout:
                    text = line.strip('\n')
                    print(text)
                # gateway["status"]["msg"] = exit_status
        client.close()


if(__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("cmdfile", help="file with commands to execute",
                    type=str)
    args = parser.parse_args()

    x = []

    for idx, val in enumerate(choirbox_list):
        cb = choirbox(choirbox_list[idx])
        print("checking network connectivity for ", cb.name)
        cb.check_gw()
        if(cb.status==0):
            print("killing all jacktrip processes")
            cb.execute_cmd("killall jacktrip")
            # sleep(2)
            print("executing commands from ")
            #TODO right now we're looping through the choirboxes, if choirbox1 isn't server, then the server will be launched in a later time...
            with open(args.cmdfile) as f:
                cmd = f.read().splitlines()
                # cb.execute_cmd("jack_bufsize "+val)
                for i in cmd: 
                    print(cmd)
                    cb.execute_cmd(i)
            if(cb.type=="server"):
                print("starting jacktrip server for ", cb.name)
                cb.execute_cmd("/home/patch/choirbox/scripts/startup/jacktripServer/jacktripServer.sh &")
            print("starting jacktrip as client for ", cb.name)
            cb.execute_cmd("/home/patch/choirbox/scripts/startup/jacktripClient/jacktripClient.sh &")


    #     temp = threading.Thread(target=choirboxes.update_choirbox, args=(val))
    #     x.append(temp)
    #     x[idx].start()

    # for i in x:
    #     i.join()  # wait for all threads to finish
    # gateways.print_results()
