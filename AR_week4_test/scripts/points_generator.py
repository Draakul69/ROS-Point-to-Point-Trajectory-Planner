#!/usr/bin/env python

import rospy
import numpy as np
import random as ra
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Float32
from AR_week4_test.msg import cubic_traj_param
pos = None
class pointsgen():
	def __init__(self):
		rospy.init_node('points_generator', anonymous=True)
		pub = rospy.Publisher('cubic_traj_params', cubic_traj_param, queue_size=10)
		
				
		global pos
		while not rospy.is_shutdown():	
			pos = cubic_traj_param()
		        pos.p0 = ra.uniform(10,-10)
        		pos.pf = ra.uniform(10,-10)
        	  	pos.v0 = ra.uniform(10,-10)
        	        pos.vf = ra.uniform(10,-10)
        	        pos.t0 = 0
        	        dt = ra.uniform(5,10)
        	        pos.tf =pos.t0+dt
	
			
        	        pub.publish(pos)
        		rospy.loginfo(pos)
			rate = rospy.Rate(0.05)  # Publish at 0.05hz or 20 times every second
        	        rate.sleep()


if  __name__ == "__main__" :
        try:
		ne = pointsgen()
        except rospy.ROSInterruptException: pass

