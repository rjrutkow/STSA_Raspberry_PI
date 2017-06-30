import time
import paho.mqtt.client as mqtt
import json
import uuid
import random


#Set the variables for connecting to the iot service
broker = ""
topic = "iot-2/evt/status/fmt/json"
username = "use-token-auth"
password = "+S_TiZF6HsvNmNL@0f" #auth-token
organization = "1ewlht" #org_id
deviceType = "myo"

topic = "iot-2/evt/status/fmt/json"
randNum=0




#Creating the client connection
#Set clientID and broker
clientID = "d:" + organization + ":" + deviceType + ":" + "Mymyo"
broker = organization + ".messaging.internetofthings.ibmcloud.com"
mqttc = mqtt.Client(clientID)

#Set authentication values, if connecting to registered service
if username is not "":
 mqttc.username_pw_set(username, password=password)

mqttc.connect(host=broker, port=1883, keepalive=60)


#Publishing to IBM Internet of Things Foundation
mqttc.loop_start() 

while mqttc.loop() == 0:

 randNum =random.randint(0,9) 
 msg = json.JSONEncoder().encode({"d":{"Myval":randNum}})
 
 mqttc.publish(topic, payload=msg, qos=0, retain=False)
 print "message published"

 time.sleep(5)
 pass
