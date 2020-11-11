import numpy as np
import random, time, math, pickle
from ga_algorithm import geneticalgorithm as ga
from Ellipse import Ellipse
import matplotlib.pyplot as plt
from numpy import savetxt
import sys
### Init parameters ###
pi = math.pi
ab = [(pi/10, pi/11),(0.9, 0.87), (2.1, 1.7), (4.3, 4), (2*pi, 1.8*pi), (2.4*pi, 1.94*pi), (6*pi, 4.4*pi)]
a,b = ab[int(sys.argv[1])]
critical = [0.416597790450531, 0.256038191595620, 0.587087047901807, 0.366970554373477, 0.435889894354067, 0.588725082039335, 0.679869268479038]	
k_arr = [pi/20, 0.45/pi, 2.1/(2*pi), 4.3/(2*pi), 1, 1.2, 3]
k = k_arr[int(sys.argv[2])]
N = int(sys.argv[3])
generations = 20 
population = 20
limits = np.array([[0,1]]*1)
c_obs = 1

### defined functions ### 
def evaluation_function(value):
  schema = Ellipse(N=N, a=a, b=b, k=k, c_aux=value, c_obs=c_obs)
  return schema.mas()

def evaluation_function2(value):
  schema = Ellipse(N=N, a=a, b=b, k=k, c_aux=value, c_obs=c_obs)
  return schema.mas(champion=True)
def eval_mas(value):
  schema = Ellipse(N=N, a=a, b=b, k=k, c_aux=value, c_obs=2*c_obs)
  return schema.mas(champion=True)

def eval(value):
	return value


rules={'max_num_iteration': generations,
	   'population_size': population,
       'mutation_probability': 0.85,
	   'elit_ratio': 0.01,
	   'crossover_probability': 0.1,
	   'parents_portion': 0.1,
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
with open("ellipse%s.txt" %(sys.argv[2]), "w") as fin:
	fin.write("Problem parameters:")
	fin.write("\n a = %s " %a + "b = %s " %b + "c_obs = %s" %c_obs)
	fin.write("\nN = %s " %N +"k = %s" %k)
	fin.write("\nGenerations = %s " %generations +"population = %s" %population)
	fin.write("\nResults:")
	fin.write("\nBest r_aux value was found to be %s " %champion.get('variable')+
			  "in %s minutes " %(time_elasped//60) +
			  "and %s seconds" %str(time_elasped%60)[0:4])
	fin.write("\n \n")
	fin.write("mean(error) = %s " %mean + "max(error) = %s " %max_ +
		      "CN = %s" %CN + " expected c_aux_critical value = %s" %str(critical[int(sys.argv[1])]))
	fin.write("\nprinting the best r_aux per generation")
	for person in report:
		fin.write("\n"+"%s" %person)
	
### save file ######################################################
savetxt("EZ_MAS%s.txt" %str(sys.argv[2]), ezmas, delimiter=',')

### to load ###
#f = open('store.pckl', 'rb')
#obj = pickle.load(f)
#f.close()
#######################################################################
### plot ###
"""
plt.plot(report)
plt.xlabel('Generations')
plt.ylabel('Max Error')
plt.title('Error Convergence cylinder = %s' %(str(r_c)[0:5]))
plt.savefig('cylpi%s.png' % str(r_c)[0:5], dpi=400, bbox_inches='tight')
#plt.show()
"""
#######################################################################

## R_CRI δίπλα στα ερρορς

##
##
