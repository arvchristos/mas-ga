from Plane import Plane
import sys
import numpy as np
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["h","b","d","max_error","CN"]
#parameters
h = [0.25, 0.5, 0.75, 1, 1.5, 2, 3]
h2 = [2]
b = np.linspace(-2*h2[0],0,24)
d = np.linspace(0.05,1,19) 
y_obs = 0 

for h_val in h2:
	for b_val in b:
		for d_val in d:
			schema = Plane(k=1, h=h_val, b=b_val, d=d_val, y=y_obs)
			max_error, CN = schema.mas()
			if CN < 1000000000000:
				table.add_row([h_val,b_val,d_val,max_error,CN])

print(table)
"""
for it in np.linspace(0.1,1,20):
	schema = Plane(k=1, h=2, b=b, d=d, y=y_obs)
	max_error,CN = schema.mas()
	print("b=%s, d=%s, result is %s and CN=%s" % (b, it, max_error, CN))
"""
