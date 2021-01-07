import constant
import math
import numpy as np
from scipy import special
import cmath
import multiprocessing as mp
import psutil
import itertools

##TO-DO : Return the mean/EZmas matrices when specific flag holds true

class Plane(object):
  """
  docstring
  """
  def __init__(self, N=50, k=1, h=1, I=1, b=-0.9, d=0.2, M=1000, EP=21, y=0, er=1,mr=1):
    """
    """
    self.N = N
    self.k = k
    self.h = h
    self.I = I
    self.b = b
    self.d = d
    self.M = M
    self.EP = EP
    self.y = y
    self.er = er
    self.mr = mr

  def mas(self, verbose=False):
    
    n_proc = psutil.cpu_count(logical=False)

    pool = mp.Pool(processes=n_proc)
    
    self.h_aux = self.b*self.h
    self.w = self.k/math.sqrt(constant.E*constant.M)

    self.decim_indices = np.arange(-self.N*self.d,self.N*self.d + self.d, self.d)
    ######################
    # Auxiliary Currents #
    ######################

    self.h2 = math.pow(self.h,2)
    self.Bn = np.array(pool.map(self.Bn_worker, range(0,2*self.N+1)))

    paramlist = list(itertools.product(range(2*self.N+1),range(2*self.N+1)))
    self.h_aux2 = math.pow(self.h_aux,2)

    res = np.array(pool.map(self.Anl_worker, paramlist))
    self.Anl = res.reshape(2*self.N+1, 2*self.N+1) 
    
    self.In = np.linalg.solve(self.Anl,self.Bn)

    ####################
    # Field quantities #
    ####################
    self.decim_indices_M = np.arange((-self.M*self.d), self.M*self.d + self.d, self.d/self.EP)
    self.b = math.pow(self.y-self.h,2)
    self.a = -((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))

    self.Ez_inc = np.array(pool.map(self.Ez_inc_worker, range(0,2*self.M*self.EP+1)))

    self.b = math.pow(self.y-self.h_aux,2)
    self.a = -((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))

    self.Ez_scat = np.array(pool.map(self.Ez_scat_worker, range(0,2*self.M*self.EP+1)))

    self.Ez_MAS = np.add(self.Ez_inc, self.Ez_scat)

    b = math.pow(self.y+self.h,2)
    a = ((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))

    self.Ez_image = np.array(pool.map(self.Ez_image_worker, range(0,2*self.M*self.EP+1)))

    self.Ez_true = np.add(self.Ez_inc, self.Ez_image)

    if verbose:
      print("Ez_Image")
      print(self.Ez_image)


    # Calculate errors
    abs_diff = abs(np.subtract(self.Ez_true, self.Ez_MAS))
    if self.y==0:
      error = abs_diff/max(abs(self.Ez_inc))
      print("error")
      print(error)
      return max(error)
    else:
      error1 = abs_diff/max(abs(self.Ez_inc))
      error2 = abs_diff/max(abs(self.Ez_true))
      print("error1")
      print(error1)
      print("error2")
      print(error2)

      return max(error1)

  def Bn_worker(self, N_index):
    return -self.I*special.hankel1(0, self.k*math.sqrt(math.pow(self.decim_indices[N_index], 2) + self.h2))

  def Anl_worker(self, params):
    return special.hankel1(0, self.k*math.sqrt( math.pow(self.decim_indices[params[0]] - self.decim_indices[params[1]],2) + self.h_aux2 ))

  def Ez_inc_worker(self, N_index):
    return self.a*special.hankel1(0, self.k * math.sqrt(math.pow(self.decim_indices_M[N_index],2) + self.b) )

  def Ez_scat_worker(self, N_index):
    tmp = 0
    for j in range(0,2*self.N+1):
        tmp = tmp + self.In[j]*special.hankel1(0, self.k* math.sqrt(math.pow(self.decim_indices_M[N_index] - self.decim_indices[j],2) + self.b  ))
    return self.a * tmp

  def Ez_image_worker(self, N_index):
    return self.a*special.hankel1(0, self.k*math.sqrt(math.pow(self.decim_indices_M[N_index],2) + self.b ))

  
