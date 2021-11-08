#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import rospy
from geometry_msgs.msg import Twist
import json

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
    msg_decode=msg.payload.decode("utf-8")
    m_in=json.loads(msg_decode)
    fleet_msg = Twist()
    #fleet_msg.linear.x = int(msg_decode)
    pub.publish(fleet_msg)

    print("message received on {} says {}".format(topic, msg_decode))


client = mqtt.Client("ID2")

client.on_log = on_log
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message


client.connect("localhost", 1883, 60)
client.subscribe("fleet/cmd_vel")
rospy.init_node('fleet_script', anonymous=True)
pub = rospy.Publisher('fleet_cmd', Twist, queue_size=10)


client.loop_start()

while not rospy.is_shutdown():
    try:
        pass
    except rospy.ROSInterruptException:
        print("Exiting...")
        break

#time.sleep(10)

client.loop_stop()
client.disconnect()