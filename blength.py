#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

file = open("output.xyz",'r')

distance = []

crd = []

step = []


for line in file:
	#if line.startswith('MD'): md_iter.append(line)
	k = line.split( )
	crd.append(k)

file.close()



for i in range(0,len(crd),5):
	H = np.array([ float(crd[i+3][1]), float(crd[i+3][2]), float(crd[i+3][3]) ])
	O = np.array([ float(crd[i+2][1]), float(crd[i+2][2]), float(crd[i+2][3]) ])
	vector_sub = H - O
	
	d = np.linalg.norm(vector_sub)
	l = ((float(crd[i+3][1])-float(crd[i+2][1]))**2 + (float(crd[i+3][2]) - float(crd[i+2][2]))**2 + (float(crd[i+3][3]) - float(crd[i+2][3]))**2)**0.5
	
	step.append(crd[i+1][2])
	
	print(l)
	print(d)
	print(abs(l-d))
	distance.append(l)




plt.plot(step,distance)
plt.ylim([0,1.5])
plt.xlim([0,2000])
plt.xlabel('Time (fs)')
plt.ylabel('Bond Length(Angstrom)') 
plt.show()
