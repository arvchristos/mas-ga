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

# Inputs:
# N: number of auxiliary sources and collocation points
# a: Half length of the major axis
# b: Half length of the minor axis
# c_aux: Scaling of the auxiliary surface
# EP: Number of error points
# E_0: Amplitude of the incident wave
# psi: Angle of incidence
# k: Wavenumber
# c_obs: Observation points

N = 200
a = 1.0
gamma = 0.28 # Ask what gamma is
c_aux = 0.95
EP = 21
E_0 = 1
psi = 0
k = 1
c_obs = 1

n_proc = mp.cpu_count()

w = k/math.sqrt(constant.E*constant.M)
lamdaNum = 2*math.pi/k

# Circumference calculation


def x(x): return np.real(gamma*lamdaNum*(cmath.exp(np.complex(0,1)*x) + a*cmath.exp(np.complex(0,-2*x))))
def y(y): return np.imag(gamma*lamdaNum*(cmath.exp(np.complex(0,1)*y) + a*cmath.exp(np.complex(0,-2*y))))
def dx(t): return derivative(x, t, dx=1e-6)
def dy(t): return derivative(y, t, dx=1e-6)

def f(t): return math.sqrt(dx(t)**2 + dy(t)**2)


myfun2_re = quad(lambda t: np.real(f(t)), 0, 2*math.pi)[0]
myfun2_im = quad(lambda t: np.imag(f(t)), 0, 2*math.pi)[0]

c = quad(f, 0, 2*math.pi)

# Discretisation of the actual smooth triangle.

def sol_worker(index):
    def sol_func(phi): return quad(f, 0, phi)[0] - index*c[0]/N
    return fsolve(sol_func, [1])


pool = mp.Pool(processes=n_proc)
sol = np.array(pool.map(sol_worker, np.arange(0, N, 1/EP)))


def x_act_worker(index):
    return np.real(gamma*lamdaNum*(cmath.exp(1j*sol[index]) + a*cmath.exp(-2j*sol[index]) ))


def y_act_worker(index):
    return np.imag(gamma*lamdaNum*(cmath.exp(1j*sol[index]) + a*cmath.exp(-2j*sol[index]) ))


pool = mp.Pool(processes=n_proc)
x_act = np.array(pool.map(x_act_worker, np.arange(0, N*EP, 1)))

pool = mp.Pool(processes=n_proc)
y_act = np.array(pool.map(y_act_worker, np.arange(0, N*EP, 1)))


# Collocation points
x_obs = x_act*c_obs
y_obs = y_act*c_obs


# Dicretisation of the auxiliary surface.
#def sol_worker(index):
#    return sol[index*EP]

#sol_discrete = map(sol_worker, np.arange(0, N, 1))

#pool = mp.Pool(processes=n_proc)
#sol_discrete = np.array(pool.map(sol_worker, np.arange(0, N, 1)))


def x_aux_worker(index):
    return c_aux*x_act[index*EP]


def y_aux_worker(index):
    return c_aux*y_act[index*EP]

x_aux = np.array(list(map(x_aux_worker, np.arange(0, N, 1))))

y_aux = np.array(list(map(y_aux_worker, np.arange(0, N, 1))))


#pool = mp.Pool(processes=n_proc)
#x_aux = np.array(pool.map(x_aux_worker, np.arange(0, N, 1)))

#pool = mp.Pool(processes=n_proc)
#y_aux = np.array(pool.map(y_aux_worker, np.arange(0, N, 1)))


# Collocation points.
x_col = x_aux/c_aux
y_col = y_aux/c_aux


# Singularities
#s1 = math.sqrt(a**2-b**2)
#s2 = -s1

# Auxiliary currents

# Determination of equation 6

def B_worker(index):
    return -E_0*cmath.exp(-1j*k*x_col[index])

pool = mp.Pool(processes=n_proc)
B = np.array(pool.map(B_worker, np.arange(0, N, 1)))

paramlist = list(itertools.product(range(N), range(N)))


def A_worker(params):
    return special.hankel1(
        0, k*math.sqrt((x_aux[params[1]]-x_col[params[0]])**2 + (y_aux[params[1]]-y_col[params[0]])**2))


pool = mp.Pool(processes=n_proc)
res = np.array(pool.map(A_worker, paramlist))
A = res.reshape(N, N)


CN = np.linalg.cond(A)

print(CN)


I_aux = np.linalg.solve(A, B)


def Ez_inc_worker(index):
    return E_0*cmath.exp(-1j*k*x_obs[index])

pool = mp.Pool(processes=n_proc)
Ez_inc = np.array(pool.map(Ez_inc_worker, np.arange(0, N*EP, 1)))

# b_pl : distance between auxiliary filament l and collocation point p
Ez_scat = np.zeros(EP*N, dtype="complex_")

paramlist = list(itertools.product(np.arange(0, N*EP, 1), range(N)))


def Ez_scat_deserialized_worker(params):
    i = params[0]
    j = params[1]
    return I_aux[j]*special.hankel1(0, k*math.sqrt(
        (x_obs[i] - x_aux[j])**2 + (y_obs[i] - y_aux[j])**2))

# A_bessel : left hand side of eq22


pool = mp.Pool(processes=n_proc)
res = np.array(pool.map(Ez_scat_deserialized_worker, paramlist))
Ez_scat_deserialized = res.reshape(N*EP, N)


def Ez_scat_worker(param):
    return np.sum(Ez_scat_deserialized[param])


pool = mp.Pool(processes=n_proc)
Ez_scat = np.array(pool.map(Ez_scat_worker, range(N*EP)))

Ez_MAS = Ez_inc+Ez_scat

error = abs(Ez_MAS)/max(abs(Ez_inc))


plt.plot(2*math.pi*np.arange(0,N, 1/EP)/N, error, label = "ERROR")
plt.suptitle("ERROR")
plt.legend()
plt.show()

#plt.show()

plt.plot(np.arange(0,N, 1), np.imag(I_aux), label = "I_aux imag")
plt.suptitle("I_aux imag")
plt.legend()
plt.show()


plt.plot(np.arange(0,N, 1), np.real(I_aux), label = "I_aux real")
plt.suptitle("I_aux real")
plt.legend()
plt.show()

exit(0)
