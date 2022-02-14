import rospy
from nav_msgs.msg import Odometry
from datetime import datetime


def callback_receive_position_data(msg):
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	print(msg.pose.pose.position.x)
	print(msg.pose.pose.position.y)
	try:
		file.write(str(timestamp) + "," + str(msg.pose.pose.position.x) + "," + str(msg.pose.pose.position.y) + "\n")
	except:
		pass

rospy.init_node('position_subscriber')
pub = rospy.Subscriber("/uwb/odom", Odometry, callback_receive_position_data)
file = open("data_position.csv", "w")
file.write("timestamp" + "," + "X" + "," + "Y" + "\n")

rospy.spin()
rospy.loginfo("Node was stopped")
