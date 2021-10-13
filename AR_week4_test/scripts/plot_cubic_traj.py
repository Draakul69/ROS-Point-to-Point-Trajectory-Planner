#!/usr/bin/env python

import rospy
import numpy as np
from matplotlib import pyplot as plt
from std_msgs.msg import Float32
from AR_week4_test.srv import compute_cubic_traj
from AR_week4_test.msg import cubic_traj_param
from AR_week4_test.msg import cubic_traj_coeffs


coeffs = cubic_traj_coeffs()
a_prof = None
v_prof = None
p_prof = None
t=0
def plot_cubic(coeffs):
	global a_prof, v_prof, p_prof,t
	time0 = coeffs.t0
	timef = coeffs.tf
	
	while (t <=timef):	
		
		t = t + 0.1
		
		p_prof= (coeffs.a0 + (coeffs.a1*t) + (coeffs.a2*(t**2)) + (coeffs.a3*(t**3)))
	
		v_prof = (coeffs.a1 + (2*coeffs.a1*t) + (3*coeffs.a2*(t**2)))
	
		a_prof = (2*coeffs.a2) + (6*coeffs.a3*(t**3))
	
		rospy.loginfo(p_prof)
		rospy.loginfo(v_prof)
		rospy.loginfo(a_prof)

		rate=rospy.Rate(0.4) #Publish at every 2.5 seconds
       		pub3.publish(a_prof)
		pub2.publish(v_prof)
      		pub.publish(p_prof)
        	rate.sleep()




if __name__ == '__main__':
        try:

                rospy.init_node('plot_cubic_traj', anonymous=True)

		pub = rospy.Publisher("position_trajectory", Float32, queue_size=10)
		pub2 = rospy.Publisher("velocity_trajectory", Float32, queue_size=10)
		pub3 = rospy.Publisher("acceleration_trajectory", Float32, queue_size=10)
		sub = rospy.Subscriber("cubic_traj_coeffs", cubic_traj_coeffs, plot_cubic)

		rospy.spin()

	except rospy.ROSInterruptException:
		pass
