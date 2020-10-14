
from deap import base, creator,tools,algorithms
import random
from define_function import calculate
from helping_funcs import *

###toolbox function aliases
def create_toolbox(r_lower, r_upper):
  creator.create( "FitnessMin", base.Fitness , weights=(-1.0,))
  creator.create( "IndividualContainer", list , fitness= creator.FitnessMin)
  toolbox = base.Toolbox()
  #2 or 2
  toolbox.register( "InitialValue1",random.uniform, r_lower, r_upper)
  toolbox.register( "indiv", tools.initRepeat, creator.IndividualContainer, toolbox.InitialValue1, 1)
  #toolbox.register( "InitialValue2",random.randint, N_lower, N_upper)
  #toolbox.register( "indiv", tools.initCycle, creator.IndividualContainer, (toolbox.InitialValue1, toolbox.InitialValue2), n=1)
  toolbox.register( "population", tools.initRepeat, list , toolbox.indiv)
  toolbox.register( "evaluate", FuncEvaluation)
  toolbox.decorate( "evaluate", tools.DeltaPenalty (feasible,100, distance))

  ### examplar evolving functions
  toolbox.register("mate", tools.cxBlend,alpha=0.4)
  toolbox.register("mutate", tools.mutGaussian, mu = 0 ,sigma= 1,indpb=0.8)
  toolbox.register("select", tools.selTournament, tournsize = 5)
  return toolbox



### 3 ways of evolving algorithms (plain \\ m,l \\ m+l)
def ea_with_stats(population,cxpb,mutpb,ngen):
  pop = toolbox.population(population)
  hof = tools.HallOfFame(1)
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  #stats.register("avg", np.mean)
  stats.register("min", np.min)
  #stats.register("max", np.max)
  pop,logbook = algorithms.eaSimple(pop, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=stats, halloffame=hof,verbose=True)
  return pop, logbook, hof
def ea_m_plus_l_withstats(m,l,population,cxpb,mutpb,ngen):
  pop = toolbox.population(population)
  hof = tools.HallOfFame(1)
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  #stats.register("avg", np.mean)
  stats.register("min", np.min)
  #stats.register("max", np.max)
  pop,logbook = algorithms.eaMuPlusLambda(pop, toolbox,m,l, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=stats, halloffame=hof,verbose=True)
  return pop, logbook, hof  
def ea_m_comma_l_withstats(m,l,population,cxpb,mutpb,ngen):
  pop = toolbox.population(population)
  hof = tools.HallOfFame(1)
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  #stats.register("avg", np.mean)
  stats.register("min", np.min)
  #stats.register("max", np.max)
  pop,logbook = algorithms.eaMuCommaLambda(pop, toolbox,m,l, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=stats, halloffame=hof,verbose=True)
  return pop, logbook, ho

if __name__ == '__main__':
  print("this is toolbox functions")
