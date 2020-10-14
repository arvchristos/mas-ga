###Initial Values for mas(r_aux,N,r_cylinder,r_obs,r_s,EP,k) = mas(r_aux,N,r_cylinder = 0.8, r_obs = 0.8, r_s = 1, EP = 21, k = 1 )
import math
from define_function import calculate
import numpy as np
#MIN_BOUNDS = np.array([r_lower, N_lower])
#MAX_BOUNDS = np.array([r_upper, N_upper])
#delta = np.array([(r_upper+r_lower)/2, (N_lower+N_upper)//2]) #value to return to, if out of bounds
###Returns random initial values for r,N. This will be calculated for each individual at the beginning
### PROBLEM PARAMETERS###

r_lower, r_upper =-20, 20


#Examine whether values are out of bounds
def feasible(indiv):
  #print(indiv)
  #if ((indiv[0] < r_lower or indiv[0] > r_upper) or (indiv[1] < N_lower or indiv[1] > N_upper)):
  if (indiv[0] < r_lower or indiv[0] > r_upper):
    #print("false")
    return False
  #print("true")
  return True
###
def distance( indiv ) :
    dist = 0.0
    for i in range (len( indiv )) :
        penalty = 0
        if ( indiv [i] < r_lower) : penalty = r_lower - indiv [i]
        if ( indiv [i] > r_upper) : penalty = r_upper - indiv [i]
        dist = dist + penalty
    return dist
###

### log purposes
def FindMinInLogbook(logbook):
  return np.argmin(logbook.select("min")),min(logbook.select("min"))
###

### log purposes
def FindFirstGoodinLogbook(logbook,goal,delta):
  work=logbook.select("min")
  return  next(a for a in enumerate(work) if a[0] <=goal+delta)
###
### log purposes
def TotalEvalsTillGood(logbook,goal,delta):
  index=FindFirstGoodinLogbook(logbook,goal,delta)
  return sum(logbook.select("nevals")[:index[0]+1])
###

##testing function
def FuncEvaluation2(indiv):
  return (indiv[0]-0.64,)
def FuncEvaluation(indiv):
  ##r_aux,N,r_c,r_obs,r_s,EP,k
  Calc = calculate(indiv[0])
  return (Calc,) 
  