import numpy as np
import random, time, math, pickle
from ga_algorithm import geneticalgorithm as ga
from Plane import Plane
import matplotlib.pyplot as plt
from numpy import savetxt
import sys

## fix output to be two 2 vars fitted (wirting output etc.)
## fix the 2 values Plane.py gets
### Init parameters ###
pi = math.pi
###
h_array = [0.25, 0.5, 0.75, 1, 1.5, 2.0, 3.0]
h = h_array[int(sys.argv[1])]
###
k_array = [pi/20, pi/10, pi/5, pi/4, 1, pi/2, pi]
k = k_array[int(sys.argv[2])]
###
#critical_value = 0.921007874660096
###
generations = int(sys.argv[3])
population = int(sys.argv[4])
N = int(sys.argv[5])
###
limits = np.array([[-5,0],[0,1]]) ### needs change on the -2 when h is even smaller.
### b ---> negative number should converge to -1 (-2,0)
### d ---> should be small (0,1)

y_obs = 0
y_obs_mas = 0.1*h

### defined functions ### 
def evaluation_function(value):
  schema = Plane(N=N, h=h, k=k, M=N, b=value[0], d=value[1], y=y_obs)
  return schema.mas()

def evaluation_function2(value):
  schema = Plane(N=N, h=h, k=k, M=N, b=value[0], d=value[1], y=y_obs)
  return schema.mas(both_flag=True)

def eval_mas(value):
  schema = Plane(N=N, h=h, k=k, M=N, b=value[0], d=value[1], y=y_obs)
  return schema.mas(both_flag=True)

def eval(value):
	return (value[0]-value[1])


rules={'max_num_iteration': generations,
	   'population_size': population,
       'mutation_probability': 0.85,
	   'elit_ratio': 0.1,
	   'crossover_probability': 0.001,
	   'parents_portion': 0.3,
	   'crossover_type':'uniform',
	   'max_iteration_without_improv':None}	

model=ga(
		 function=evaluation_function,
		 dimension=2,
		 variable_type=np.array([['real']]),
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

Best_pair = champion.get('variable')
print(Best_pair,type(Best_pair))

mean, max_, _, CN = evaluation_function2(Best_pair)
print("champion is ", champion.get('variable'))
print("with mean error = ", mean)
print("max error = ", max_)
print("and CN = ", CN)
#ezmas = [1,1]
_, _, ezmas, _ = eval_mas(Best_pair)
print("and ez_MAS value", ezmas)
######################################################################
### write data on a file ###
with open("Plane%s_%s_%s_%s_%s.txt" %(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5])) , "w") as fin:
	fin.write("Problem parameters:")
	fin.write("\n h = %s " %h + "y_obs = %s" %y_obs)
	fin.write("\nN = %s " %N +"k = %s" %k)
	fin.write("\nGenerations = %s " %generations +"population = %s" %population)
	fin.write("\nResults:")
	fin.write("\nBest r_aux value was found to be %s " %champion.get('variable')+
			  "in %s minutes " %(time_elasped//60) +
			  "and %s seconds" %str(time_elasped%60)[0:4])
	fin.write("\n \n")
	fin.write("mean(error) = %s " %mean + "max(error) = %s " %max_ +
		      "CN = %s" %CN + " expected positive critical value = %s" %h)
	fin.write("\nprinting the best r_aux per generation")
	for person in report:
		fin.write("\n"+"%s" %person)
	
### save file ######################################################
savetxt("EZ_MAS%s_%s_%s_%s_%s.txt" %(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5])), ezmas, delimiter=',')


#######################################################################
### plot ###

plt.plot(report)
plt.xlabel('Generations')
plt.ylabel('Max Error')
plt.title('Error Convergence SmoothTriangle %s' %(str(sys.argv[1])))
plt.savefig('PlaneError%s_%s_%s_%s_%s.png' %(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5])), dpi=400, bbox_inches='tight')
#plt.show()

#######################################################################

## 
##
##
