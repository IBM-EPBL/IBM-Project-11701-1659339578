import json
import wiotp.sdk.device
import time
import ibmiotf.application
import ibmiotf.device

myConfig = {
    "identity": {
        "orgId": "jm6fjh",
        "typeId": "ESP",
        "deviceId": "esp-vlsm"
    },
    "auth": {
        "token": "1234567890"
    }
}

        
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name= "Vishal"

    latitude= 11.055712
    longitude= 76.804089
    mydata={'name': name, 'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=mydata, qos=0, onPublish=None)
    print("Data published to IBM IoT platform: ",mydata)
    time.sleep(20)

client.disconnect()
