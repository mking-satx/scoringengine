#!/usr/bin/python3
#Requires `pip3 install python-nmap`

#PURPOSE: This will perform enumeration via nmap on an ip/range every xx minutes/seconds.
#		I would like it to be able to recognize if HTTP/80 is open and run dirb.
#
#USAGE: python3 leafenum.py <ip address> <port range> <options> 

import time
import os
import nmap
import sys
import subprocess
#import Popen

print(sys.argv[0], "is a work in progress")
print("Number of arguments: ", len(sys.argv))
print("The arguments are: ", str(sys.argv))

#If no ip address is given
if len(sys.argv) < 2:
    print ("USAGE: python3 scoringengine.py <ip address> <port range> <options>") #ADD SLEEP TIME (opt.2)
    sys.exit(0)

hostaddress = sys.argv[1]
portrange = sys.argv[2]

print("-----------" * 6)
print("Scanning " +hostaddress)
print("-----------" * 6)

try:
    nmscan=nmap.PortScanner() #init port scanner
    nmscan.scan(hostaddress,portrange) #scan host and ports
except nmap.PortScannerError:
    print("nmap not found ", sys.exc_info[0])
except:
    print("unexpected error ",sys.exc_info[0])
    sys.exit(0)

#loop for printing port output
for host in nmscan.all_hosts():
    sys.stdout = open('/var/www/html/index.html','w+')
    print("<html><h1>")
    print("Host : %s" % (hostaddress)) #display host ip
    print("State : %s" % nmscan[host].state())	#host state (up/down)
    print("</h1><body>")
    for proto in nmscan[host].all_protocols(): #checks for tcp/udp
        print("<br>")
        print("-----------" * 6)
        print("<br>")
        print("protocols : %s" % proto)
        print("<br><br>")
        lport = nmscan[host][proto].keys() #list ports for tcpc/udp
        sorted(lport)
        for port in lport:
            print("port : %s \t state : %s " % (port, nmscan[host][proto][port]['state']))
            print("<br>")
        print("</body></html>")

time.sleep(1)

#def parsefile(leaves):
#    with open (leaves,'a') as f:
#        line = f.readline()

#parsefile = open('leaves','r')

#with open('leaves','w+') as f:
   # line = f.readline()
    #for line in f:
        #p = Popen.communicate(stdin=subprocess.PIPE, stdout=subprocess.PIPE)
       # sys.stdout = Popen(subprocess.run
        #if 'port : 80        state : open' in line:
            #f.write("run nikto here")
        

    
   # p = subprocess.Popen(["ping","192.168.136.140"], stdin=subprocess.PIPE, stdout='f')



#IF "port : 80" FOUND, RUN NIKTO
