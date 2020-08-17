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

print ("author:jalil")

print ("Sarah mon coeur")

choice = input("""
[1] Simple DDoS

[2] PowerFul DDoS

[3] Phone Number information

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
    import re
import json
from urllib2 import urlopen


phone_number = raw_input("Enter Phone Number:  ")

key = "22157d91a21b4bea9804521fda0fe886"

url = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + phone_number + "&country_code=FR&format=1"

response = urlopen(url)
data = json.load(response)

if ['valid'] == True:
    print("Phone Number valid")
if ['valid'] == False:
    print("Invalid Phone Number")

valid=data['valid']

country_name=data['country_name']

country_code=data['country_code']

line_type=data['line_type']

carrier=data['carrier']

location=data['location']

