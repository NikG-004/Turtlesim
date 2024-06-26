#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import math

data = []
data_set = []
class TurtleBot:

    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)

        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)
        

    def update_pose(self, data):
        
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):

        return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=0.5):
        
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=8.5):
        
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)
    
    def generate_sine_wave(self):
        global data_set
        amplitude = 3.0  # Amplitude of the sine wave
        frequency = 1  # Frequency of the sine wave
        phase_shift = 0.0  # Phase shift of the sine wave
        a = 0

        while a <= 4*math.pi: 
            data.append(a)
            data_set.append(amplitude * math.sin(frequency * a + phase_shift))

            a += 0.1
        """plt.plot(data, data_set)   
        plt.show()"""
        print(data)
        print(data_set)

    def move2goal(self):
        no_of_iterations = int(input("No. of Iterations: "))
        rate = rospy.Rate(1000)

        for _ in range(no_of_iterations):
            goal_pose = Pose()

            goal_pose.x = float(input("Enter x: "))
            goal_pose.y = float(input("Enter y: "))

            vel_msg = Twist()

            distance_tolerance = 0.01
            angle_tolerance = 0.001

            while round(abs(self.steering_angle(goal_pose) - self.pose.theta), 3) >= angle_tolerance:
                vel_msg.angular.x = 0
                vel_msg.angular.y = 0
                vel_msg.angular.z = self.angular_vel(goal_pose)
                #print(self.pose.theta)
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

            # Stop rotation before moving linearly
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            #print("Nikhil")

            while round(self.euclidean_distance(goal_pose), 2) >= distance_tolerance:
                # Update the goal position to account for the rotation
                """updated_goal_pose = Pose()
                updated_goal_pose.x = goal_pose.x - self.pose.x
                updated_goal_pose.y = goal_pose.y - self.pose.y"""

                vel_msg.linear.x = self.linear_vel(goal_pose)
                vel_msg.linear.y = 0
                vel_msg.linear.z = 0
                #print(self.euclidean_distance(goal_pose))
                self.velocity_publisher.publish(vel_msg)
                self.rate.sleep()

            # Stop linear motion after reaching the goal
            vel_msg.linear.x = 0
            self.velocity_publisher.publish(vel_msg)

        # Stop the robot at the end of the iterations
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass
