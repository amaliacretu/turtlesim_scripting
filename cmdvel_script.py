#!/usr/bin/env python
# license removed for brevity

import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('script_cmd', anonymous=True)
    my_msg = Twist()
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        my_msg.linear.x = 2.0
        my_msg.linear.y = 0.0
        my_msg.linear.z = 0.0

        my_msg.angular.x = 0.0
        my_msg.angular.y = 0.0
        my_msg.angular.z = 1.8

        pub.publish(my_msg)
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass