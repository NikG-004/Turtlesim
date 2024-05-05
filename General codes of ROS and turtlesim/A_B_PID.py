#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import atan2, sqrt

# Constants for PID controller
KP = 1.0
KI = 0.1
KD = 0.5

# Global variables
current_pose = Pose()
target_point = Pose()
error = 0.0
error_sum = 0.0
last_error = 0.0
error_theta = 0.0

# Callback function for turtle's current pose
def pose_callback(data):
    global current_pose
    current_pose.x = 0
    current_pose.y = 0

# Callback function for target point
def target_callback(data):
    global target_point
    target_point.x = 3
    target_point.y = 3
 
# Calculate the error between current pose and target point
def calculate_error():
    global error, last_error, error_sum, error_theta
    error_x = target_point.x - current_pose.x
    error_y = target_point.y - current_pose.y
    error_theta = atan2(error_y, error_x) - current_pose.theta
    error = sqrt(error_x**2 + error_y**2)
    error_sum += error
    error_diff = error - last_error
    last_error = error
    return error, error_sum, error_diff, error_theta

# Apply PID control to move the turtle towards the target point
def move_turtle():
    global error, error_sum
    rospy.init_node('turtle_pid_controller')

    # Create a publisher to control the turtle's movement
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Create subscribers for current pose and target point
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.Subscriber('/target_point', Pose, target_callback)

    rate = rospy.Rate(10)  # Update rate in Hz

    while not rospy.is_shutdown():
        error, error_sum, error_diff, error_theta = calculate_error()

        # Calculate control commands using PID formula
        linear_vel = KP * error + KI * error_sum + KD * error_diff
        angular_vel = -KP * error_theta

        # Create a Twist message and set linear and angular velocities
        twist_msg = Twist()
        twist_msg.linear.x = linear_vel
        twist_msg.angular.z = angular_vel

        # Publish the Twist message
        pub.publish(twist_msg)

        # Check if the target point is reached
        if error < 0.1:
            rospy.loginfo("Target point reached!")
            break

        rate.sleep()

    # Stop the turtle's movement
    twist_msg.linear.x = 0.0
    twist_msg.angular.z = 0.0
    pub.publish(twist_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass


