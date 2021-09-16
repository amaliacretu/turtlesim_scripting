#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

class MiddleWare:

    def __init__(self):
        self.pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber("fleet_cmd", Twist, self.callback)

    def callback(self, data):
        self.pub.publish(data)


if __name__ == '__main__':
    try:
        rospy.init_node('listen_2fleet', anonymous=True)
        MiddleWare()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
