import numpy as np
import random, time, math, pickle
from ga_algorithm import geneticalgorithm as ga
from Cylinder import Cylinder
import matplotlib.pyplot as plt
from numpy import savetxt
### Init parameters ###
r_c, r_obs = math.pi/15 , math.pi/15  # The same 
r_s = 1.6*r_c
N = 25


limits=np.array([[0,r_c]]*1)


### defined functions ### 
def evaluation_function(value):
  schema = Cylinder(N= N, r_c= r_c, r_s=r_s, r_aux=value, r_obs=r_obs)
  return schema.mas()

def evaluation_function2(value):
  schema = Cylinder(N = N, r_c= r_c, r_s=r_s, r_aux=value, r_obs=r_obs)
  return schema.mas(champion=True)
def eval_mas(value):
  schema = Cylinder(N= N, r_c= r_c, r_s=r_s, r_aux=value, r_obs=1.5*r_c)
  return schema.mas(champion=True)

def eval(value):
	return value


rules={'max_num_iteration': 35,
	   'population_size': 30,
       'mutation_probability': 0.85,
	   'elit_ratio': 0.01,
	   'crossover_probability': 0.1,
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

######################################################################
#run the GAlgorithm
time1 = time.time()
report, champion = model.run()
time_elasped = time.time() - time1

######################################################################	
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
#print("and ez_MAS value", ezmas)
######################################################################
### write data on a file ###
with open("cylinder%s.txt" %str(r_c)[0:5], "w") as fin:
	fin.write("Problem parameters:")
	fin.write("\nr_cylinder = %s " %r_c + "r_obs = %s " %r_obs + "r_s = %s" %r_s)
	fin.write("\nN = %s" %N)
	fin.write("\nResults:")
	fin.write("\nBest r_aux value was found to be %s " %champion.get('variable')+
			  "in %s minutes " %(time_elasped//60) +
			  "and %s seconds" %str(time_elasped%60)[0:4])
	fin.write("\n \n")
	fin.write("mean(error) = %s " %mean +"max(error) = %s " %max_ +
		      "CN = %s" %CN)
	fin.write("\nprinting the best r_aux per generation")
	for person in report:
		fin.write("\n"+"%s" %person)
	
### save file ###
savetxt("EZ_MAS%s.txt" %str(r_c)[0:5], ezmas, delimiter=',')

### to load ###
#f = open('store.pckl', 'rb')
#obj = pickle.load(f)
#f.close()
#######################################################################
### plot ###
plt.plot(report)
plt.xlabel('Generations')
plt.ylabel('Max Error')
plt.title('Error Convergence cylinder = %s' %(str(r_c)[0:5]))
plt.savefig('cylpi%s.png' % str(r_c)[0:5], dpi=400, bbox_inches='tight')
#plt.show()
#######################################################################
### run for different params


## rerun ez_maz for p/15 p/2 p :O ##
