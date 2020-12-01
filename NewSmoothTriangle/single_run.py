from SmoothTriangle import SmoothTriangle
import sys
import numpy as np
gamma = 0.05
N = 60 
c_aux = 0.9
k = 1
c_obs = 1

for it in np.linspace(0.001, 0.999 ,50): 
	schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=it, c_obs=c_obs)
	print(schema.mas(),it)

