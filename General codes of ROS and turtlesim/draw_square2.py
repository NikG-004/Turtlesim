#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("draw_square")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    duration = 1.0
    rate = rospy.Rate(1000)
    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.y = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)

        rate.sleep()
    
    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)

        rate.sleep()
    
    start_time = rospy.Time.now().to_sec()
    
    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 1.57079633
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()    

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 1.57079633
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 1.57079633
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        pub.publish(msg)

        rate.sleep()

    start_time = rospy.Time.now().to_sec()

    while rospy.Time.now().to_sec() - start_time < duration:
        msg = Twist()
        msg.linear.x = 0.0
        msg.angular.z = 1.57079633
        pub.publish(msg)

        rate.sleep()
    rospy.spin()    




