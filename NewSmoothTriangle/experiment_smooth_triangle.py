Experiment 3: Smooth Trianglular Cylinder.

3A: We check the performance of our computational scheme on an bland triangular cylinder of various dimensions. Every other parameter
(including generations, population) remains constant.

Thus, for every single experiment:
k = 1
a = 0.2
E_0 = 1
EP = 21
psi = 0
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
N = 3*x+3 (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)
x = your choice.

Dimensions:

gamma = 0.05, Your c_aux should be around 0.921007874660096

gamma = 0.28, Your c_aux should be around 0.921007874660096

gamma = 0.4, Your c_aux should be around 0.921007874660096

gamma = 0.5, Your c_aux should be around 0.921007874660096

gamma = 0.7, Your c_aux should be around 0.921007874660096

gamma = 1, Your c_aux should be around 0.921007874660096

gamma = 2, Your c_aux should be around 0.921007874660096

gamma = 5, Your c_aux should be around 0.921007874660096

Note that the singularities (and thus the c_cri) depends solely only on the parameter a. Since we maintain a constant, we expect the same critical surface for all simulations (a is
a very powerful variable able to transifgure our triangle, so it is better to be left alone). 

You should check
1) if the error is good (and stable, see the CN; do not expect as good errors as in previous experiments, I think the triangle is more tricky, 
		         we are satisfied with max(error)~10^(-3))
2) If c_aux coincides with the c_cri I provided you above.

You should observe
1) Gradual divergence from c_cri, as we have shown in the first experiment (circular cylinder) with increasing dimensions*

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.

_____________________________________________________________________________________________________

3B: We check the performance of our computational scheme on an bland triangular cylinder for excitations of various frequencies. Every other parameter
(including generations, population) remains constant.

Thus, for every single experiment:
E_0 = 1
EP = 21
psi = 0
a = 0.2, gamma = 1
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
N = 3*x+3 (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)
x = your choice.
Then, the critical surface should be, for every single experiment, 

Frequencies:
k = 0.05

k = 0.28

k = 0.4

k = 0.5

k = 0.7

k  = 1 (you have already done that)

k = 2

k = 5

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

3C: We check the performance of our computational scheme on a bland triangular cylinder for different parameters of our GA. Every other parameter
(including generations, population) remains constant. We are conducting this experiment in order to verify whether the scheme fails to predict
the critical surface for high frequencies/big dimensions completely or it approaches when Gen/Pop -> infinity.

Thus, for every single experiment:
k = 1
E_0 = 1
EP = 21
psi = 0
a = 0.2, gamma = 1
c_obs = 1 for the GAs, c_obs > 1 for the calculation of Ez_MAS (final simulation)
N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)

Then, the critical surface should be, for every single experiment, 0.921007874660096

Gen/Pops

G*P = 1.0*y

G*P = 1.5*y

G*P = 2*y

G*P = 2.5*y

G*P = 3*y

G*P = 3.5*y

G*P = 4*y

y: your choice (that will be constant for all the experiment)

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
