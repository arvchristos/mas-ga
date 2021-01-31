from Plane import Plane
import sys
import numpy as np

#parameters
h = 1
k = 1
value = [-2,0.2]
y_obs = 0 
#change both flag_location
for it in np.linspace(-4,-0.5,50):
	schema = Plane(k=1, h=2, b=it, d=value[1], y=y_obs)
	print(it,schema.mas())

