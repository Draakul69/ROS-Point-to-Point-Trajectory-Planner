#!/usr/bin/env python

from __future__ import print_function
from AR_week4_test.srv import compute_cubic_traj,compute_cubic_trajResponse
from AR_week4_test.msg import cubic_traj_param
import rospy
import numpy as np

def compute_traj(req):
	print("Returning Cubic Coeffs")
	return cubic_traj_param(req)
	return compute_cubic_trajResponse
def compute_cubic_service():
	rospy.init_node('compute_cubics')
	s = rospy.Service('computing_cubics', compute_cubic_traj, compute_traj)
	print("Ready to convert to cubic coeffs")
	rospy.spin()

if __name__ == "__main__" :
		try:
 			compute_cubic_service()
		except rospy.ROSInterruptException:
			pass


