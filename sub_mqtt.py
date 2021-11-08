#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

#online brokers
broker = "test.mosquitto.org"
#broker = "broker.hivemq.org"
#broker = "iot.eclipse.org"

#local brokers
# broker = "127.0.0.1" # "localhost"

def on_log(client, userdata, flags, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connection OK")
    else:
        print("Bad connection with rc code", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code: ", rc)

def on_message(client, userdata, msg):
    topic=msg.topic
    msg_decode=str(msg.payload.decode("utf-8"))
    print("message received on {} says {}".format(topic, msg_decode))


client = mqtt.Client("ID2")

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message


client.connect("localhost", 1883, 60)
client.subscribe("fleet/cmd_vel")


client.loop_start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        print("Exiting...")
        break

#time.sleep(10)

client.loop_stop()
client.disconnect()