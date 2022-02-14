import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from datetime import datetime

def callback_receive_luxmetre_data(msg):
	now = datetime.now()
	timestamp = datetime.timestamp(now)
	print(str(timestamp) + "," + X + "," + Y + "," + msg.data + "\n")
	try:
		file.write(str(timestamp) + "," + X + "," + Y + "," + msg.data + "\n")
	except:
		pass

def callback_receive_position_data(msg):
	#now = datetime.now()
	#timestamp = datetime.timestamp(now)
	global X, Y
	X = str(msg.pose.pose.position.x)
	Y = str(msg.pose.pose.position.y)



rospy.init_node('data_subscriber')
pub = rospy.Subscriber("/luxmetre", String, callback_receive_luxmetre_data)
pub = rospy.Subscriber("/uwb/odom", Odometry, callback_receive_position_data)
file = open("data.csv", "w")
file.write("timestamp" + "," + "X" + "," + "Y" + "," + "Lux" + "\n")

rospy.spin()
rospy.loginfo("Node was stopped")
