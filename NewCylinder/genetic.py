import numpy as np
import random
from ga_algorithm import geneticalgorithm as ga
from Cylinder import Cylinder

r_c=0.800
limits=np.array([[0,1]]*1)


def evaluation_function(value):
  schema = Cylinder(r_aux = value)
  return schema.mas()

def eval(value):
	return value

rules={'max_num_iteration': 20,
	   'population_size':20,
       'mutation_probability':0.5,
	   'elit_ratio': 0.01,
	   'crossover_probability': 0.5,
	   'parents_portion': 0.2,
	   'crossover_type':'uniform',
	   'max_iteration_without_improv':None}	

### limits = r_c*r_c / r_s

model=ga(
	function=evaluation_function,
	dimension=1,
	r_c = r_c,
	variable_type='real',
	variable_boundaries=limits,
	algorithm_parameters=rules)


report = model.run()



"""
to do list:
1. image saved local instead of show
2. fix image titles and stuff
3. let it run on ubuntu big machine
4. get better logs 
"""