from Plane import Plane
import sys
import numpy as np

#parameters
h, k = 2.5, 1
d = 0.2
y_obs = 0 
#change both flag_location

for it in np.linspace(-4,-0.5,50):
	schema = Plane(k=1, h=2, b=it, d=d, y=y_obs)
	max_error,CN = schema.mas()
	print("b=%s, d=%s, result is %s and CN=%s" % (it, d, max_error, CN))
