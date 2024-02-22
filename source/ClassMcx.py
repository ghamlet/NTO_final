import requests
import json
import binascii

class mcx():
    def __init__(self) -> None:
        pass
    def move(self, name, x, y, z, t, g) -> bool:
        #position z
        positionMode = False
        if positionMode:
            if z == 0:
                z = 150
            elif z == 1:
                z == 70
            elif z == 1:
                z == 90

        msg = {
            'robot_name': name,
            'N': '0',
            'X': x,
            'Y': y,
            'T': t,
            'G': z,
            'V': g,
            'D0': '0',
            'L1': '0',
            'L2': '0',
            'L3': '0',
            'L4': '0',
            'P': '0',
            'Text': '' 
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            r = requests.post("http://127.0.0.1:17360/message", data=json.dumps(msg), headers=headers) #send command message
            return True, msg
        except:
            return False, msg
        
    def getImage(self, name):
        try:
            if name == "Cam2":
                r = requests.get("http://127.0.0.1:17362/image", stream=True, timeout=1) #stream image
                return binascii.unhexlify(r.text.encode('utf-8'))
            
            elif name == "Cam1":
                r = requests.get("http://127.0.0.1:17361/image", stream=True, timeout=1) #stream image
                return binascii.unhexlify(r.text.encode('utf-8'))
        except:
            return None
    
    def getData(self):
        try:
            r = requests.get("http://127.0.0.1:17363/data", stream=True, timeout=1) #get data from manipulator
            return str(r.text)
        except:
            None

