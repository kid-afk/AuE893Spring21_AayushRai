import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897


speed=0.2

def move_square():
	rospy.init_node('move_square',anonymous = True)
	pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size = 10)
	vel_msg=Twist()
	side_length = 2
	rotations = 4

	current_rotation = 0
	while current_rotation < rotations:
		move_in_line(side_length,vel_msg,pub)
		rotate(vel_msg,pub)
		current_rotation+=1

def move_in_line(side_length,vel_msg,pub):
	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.y = 0
	vel_msg.angular.z = 0
	t0 = rospy.Time.now().to_sec()
	distance_travelled = 0
	while distance_travelled < side_length:
			pub.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			distance_travelled = speed*(t1-t0)

	vel_msg.linear.x = 0
	pub.publish(vel_msg)

def rotate(vel_msg,pub):
	angular_speed = 0.2
	vel_msg.angular.z = angular_speed
	t0	= rospy.Time.now().to_sec()
	angle_travelled = 0

	while ( angle_travelled < PI/2.0 ):
			pub.publish(vel_msg)
			t1 = rospy.Time.now().to_sec()
			angle_travelled=angular_speed*(t1-t0)

	vel_msg.angular.z = 0
	pub.publish(vel_msg)

if __name__ == '__main__':
	try:
		move_square()
	except rospy.ROSInterruptException:
		pass	




