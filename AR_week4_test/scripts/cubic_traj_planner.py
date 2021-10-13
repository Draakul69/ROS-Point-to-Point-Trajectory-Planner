#!/usr/bin/env python

import rospy
import numpy as np
from AR_week4_test.srv import compute_cubic_traj
from AR_week4_test.msg import cubic_traj_param
from AR_week4_test.msg import cubic_traj_coeffs

pub_coeffs = cubic_traj_coeffs()
pub_param = cubic_traj_param()
x=cubic_traj_coeffs()
def Computecubics(pos):

		global pub_coeffs
		coeffs = cubic_traj_coeffs()
		pub_param = pos.p0, pos.pf, pos.v0, pos.vf, pos.t0, pos.tf
			
		m_list1 = coeffs
       		x = np.array(m_list1)


       		m_list2 = [[1,(pub_param[4]),(pub_param[4]**2),(pub_param[4]**3)],
               		[0, 1, (2*pub_param[4]), (3*pub_param[4]**2)],
               		[1, (pub_param[5]), (pub_param[5]**2), (pub_param[5]**3)],
               		[0, 1, (2*pub_param[5]), (3*pub_param[5]**2)]]
       		a = np.array(m_list2)
		
		m_list3 = [[pub_param[0]],
               	     	[pub_param[2]],
               	     	[pub_param[1]],
               	     	[pub_param[3]]]
       		b = np.array(m_list3)

       		inv_a = np.linalg.inv(a)

       		x = np.linalg.inv(a).dot(b)


		
		pub_coeffs.a0 = x[0]
		pub_coeffs.a1 = x[1]
		pub_coeffs.a2 = x[2]
		pub_coeffs.a3 = x[3]
		pub_coeffs.t0 = pub_param[4]
		pub_coeffs.tf = pub_param[5]
		rospy.loginfo(pub_coeffs)


if __name__ == '__main__':
	try:

		rospy.init_node('cubic_traj_listener', anonymous=True)

		
                rospy.wait_for_service('computing_cubics')

                rospy.ServiceProxy('computing_cubics', compute_cubic_traj)


                pub = rospy.Publisher("cubic_traj_coeffs", cubic_traj_coeffs, queue_size=10)
		sub = rospy.Subscriber("cubic_traj_params", cubic_traj_param, Computecubics, queue_size =10)

		while not rospy.is_shutdown():
			
					
			rate=rospy.Rate(0.05) #0.05Hz
			pub.publish(pub_coeffs)
			rate.sleep()
				
		


	except rospy.ROSInterruptException:
		pass

