Experiment 2: Elliptical Cylinder.

2A: We check the performance of our computational scheme on an elliptical cylinder of various dimensions. Every other parameter
(including generations, population) remains constant.

Thus, for every single experiment:
k = 1
E_0 = 1
EP = 21
psi = 0
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)

Dimensions:

a = pi/10, b = pi/11, a/b = 1.1 (<sqrt(2)) Your c_aux should be around 0.416597790450531

a = 0.9, b = 0.87, a/b = 1.03 (<sqrt(2)) Your c_aux should be around 0.256038191595620

a = 2.1, b = 1.7, a/b = 1.24 (<sqrt(2)) Your c_aux should be around 0.587087047901807

a = 4.3, b = 4, a/b = 1.08 (<sqrt(2)) Your c_aux should be around 0.366970554373477

a = 2*pi, b = 1.8*pi, a/b = 1.11 (<sqrt(2)) Your c_aux should be around 0.435889894354067

a = 2.4*pi, b = 1.94*pi, a/b = 1.24 (<sqrt(2)) Your c_aux should be around 0.588725082039335

a = 6*pi, b = 4.4*pi, a/b = 1.36 (<sqrt(2)) Your c_aux should be around 0.679869268479038

You should check
1) if the error is good (and stable, see the CN)
2) If c_aux coincides with the c_cri I provided you above

You should observe
1) Gradual divergence from c_cri, as we have shown in the first experiment (circular cylinder) with increasing dimensions*

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.

_____________________________________________________________________________________________________

2B: We check the performance of our computational scheme on an elliptical cylinder for excitations of various frequencies. Every other parameter
(including generations, population) remains constant.

Thus, for every single experiment:
E_0 = 1
EP = 21
psi = 0
a = 2*pi, b = 1.8*pi
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)

Then, the critical surface should be, for every single experiment, 0.435889894354067

Frequencies:
k = pi/20

k = 0.45/pi

k = 2.1/(2*pi)

k = 4.3/(2*pi)

k  = 1 (you have already done that)

k = 1.2

k = 3

You should check
1) if the error is good (and stable, see the CN)
2) If c_aux coincides with the c_cri I provided you above

You should observe
1) Gradual divergence from c_cri, as we have shown in the first experiment (circular cylinder) with increasing frequency*

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.
_____________________________________________________________________________________________________

* There is a chance that you will not observe such thing: Fikioris claims that for the ellipse the critical surface is calculated exactly even for the dynamic (big dimensions, high frequency) case. We shall see.
If we cannot calculate the c_cri, run the following experiment, in order to understand what we are calculating.

-----------------------------------------------------------------------------------------------------

2C: We check the performance of our computational scheme on an elliptical cylinder for different parameters of our GA. Every other parameter
(including generations, population) remains constant. We are conducting this experiment in order to verify whether the scheme fails to predict
the critical surface for high frequencies/big dimensions completely or it approaches when Gen/Pop -> infinity.

Thus, for every single experiment:
k = 1
E_0 = 1
EP = 21
psi = 0
a = 2*pi, b = 1.8*pi
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)

Then, the critical surface should be, for every single experiment, 0.435889894354067

Gen/Pops

G*P = 1.0*x

G*P = 1.5*x

G*P = 2*x

G*P = 2.5*x

G*P = 3*x

G*P = 3.5*x

G*P = 4*x

x: your choice (that will be constant for all the experiment)

You mus run two series of simulations: the first one you elect beforehand a Pop and increase Gen, so as to get the products above (x is you choice). In the second
one you elect a Gen and increase the Pop, so as to get the SAME products above 

You should check
1) if the error is good (and stable, see the CN)
2) If c_aux coincides with the c_cri I provided you above

You should observe
1) I do not know! Maybe better approximation of the c_cri, but, as we have seen in the first experiment, this may just mean a better approximation of a different c_aux (closer to the c_cri, but surely not the c_cri)

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.
_________________________________________________________________________________________________
