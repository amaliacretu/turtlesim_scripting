#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import sys
import json

#online brokers
#broker = "test.mosquitto.org"
#broker = "broker.hivemq.org"
#broker = "iot.eclipse.org"

#local brokers
#broker = "127.0.0.1" # "localhost"

def on_log(client, userdata, flags, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection OK")
    else:
        print("Bad connection with rc code", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code: ", rc)


msg_cmdvel = {
    "linear_x": "2",
    "linear_y": "0",
    "linear_z": "0",
    "angular_x": "0",
    "angular_y": "0",
    "angular_z": "0"
}

data_out=json.dumps(msg_cmdvel)

client = mqtt.Client("ID1")

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker")
    sys.exit(-1)


while True:
    try:
        client.loop()
        client.publish("fleet/cmd_vel", data_out)
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break

client.disconnect()