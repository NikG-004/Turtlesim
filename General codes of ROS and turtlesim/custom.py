#!/usr/bin/env python3

import rospy
from my_robot_controller.msg import Position

def publisher():
    rospy.init_node('custom_message_publisher', anonymous=True)
    pub = rospy.Publisher('custom_topic', Position, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    # Create a custom message object
    msg = Position()
    msg.message = "John"
    msg.x = 25
    msg.y = 25

    while not rospy.is_shutdown():
        pub.publish(msg)
        rospy.loginfo("Published: %s, %d, %d", msg.message, msg.x, msg.y)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
