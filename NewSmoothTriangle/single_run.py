from SmoothTriangle import SmoothTriangle
import sys

gamma = 0.05
N = 60 
c_aux = 0.9
k = 1
c_obs = 1

schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=c_aux, c_obs=c_obs)
print(schema.mas())

