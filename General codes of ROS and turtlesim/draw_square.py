#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('turtle_square')  # Initialize the ROS node

velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  # Create a publisher to control the turtle's velocity


def move(linear_speed, angular_speed, duration):
    # Function to set the turtle's linear and angular velocity for a specified duration
    vel_msg = Twist()
    vel_msg.linear.x = linear_speed
    vel_msg.angular.z = angular_speed

    rate = rospy.Rate(100000)  # Set the loop rate in Hz

    start_time = rospy.Time.now().to_sec()  # Get the current time

    while rospy.Time.now().to_sec() - start_time < duration:  # Loop until the specified duration is reached
        velocity_publisher.publish(vel_msg)  # Publish the velocity message
        #rate.sleep()  # Sleep to maintain the loop rate

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

def draw_square():

    linear_speed = 4.0  # Linear speed of the turtle (m/s)
    angular_speed = 0.7854  # Angular speed of the turtle (rad/s) - approximately 90 degrees per second
    duration = 1.0  # Duration to move forward and turn (seconds)

   
    # Move forward
    move(linear_speed, 1.27323955*angular_speed, 6.28318)

    # Turn right
    move(0.0, 2*angular_speed, duration)

    # Move forward
    move(linear_speed/4, 0.0, duration)

    # Turn left
    move(0.0, 6*angular_speed, duration)

    # Move forward
    move(linear_speed, 1.69765273*angular_speed, 4.7)

    # Turn right
    move(0.0, 2*angular_speed, duration)

    # Move forward
    move(linear_speed/4, 0.0, duration)

    # Turn left
    move(0.0, 6*angular_speed, duration)

    # Move forward
    move(linear_speed, 2.54647909*angular_speed, 3.14159265)



if __name__ == '__main__':
    
    
    
    try:
        draw_square()  # Draw a square shape
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
