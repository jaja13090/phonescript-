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

country_prefix=data['country_prefix']


print(valid)

print(pays?)

print(country code )

print(line_type)

print(location)

print(carrier)

print(country_prefix)
