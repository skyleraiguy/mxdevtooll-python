# excel link : https://blog.naver.com/montrix/221389851455

import sys, os
import mxdevtool as mx
import mxdevtool.xenarix as xen
import numpy as np

filename = './test_cir1f.npz'
ref_date = mx.Date.todaysDate()

def model():

	r0 = 0.02
	alpha = 0.1
	longterm = 0.042
	sigma = 0.03

	cir1f = xen.CIR1F('cir1f', r0, alpha, longterm, sigma)

	return cir1f

def test():
	print('cir1f test...', filename)

	m = model()
	timeGrid = mx.TimeEqualGrid(ref_date, 3, 365)

	# random 
	rsg = xen.Rsg(sampleNum=5000)
	results = xen.generate1d(m, None, timeGrid, rsg, filename, False)
	
	#print(results.multiPath(scenCount=10))

if __name__ == "__main__":
	
	test()
	#mx.npzee_view(filename)