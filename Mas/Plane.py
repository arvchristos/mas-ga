import constant
import math
import numpy as np
from scipy import special
import cmath

# Inputs:
# N
# k
# h
# I
# b
# d
# M
# EP
# y

N = 50
k = 1
h = 1
I = 1
b = -0.9
d = 0.2
M= 1000
EP = 21
y = 0

er = 1
mr = 1

h_aux = b*h
w = k/math.sqrt(constant.E*constant.M)

decim_indices = np.arange(-N*d,N*d + d, d)
######################
# Auxiliary Currents #
######################

Bn =  np.zeros(2*N+1, dtype="complex_" )
h2 = math.pow(h,2)

for i in range(0,2*N+1):
  Bn[i] = -I*special.hankel1(0, k*math.sqrt(math.pow(decim_indices[i], 2) + h2))

Anl = np.zeros((2*N+1, 2*N+1), dtype="complex_" )
h_aux2 = math.pow(h_aux,2)
for i in range(0,2*N+1):
  for j in range(0,2*N+1):
    Anl[i][j] = special.hankel1(0, k*math.sqrt( math.pow(decim_indices[i] - decim_indices[j],2) + h_aux2 ))

In = np.zeros(2*N+1)
In = np.linalg.solve(Anl,Bn)


####################
# Field quantities #
####################
decim_indices_M = np.arange((-M*d), M*d + d, d/EP)
Ez_inc =  np.zeros(2*M*EP+1, dtype="complex_" )
b = math.pow(y-h,2)
a = -((math.pow(k,2)*I)/(4*w*constant.E))

for i in range(0,2*M*EP+1):
  Ez_inc[i] = a*special.hankel1(0, k* math.sqrt(math.pow(decim_indices_M[i],2) + b  ) )



Ez_scat = np.zeros(2*M*EP+1, dtype="complex_" )
b = math.pow(y-h_aux,2)
a = -((math.pow(k,2)*I)/(4*w*constant.E))

for i in range(0,2*M*EP+1):
  for j in range(0,2*N+1):
    Ez_scat[i] = Ez_scat[i] + In[j]*special.hankel1(0, k* math.sqrt(math.pow(decim_indices_M[i] - decim_indices[j],2) + b  ))
  Ez_scat[i] = a * Ez_scat[i]

Ez_MAS = np.add(Ez_inc, Ez_scat)

Ez_image = np.zeros(2*M*EP+1, dtype="complex_" )
b = math.pow(y+h,2)
a = ((math.pow(k,2)*I)/(4*w*constant.E))
for i in range(0,2*M*EP+1):
  Ez_image[i] = a*special.hankel1(0, k*math.sqrt(math.pow(decim_indices_M[i],2) + b ))

Ez_true = np.add(Ez_inc, Ez_image)

print("Ez_Image")
print(Ez_image)

# Calculate errors
abs_diff = abs(np.subtract(Ez_true, Ez_MAS))
if y==0:
  error = abs_diff/max(abs(Ez_inc))
  print("error")
  print(error)
else:
  error1 = abs_diff/max(abs(Ez_inc))
  error2 = abs_diff/max(abs(Ez_true))
  print("error1")
  print(error1)
  print("error2")
  print(error2)
