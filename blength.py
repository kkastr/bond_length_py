#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

file = open("output.xyz",'r')

coords = []

distance = []

crd = []

t = np.linspace(0,1,10001)

for line in file:
	if line.startswith('MD'): continue
	k = line.split( )
	coords.append(k)


j = 0


#gets rid of the '# of atoms' that dftb likes printing at every iteration
while j < len(coords):
	if j % 4.0 != 0:
		crd.append(coords[j])
	j+=1 



for i in range(0,len(crd),3):
	d = ((float(crd[i+1][1])-float(crd[i][1]))**2 + (float(crd[i+1][2]) - float(crd[i][2]))**2 + (float(crd[i+1][3]) - float(crd[i][3]))**2)**0.5	
	distance.append(d)
	#print(d)
	








plt.plot(t,distance)
plt.ylim([0,max(distance)])
plt.xlabel('Time (fs)')
plt.ylabel('Bond Length(Angstrom)') 
plt.show()

