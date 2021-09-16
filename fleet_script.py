#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

class FleetCommands:

    def __init__(self):
        self.pub = rospy.Publisher('fleet_cmd', Twist, queue_size=10)
        self.fleetMsg()


    def fleetMsg(self):
        fleet_msg = Twist()

        rate = rospy.Rate(10) # 10hz
    
        while not rospy.is_shutdown():
            fleet_msg.linear.x = 2.0
            fleet_msg.linear.y = 0.0
            fleet_msg.linear.z = 0.0

            fleet_msg.angular.x = 0.0
            fleet_msg.angular.y = 0.0
            fleet_msg.angular.z = 1.8

            self.pub.publish(fleet_msg)
            rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node('fleet_script', anonymous=True)
        FleetCommands()
    except rospy.ROSInterruptException:
        pass