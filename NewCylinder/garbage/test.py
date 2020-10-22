import numpy as np
import random
from geneticalgorithm import geneticalgorithm as ga

def evaluation_function(chrom):
	return (chrom)

def pop_init(pop_size, limits):
	"""
	Initialize pop_size chromosomes with 
	genes=1! each one. Values are determined
	By uniform distribution within the limits
	"""
	population = np.random.uniform(
		limits[0], limits[1], size=pop_size)
	return population.tolist()

def apply_crossover(c_prob, beta, p1, p2):
	"""
	applies crossover to p1,p2
	produces offsprings c1,c2
	"""
	c1 = p1 
	c2 = p2
	if (random.uniform(0, 1) < c_prob):
		c1 = c1 - beta*(p1 - p2)
		c2 = c2 - beta*(p2 - p1)
	return (c1, c2)

def apply_mutation(m_prob, p1, mu, sigma):
	"""
	applies mutation on p1 
	with mu mean and sigma
	"""
	if (random.uniform(0, 1) < m_prob):
		p1 = p1 + np.random.normal(mu,sigma)
	return (p1)

def evaluate(population):
	evaluated_pop = [(chrom, evaluation_function(chrom)) for chrom in population]
	return evaluated_pop



#def tour_selection(evaluated_pop, out_of):

rules={'max_num_iteration': 1000,
	   'population_size':100,
       'mutation_probability':0.1,
	   'elit_ratio': 0.01,
	   'crossover_probability': 0.5,
	   'parents_portion': 0.3,
	   'crossover_type':'uniform',
	   'max_iteration_without_improv':None}	


limits=np.array([[0,1]]*1)

model=ga(
	function=evaluation_function,
	dimension=1,
	variable_type='real',
	variable_boundaries=limits,
	algorithm_parameters=rules)
print(model.param)
model.run()
