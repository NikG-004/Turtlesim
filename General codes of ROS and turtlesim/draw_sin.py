#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

import math

class TurtleSineWave:
    def __init__(self):
        rospy.init_node('turtle_sine_wave', anonymous=True)

        # Create a publisher to control the turtle's velocity
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # Create a subscriber to get the turtle's pose (position and orientation)

    def move(self, linear_speed, angular_speed):
        # Function to set the turtle's linear and angular velocity
        vel_msg = Twist()
        vel_msg.linear.x = linear_speed
        vel_msg.angular.z = angular_speed
        self.velocity_publisher.publish(vel_msg)

    def stop(self):
        # Function to stop the turtle's movement
        vel_msg = Twist()
        self.velocity_publisher.publish(vel_msg)

    def make_sine_wave(self):
        # Function to make a sine wave pattern using the turtle

        frequency = 5  # Frequency of the sine wave (in Hz)
        amplitude = 5.0  # Amplitude of the sine wave
        x_increment = 0.1  # Increment value for x-axis
        rate = rospy.Rate(10)  # Loop rate in Hz

        while not rospy.is_shutdown():
            x = 0.0  # Initial x-coordinate
            y = 0.0  # Initial y-coordinate

            # Iterate over the x-axis and calculate y-coordinate based on the sine wave equation
            while x <= 2 * math.pi:
                y = amplitude * math.sin(frequency * x)

                # Move the turtle to the calculated position
                self.move(x, y)

                x += x_increment  # Increment x-axis

                rate.sleep()  # Sleep to maintain the loop rate

            self.stop()  # Stop the turtle's movement

if __name__ == '__main__':
    try:
        # Create an instance of the TurtleSineWave class
        turtle = TurtleSineWave()
        turtle.make_sine_wave()  # Run the turtle sine wave program
    except rospy.ROSInterruptException:
        pass
