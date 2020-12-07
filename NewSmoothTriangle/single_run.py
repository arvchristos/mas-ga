from SmoothTriangle import SmoothTriangle
import sys
import numpy as np
gamma = 5
N = 96
c_aux = 0.921
k = 1
c_obs = 1

schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=c_aux, c_obs=c_obs)
print(schema.mas())

