import matplotlib.pyplot as plt
import constant
import math
import numpy as np
from scipy import special
from scipy.integrate import quad
from scipy.misc import derivative
from scipy.optimize import fsolve
import itertools
import multiprocessing as mp
import cmath
import mpmath
import psutil


class SmoothTriangle(object):
  """
  Smooth Triangle scatterer
  """
  def __init__(self, N=50, a=0.2, gamma=0.05, c_aux=0.95, EP=21, E_0= 1, psi=0, k=1, c_obs=1):
    """
    """
    self.N = N
    self.a = a
    self.gamma = gamma
    self.c_aux = c_aux
    self.EP = EP
    self.E_0 = E_0
    self.psi = psi
    self.k = k  
    self.c_obs = c_obs

  def mas(self, verbose=False, both_flag=False):
    #n_proc = 1   
    n_proc = psutil.cpu_count(logical=True)
    
    self.w = self.k/math.sqrt(constant.E*constant.M)
    self.lamdaNum = 2*math.pi/self.k

    # Circumference calculation

    def x(x): return np.real(self.gamma*self.lamdaNum*(cmath.exp(np.complex(0,1)*x) + self.a*cmath.exp(np.complex(0,-2*x))))
    def y(y): return np.imag(self.gamma*self.lamdaNum*(cmath.exp(np.complex(0,1)*y) + self.a*cmath.exp(np.complex(0,-2*y))))
    def dx(t): return derivative(x, t, dx=1e-6)
    def dy(t): return derivative(y, t, dx=1e-6)

    def f(t): return math.sqrt(dx(t)**2 + dy(t)**2)

    self.c = quad(f, 0, 2*math.pi)

    # print(c)

    # Discretisation of the actual smooth triangle.

    pool = mp.Pool(processes=n_proc)
    
    self.sol = np.array(pool.map(self.sol_worker, np.arange(0, self.N, 1/self.EP)))

    self.x_act = np.array(pool.map(self.x_act_worker, np.arange(0, self.N*self.EP, 1)))

    self.y_act = np.array(pool.map(self.y_act_worker, np.arange(0, self.N*self.EP, 1)))

    # Collocation points
    self.x_obs = self.x_act*self.c_obs
    self.y_obs = self.y_act*self.c_obs

    # Dicretisation of the auxiliary surface.

    self.x_aux = np.array(list(map(self.x_aux_worker, np.arange(0, self.N, 1))))

    self.y_aux = np.array(list(map(self.y_aux_worker, np.arange(0, self.N, 1))))


    # Collocation points.
    self.x_col = self.x_aux/self.c_aux
    self.y_col = self.y_aux/self.c_aux


    # Auxiliary currents

    # Determination of equation 6
    B = np.array(pool.map(self.B_worker, np.arange(0, self.N, 1)))

    paramlist = list(itertools.product(range(self.N),range(self.N)))

    res = np.array(pool.map(self.A_worker, paramlist))
    
    A = res.reshape(self.N, self.N)

    CN = np.linalg.cond(A)
    if verbose:
      print(CN)

    self.I_aux = np.linalg.solve(A, B)

    Ez_inc = np.array(pool.map(self.Ez_inc_worker, np.arange(0, self.N*self.EP, 1)))

    # b_pl : distance between auxiliary filament l and collocation point p
    Ez_scat = np.zeros(self.EP*self.N, dtype="complex_")

    paramlist = list(itertools.product(np.arange(0,self.N*self.EP, 1),range(self.N)))

    # A_bessel : left hand side of eq22
    res = np.array(pool.map(self.Ez_scat_deserialized_worker, paramlist))
    self.Ez_scat_deserialized = res.reshape(self.N*self.EP, self.N)

    Ez_scat = np.array(pool.map(self.Ez_scat_worker, range(self.N*self.EP)))

    Ez_MAS = np.add(Ez_inc, Ez_scat)

    error = abs(Ez_MAS)/max(abs(Ez_inc))

    if verbose:
        print(max(abs(Ez_inc)))

      #print(error)

    pool.close()
    pool.join()

    if both_flag:

      return(np.mean(error),max(error), Ez_MAS, CN)
    return(max(error))

    #plt.plot(2*math.pi*np.arange(0,N, 1/EP)/N, error, label = "ERROR")
    # plt.suptitle("ERROR")
    # plt.legend()
    # plt.show()

    # plt.show()



  def f(self, t):
    def x(x): return np.real(self.gamma*self.lamdaNum*(cmath.exp(np.complex(0,1)*x) + self.a*cmath.exp(np.complex(0,-2*x))))
    def y(y): return np.imag(self.gamma*self.lamdaNum*(cmath.exp(np.complex(0,1)*y) + self.a*cmath.exp(np.complex(0,-2*y))))
    def dx(t): return derivative(x, t, dx=1e-6)
    def dy(t): return derivative(y, t, dx=1e-6)

    def f(t): return math.sqrt(dx(t)**2 + dy(t)**2)

    return math.sqrt(dx(t)**2 + dy(t)**2)


  def sol_worker(self, index):
    def sol_func(phi): return quad(self.f, 0, phi)[0] - index*self.c[0]/self.N
    return fsolve(sol_func, [1])

  def x_act_worker(self, index):
    return np.real(self.gamma*self.lamdaNum*(cmath.exp(1j*self.sol[index]) + self.a*cmath.exp(-2j*self.sol[index]) ))

  def y_act_worker(self, index):
    return np.imag(self.gamma*self.lamdaNum*(cmath.exp(1j*self.sol[index]) + self.a*cmath.exp(-2j*self.sol[index]) ))

  def x_aux_worker(self, index):
    return self.c_aux*self.x_act[index*self.EP]

  def y_aux_worker(self, index):
    return self.c_aux*self.y_act[index*self.EP]

  def B_worker(self, index):
    return -self.E_0*cmath.exp(np.complex(0, -1*self.k*self.x_col[index]))

  def A_worker(self, params):
    return special.hankel1(
              0, self.k*math.sqrt((self.x_aux[params[1]]-self.x_col[params[0]])**2 + (self.y_aux[params[1]]-self.y_col[params[0]])**2))

  def Ez_inc_worker(self, index):
    return self.E_0*cmath.exp(np.complex(0, -1*self.k*self.x_obs[index]))

  def Ez_scat_deserialized_worker(self, params):
    i = params[0]
    j = params[1]
    return self.I_aux[j]*special.hankel1(0, self.k*math.sqrt(
              (self.x_obs[i] - self.x_aux[j])**2 + (self.y_obs[i] - self.y_aux[j])**2))

  def Ez_scat_worker(self, param):
    return np.sum(self.Ez_scat_deserialized[param])
