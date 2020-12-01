import numpy as np
import random, time, math, pickle
from ga_algorithm import geneticalgorithm as ga
from SmoothTriangle import SmoothTriangle
import matplotlib.pyplot as plt
from numpy import savetxt
import sys
### Init parameters ###
pi = math.pi
###
gamma_array = [0.05, 0.28, 0.4, 0.5, 0.7, 1, 2, 5]
gamma = gamma_array[int(sys.argv[1])]
###
k_array = [0.05, 0.28, 0.4, 0.5, 0.7, 1, 2, 5]
k = k_array[int(sys.argv[2])]
###
critical_value = 0.921007874660096
###
generations = int(sys.argv[3])
population = int(sys.argv[4])
N =   int(sys.argv[5])
###
limits = np.array([[0,1]]*1)
c_obs = 1

### defined functions ### 
def evaluation_function(value):
  schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=value, c_obs=c_obs)
  return schema.mas()

def evaluation_function2(value):
  schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=value, c_obs=c_obs)
  return schema.mas(both_flag=True)

def eval_mas(value):
  schema = SmoothTriangle(N=N, gamma=gamma, k=k, c_aux=value, c_obs=2*c_obs)
  return schema.mas(both_flag=True)

def eval(value):
	return value


rules={'max_num_iteration': generations,
	   'population_size': population,
       'mutation_probability': 0.85,
	   'elit_ratio': 0.02,
	   'crossover_probability': 0.05,
	   'parents_portion': 0.2,
	   'crossover_type':'uniform',
	   'max_iteration_without_improv':None}	

model=ga(
		 function=evaluation_function,
		 dimension=1,
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
print(champion)
mean, max_, _, CN = evaluation_function2(champion.get('variable'))
print("champion is ", champion.get('variable'))
print("with mean error = ", mean)
print("max error = ", max_)
print("and CN = ", CN)
_, _, ezmas, _ = eval_mas(champion.get('variable'))
#print("and ez_MAS value", ezmas)
######################################################################
### write data on a file ###
with open("ellipse%s.txt" %(str(sys.argv[1])), "w") as fin:
	fin.write("Problem parameters:")
	fin.write("\n gamma = %s " %gamma + "c_obs = %s" %c_obs)
	fin.write("\nN = %s " %N +"k = %s" %k)
	fin.write("\nGenerations = %s " %generations +"population = %s" %population)
	fin.write("\nResults:")
	fin.write("\nBest r_aux value was found to be %s " %champion.get('variable')+
			  "in %s minutes " %(time_elasped//60) +
			  "and %s seconds" %str(time_elasped%60)[0:4])
	fin.write("\n \n")
	fin.write("mean(error) = %s " %mean + "max(error) = %s " %max_ +
		      "CN = %s" %CN + " expected c_aux_critical value = %s" %critical_value)
	fin.write("\nprinting the best r_aux per generation")
	for person in report:
		fin.write("\n"+"%s" %person)
	
### save file ######################################################
savetxt("EZ_MAS%s.txt" %(str(sys.argv[1])), ezmas, delimiter=',')

### to load ###
#f = open('store.pckl', 'rb')
#obj = pickle.load(f)
#f.close()
#######################################################################
### plot ###

plt.plot(report)
plt.xlabel('Generations')
plt.ylabel('Max Error')
plt.title('Error Convergence SmoothTriangle %s' %(str(sys.argv[1])))
plt.savefig('SmoothTriangleError%s.png' %(str(sys.argv[1])), dpi=400, bbox_inches='tight')
#plt.show()

#######################################################################

## 
##
##
