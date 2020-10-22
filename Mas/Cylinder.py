import constant
import math
import numpy as np
from scipy import special
import cmath
import itertools
import multiprocessing as mp
import psutil

class Cylinder(object):
  """
  Cylinder smooth scatterer
  """
  def __init__(self, r_s=1, I=1, k=1, N=50, r_c=0.8, EP=21, r_aux=0.7, r_obs = 2, phi_s = 0):
    """
    """
    self.r_s = r_s
    self.I = I
    self.k = k
    self.N = N
    self.r_c = r_c
    self.EP = EP
    self.r_aux = r_aux
    self.r_obs = r_obs
    self.phi_s = phi_s

  def mas(self, verbose=False, both_flag=False ):
    """
    Execute MAS algorithm
    """

    discrete_range = range(-100, 101)

    n_proc = psutil.cpu_count(logical=False)

    ################
    # Verify input #
    ################

    # Calculate r_critical
    r_cri = math.pow(self.r_c,2)/self.r_s

    # If r_aux less than r_critical no need to execute
    if self.r_aux < r_cri:
      print('r_aux={:f} is less than r_cri={:f}'.format(self.r_aux,r_cri))
      exit()

    # Speed of light
    c = 1/math.sqrt(constant.E * constant.M)

    # Omega
    self.w = self.k*c

    ######################
    # Auxiliary Currents #
    ######################

    chunksize = self.N // n_proc

    # d_p :  distance between filament I and collocation point p

    pool = mp.Pool(processes=n_proc)

    self.d_p = pool.map(self.d_p_sqrt, range(self.N))

    #for i in range(len(d_p)):
    #  d_p[i] = math.sqrt(A-B*math.cos(C*i))

    if verbose:
      print("d_p:")
      print(self.d_p)

    # B_bessel : Right hand side of eq 22

    B_bessel = np.array(pool.map(self.B_bessel_worker, range(self.N)))
    #for i in range(len(B_bessel)):
    #  B_bessel[i] = -1*special.hankel1(0, k*d_p[i])

    if verbose:
      print("B_bessel:")
      print(B_bessel)

    # b_pl : distance between auxiliary filament l and collocation point p

    # b_pl[i][j] = sqrt(A - B*cos(C*(i-j)))

    paramlist = list(itertools.product(range(self.N),range(self.N)))

    res = np.array(pool.map(self.b_pl_worker, paramlist))
    self.b_pl = res.reshape(self.N, self.N)

    if verbose:
      print("b_pl")
      print(self.b_pl)

    # A_bessel : left hand side of eq22

    res = np.array(pool.map(self.A_bessel_worker, paramlist))
    A_bessel = res.reshape(self.N, self.N)

    if verbose:
      print("A_bessel")
      print(A_bessel)

    self.I_aux = np.linalg.solve(A_bessel,B_bessel)

    if verbose:
      print("I_aux")
      print(self.I_aux)


    ####################
    # Field quantities #
    ####################

    # r_obs_s[i] = sqrt(A - B*cos(C*i - phi_s)

    self.r_obs_s = pool.map(self.r_obs_s_worker, np.arange(0, self.N, 1/self.EP))

    if verbose:
      print("r_obs_s")
      print(self.r_obs_s)

    self.Ez_inc = np.array(pool.map(self.Ez_inc_worker, range(self.N*self.EP)))

    if verbose:
      print("Ez_inc")
      print(self.Ez_inc)

    # b_pl : distance between auxiliary filament l and collocation point p

    # b_pl[i][j] = sqrt(A - B*cos(C*(i-j)))

    # First create a N,N array to hold inner loop values to be added later on
    paramlist = list(itertools.product(np.arange(0, self.N, 1/self.EP),range(self.N)))

    # A_bessel : left hand side of eq22

    res = np.array(pool.map(self.Ez_scat_deserialized_worker, paramlist))
    self.Ez_scat_deserialized = res.reshape(self.N*self.EP, self.N)

    self.Ez_scat = np.array(pool.map(self.Ez_scat_worker, range(self.N*self.EP)))

    # A_bessel : left hand side of eq22

    if verbose:
      print("Ez_scat")
      print(self.Ez_scat)

    self.Ez_MAS = np.add(self.Ez_inc, self.Ez_scat)

    if verbose:
      print("Ez_MAS")
      print(self.Ez_MAS)

    self.K_r_c = self.k*self.r_c
    self.K_r_s = self.k*self.r_s

    # Ez_scat_true

    paramlist = list(itertools.product(np.arange(0,self.N, 1/self.EP),discrete_range))

    # A_bessel : left hand side of eq22

    res = np.array(pool.map(self.Ez_scat_true_deserialized_worker, paramlist))
    self.Ez_scat_true_deserialized = res.reshape(self.N*self.EP, len(discrete_range))

    self.Ez_scat_true = np.array(pool.map(self.Ez_scat_true_worker, range(self.N*self.EP)))

    if verbose:
      print("Ez_scat_true")
      print(self.Ez_scat_true)

    Ez_true = np.add(self.Ez_inc, self.Ez_scat_true)

    error = abs(np.subtract(Ez_true, self.Ez_MAS))/max(abs(self.Ez_inc))

    if verbose:
      print(error)

    pool.close()
    pool.join()

    if both_flag:
      return(np.mean(error),max(error))
    return max(error)


  # d_p[i] = sqrt(A-B*cos(C*i))
  def d_p_sqrt(self, N_index):
    A = math.pow(self.r_s,2) + math.pow(self.r_c,2)
    B = 2*self.r_s*self.r_c
    C = 2*math.pi/self.N

    return math.sqrt(A-B*math.cos(C*N_index))


  def B_bessel_worker(self, N_index):
    return -1*special.hankel1(0, self.k*self.d_p[N_index])


  def b_pl_worker(self, params):
    A = math.pow(self.r_aux,2) + math.pow(self.r_c,2)
    B = 2*self.r_aux*self.r_c
    C = 2*math.pi/self.N
    return math.sqrt(A-B*math.cos(C*(params[0]-params[1])))

  def A_bessel_worker(self, params):
    return special.hankel1(0, self.k*self.b_pl[params[0],params[1]])

  def r_obs_s_worker(self, parameter):
    A = math.pow(self.r_obs,2) + math.pow(self.r_s,2)
    B = 2*self.r_obs*self.r_s
    C = 2*math.pi/self.N
    return math.sqrt(A-B*math.cos(C*parameter - self.phi_s))

  def Ez_inc_worker(self, parameter):
    A = -((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))
    return A*special.hankel1(0,self.k*self.r_obs_s[parameter])

  def Ez_scat_deserialized_worker(self, params):
    A = math.pow(self.r_aux,2) + math.pow(self.r_obs,2)
    B = 2*self.r_aux*self.r_obs
    C = 2*math.pi/self.N
    D = -((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))

    rl_obs = math.sqrt(A-B*math.cos(C*(params[0]-params[1])))
    return D*self.I_aux[params[1]]*special.hankel1(0,self.k*rl_obs)


  def Ez_scat_worker(self, param):
    return np.sum(self.Ez_scat_deserialized[param])


  def Ez_scat_true_deserialized_worker(self, params):
    D = -((math.pow(self.k,2)*self.I)/(4*self.w*constant.E))
    E = 2*math.pi/self.N
    C = cmath.exp(complex(0,params[1]*params[0]*E))/special.hankel1(params[1],self.K_r_c)
    return -1*D*special.jv(params[1],self.K_r_c) * special.hankel1(params[1], self.K_r_s) * special.hankel1(params[1], self.k*self.r_obs)*C


  def Ez_scat_true_worker(self, param):
    return np.sum(self.Ez_scat_true_deserialized[param])
