from SmoothTriangle import SmoothTriangle
import sys
import numpy as np
gamma = 1
N = 66
c_aux = 0.933
k = 1
c_obs = 1

schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=c_aux, c_obs=c_obs)
print(schema.mas())

