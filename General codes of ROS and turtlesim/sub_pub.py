#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback_function(msg):
    # Process the received message
    rospy.loginfo("Received message: %s", msg.data)

def publisher_subscriber_example():
    # Initialize the ROS node
    rospy.init_node('publisher_subscriber_example')

    # Create a publisher
    pub = rospy.Publisher('my_topic', String, queue_size=10)

    # Create a subscriber
    sub = rospy.Subscriber('my_topic', String, callback_function)

    # Set the publishing rate
    rate = rospy.Rate(1)  # 1 Hz publishing rate

    # Start the main loop
    while not rospy.is_shutdown():
        # Create a message
        msg = String()
        msg.data = "Hello, ROS!"

        # Publish the message
        pub.publish(msg)

        # Sleep according to the publishing rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_subscriber_example()
    except rospy.ROSInterruptException:
        pass
