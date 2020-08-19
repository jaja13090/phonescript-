import time
import os

os.system("clear")

print("""
\033[1;91m    

|  _ \ _ __ ___ (_) ___| |_ 
| |_) | '__/ _ \| |/ _ \ __|
|  __/| | | (_) | |  __/ |_ 
|_|   |_|  \___// |\___|\__|
              |__/    
V 1.5

==Projet==By==LeDz==Devv==

Instagram:jalil_rhu

==Check Read.me to more details==                                                                  
""")

choice = input("""
[1] Simple DDoS

[2] PowerFul DDoS

[3] Phone Number information

[4] Ping ip adress  

[5]Advanced phone number info

\033[1;95mPlease Enter Your Choice: """)

if choice == 1:
    time.sleep(4)
    print("\033[1;94mNumbers 1 Selected")
    print " "
    execfile("ddos.py")
if choice == 2:
    time.sleep(4)
    print("\033[1;94mNumbers 2 Selected")
    print " "
    execfile("ssh.py")
if choice == 3:
    time.sleep(4)
    print("\033[1;94mNumbers 3 Selected")
    print " "
    execfile("PhoneNumber.py")
if choice == 4:
    time.sleep(4)
    print("\033[1;94mNumbers 4 Selected")
    print (" ")
    execfile("info.py")
if choice == 5:
    time.sleep(4)
    print("\033[1;94mNumbers 5 Selected")
    print " "
    execfile("infotel.py")
else:
    print("Error")
