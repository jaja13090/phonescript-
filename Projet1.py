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
V 1.0
                                                                          
""")

print ("Instagram jalil_rhu")

print ("author:ledz")

print ("Sarah mon coeur")

choice = input(""""
[1] Simple DDoS

[2] PowerFul DDoS

[3] Phone Number information

[4] Advanced Phone Number information 

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
   time.sleep(4
     print("\033[1;94mNumbers 4 Selected")
    print " "
    execfile("Suce.py")
else:
  print("Error")
