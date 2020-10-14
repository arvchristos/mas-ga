
import numpy as np
import warnings, time ,datetime, math, cmath, random
from math import *
from cmath import *
from scipy import special
from deap import base, creator,tools,algorithms
from math import *
import warnings , time, datetime, math, cmath, random
from scipy import special
from prettytable import PrettyTable
from define_function import calculate
from helping_funcs import *
from toolbox_functions import *
import matplotlib.pyplot as plt

#warnings.filterwarnings("ignore")
if __name__ == '__main__':
	"""
	### PROBLEM PARAMETERS###
	divisor = 2
	r_cylinder = math.pi / divisor
	r_s = (3/2)* r_cylinder
	N = 50
	r_critical = math.pow(r_cylinder,2)/r_s
	r_lower, r_upper, N_lower, N_upper = r_critical, r_cylinder, 1, 50
	numVariables = 1
	"""
	toolbox  = create_toolbox(r_lower, r_upper)

	final_data = []
	ngen = 4
	for N in range(25,26,4):
	  def FuncEvaluation(indiv):
	  ##r_aux,N,r_c,r_obs,r_s,EP,k
	    Calc = calculate(indiv[0])
	    return (Calc,) 
	  #init_values
	  goal, error, iterations  = 0.0, 1e-7, 1
	  ngen_arr, time_arr, hof_arr, min_val_arr, first_best_arr = [],[],[],[],[]
	  logs = []
	  ###Total run
	  #for j in range(iterations):
	  start = time.time()
	  log_arr = []
	  #THREE STEP TOTAL SCALING MUTATION
	  population = 20
	  m, l = population//2 , population
	  cxpb ,mutpb = 0.15, 0.85
	  #ngen = ngen + 1  #that will be tripled
	  diff = r_upper - r_lower
	  print(diff,"diff")
	  
	  ### Specify the mutations. GA will be applied for every $N: $len(gauss_sigma) times. Every time: $population evolves $ngen
	  #gauss_sigma=[diff/10,diff/100,diff/500,diff/1000,diff/5000,diff/10000]
	  gauss_sigma=[diff/10,diff/100,diff/500]
	  		  

	  pop = toolbox.population(population)
	  
	  for i in range(len(gauss_sigma)):
	    toolbox.register("mutate", tools.mutGaussian, mu = 0 ,sigma = gauss_sigma[i],indpb=0.99)
	    hof = tools.HallOfFame(1)
	    stats = tools.Statistics(lambda ind: ind.fitness.values)
	    stats.register("min", np.min)
	    pop,logbook = algorithms.eaMuPlusLambda(pop, toolbox,m,l, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=stats, halloffame=hof,verbose=True)
	    log_arr.append(logbook)
	    ngen_arr.append(ngen*(i+1))
	    time_arr.append(time.time()-start)
	    hof_arr.append(hof)
	    print("hof is ", hof)
	    logs.append(log_arr)
	    min_val_arr.append(FindMinInLogbook(logbook))
	    first_best_arr.append(FindFirstGoodinLogbook(logbook,goal,error))
	    #Minimum_value = FindMinInLogbook(logbook)
	    #First_best = FindFirstGoodinLogbook(logbook,goal,error)
	    
	    
	    
	    


	  table=PrettyTable()
	  table.field_names=["number of gens","pop","time elasped (s)","Best Gene","Minimum Max Abs Error","First suited Gene value"]
	  for i in range(len(gauss_sigma)):
	    table.add_row([ngen_arr[i], population, str(datetime.timedelta(seconds=floor(time_arr[i]))), hof_arr[i], min_val_arr[i][1], first_best_arr[i][1]])

	  table.sortby = "number of gens"
	  
	  final_data.append([[str(datetime.timedelta(seconds=floor(time_arr[len(gauss_sigma)-1])))],hof_arr[len(gauss_sigma)-1][0],min_val_arr[len(gauss_sigma)-1][1],N])
	  
	  print(table)
	  print("-------------------------------")
	  print("N = ",N)


	### PLOT ###  
	#(str(time_arr[i]//60)+"minutes"+str((time_arr[i]% 60)[0:2]+"sec"))
	#shapes data removes duplicates by multiple generations
	champs = [log_arr[iter][gen].get('min') for iter in range(len(log_arr)) for gen in range(len(log_arr[0]))]
	b = [x for x in range(ngen + 1,ngen*len(gauss_sigma)+1,ngen)] # indexes to delete
	for item in range(len(b)): # because i, delete i reduce 
	  del champs[b[item] - item]
	#a =  [(a[item],item) for item in range(len(a)) ]
	print("plot is omitted for now")
	# plot, then save plot, save data in txt file 
	"""
	import matplotlib.pyplot as plt
	plt.plot(champs)
	plt.ylabel('max error')
	plt.xlabel('number of generations')
	plt.title('N = %i ' % N)
	plt.savefig('cylpi%s.png' % str(divisor), dpi=400, bbox_inches='tight')
	plt.show()

	with open('cylpi%s.txt' % str(divisor), 'w') as f:
	  f.write("r_cylinder=%s" %str(r_cylinder)+'\n')
	  f.write("N=%s" %N+'\n')
	  f.write("time elasped = %s" %str(datetime.timedelta(seconds=floor(time_arr[len(gauss_sigma)-1])))+'\n')
	  f.write("best r_aux value = %s" %str(hof_arr[len(gauss_sigma)-1][0]) + '\n')
	  f.write('max error values:\n')
	  for item in champs:
	    f.write(str(item)+',')
	  
	#15,25....
	"""
