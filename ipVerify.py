"""
---------------------------------------------------

I hope you use this package well, it is meant to verify whether or not an ip address is valid or not

;)

-- Made by john

Open source use it for whatever the fuck you want, just make sure it is not illegal because cmon mean we all wanna live at the end of the day

and freedom is fuggin dope and I don't see why you would want to give that up

"""


import socket
import requests
import os
import sys
import json

def verifALG(ipADDR: str):
    x = ipADDR.split(".")
    dot_count = ipADDR.count(".")
    
    # check if the starting value of the ip address is greater than 255
    if int(x[0]) > 255:
        return False

    # check if there are more than three dots
    if dot_count > 3:
        return False

    # check if the starting ip address is 240-255 which is reserved meaning that it is invalid.
    if 240 <= int(x[0]) <= 255:
        return False
    # same thing here except that it is 224-239 which I have nofucking clue what that could be
    if 224 <= int(x[0]) <= 239:
        return False

    if int(x[0]) == 172 and 16 <= int(x[1]) <= 31:
        return False 
    if int(x[0]) == 10:
        return False

    if ipADDR.startswith("0"):
        return False
    
    return True


def verifyREQUEST(ip: str):
    i = requests.get("http://ip-api.com/json/"+ip)
    i = i.text
    i = json.loads(i)

    if i["status"] == "success":
        return True
    else: 
        return False
    

def fullVerify(ip):
    if verifALG(ip) and verifyREQUEST(ip):
        return True
    else:
        return False

