#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

def callback(data):
    pub.publish(data)
    

if __name__ == '__main__':
    try:
        rospy.init_node('listen_2fleet', anonymous=True)
        rospy.Subscriber("fleet_cmd", Twist, callback)
        rospy.spin()

    except rospy.ROSInterruptException:
        pass
