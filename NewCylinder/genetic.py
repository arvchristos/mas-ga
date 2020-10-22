import numpy as np
import random
from ga_algorithm import geneticalgorithm as ga
from Cylinder import Cylinder
import time
### Init parameters ###
r_c, r_s, = 0.8, 1.6
r_obs = r_c
limits=np.array([[0,1]]*1)


### defined functions ### 
def evaluation_function(value):
  schema = Cylinder(r_c= r_c, r_s=r_s, r_aux=value, r_obs=r_obs)
  return schema.mas()

def evaluation_function2(value):
  schema = Cylinder(r_c= r_c, r_s=r_s, r_aux=value, r_obs=r_obs)
  return schema.mas(champion=True)
def eval_mas(value):
  schema = Cylinder(r_c= r_c, r_s=r_s, r_aux=value, r_obs=1.5)
  return schema.mas(champion=True)

def eval(value):
	return value


rules={'max_num_iteration': 20,
	   'population_size':20,
       'mutation_probability':0.5,
	   'elit_ratio': 0.01,
	   'crossover_probability': 0.5,
	   'parents_portion': 0.1,
	   'crossover_type':'uniform',
	   'max_iteration_without_improv':None}	

model=ga(
		 function=evaluation_function,
		 dimension=1,
		 r_c = r_c,
		 variable_type='real',
		 variable_boundaries=limits,
		 algorithm_parameters=rules)


#run the GAlgorithm
time1 = time.time()
report, champion = model.run()
time_elasped = time.time() - time1

	
#print fetched data
print("\n time_elasped = ", time_elasped)
print("printing error convergence...")
for person in report:
	print(person)

mean, max_, _, CN = evaluation_function2(champion.get('variable'))
print("champion is ", champion.get('variable'))
print("with mean error = ", mean)
print("max error = ", max_)
print("and CN = ", CN)
_, _, ezmas, _ = eval_mas(champion.get('variable'))
print("and ez_MAS value", ezmas)

#time + max,mean error progress
#EZ_maz for champion	

#TO-DO 
#write and plot to a file
#
#


