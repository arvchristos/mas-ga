from define_function import calculate
import numpy as np
for i in np.linspace(0.00001,40.00041,40):
	print(i, calculate(i))