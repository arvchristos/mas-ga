import numpy as np
import random, time, math, pickle
from ga_algorithm import geneticalgorithm as ga
from Cylinder import Cylinder
import matplotlib.pyplot as plt
from numpy import savetxt


r_c, r_obs = 10*math.pi, 10*math.pi  # The same 
r_s = 1.6*r_c
N = 100
r_aux = 16.40965522

limits=np.array([[0,r_c]]*1)

def eval_mas(value):
  schema = Cylinder(N= N, r_c= r_c, r_s=r_s, r_aux=value, r_obs=1.5*r_c)
  return schema.mas(champion=True)


_, _, ezmas, _ = eval_mas(r_aux)
savetxt("EZ_MAS%s.txt" %str(r_c)[0:5], ezmas, delimiter=',')	