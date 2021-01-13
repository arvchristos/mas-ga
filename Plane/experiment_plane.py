Experiment 5: Plane.

2A: We check the performance of our computational scheme on an open scatterer, in particular a PEC plane, having the external source radiate at various heights.

Thus, for every single experiment:
k = 1
I = 1
EP = 21
y = 0 for the GAs, y > 0 (e.g. 0.1h) for the field calculation (y is like c_obs!!)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
M = N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function')
    ~50.
DO NOT FORGET TO SET M = N, OTHERWISE OUR METRICS WILL NOT BE INDICATING (actually, this is what my (hopefully) third paper is about!)!!!

Dimensions:

h = 0.25 Your y_aux should be -0.25

h = 0.50 Your y_aux should be -0.50

h = 0.75 Your y_aux should be -0.75

h = 1.00 Your y_aux should be -1.00

h = 1.50 Your y_aux should be -1.50

h = 2.00 Your y_aux should be -2.00

h = 3.00 Your y_aux should be -3.00

You should check
1) if the error is good (and stable, see the CN)
2) If y_aux coincides with the y_cri I provided you above
3) the product k*d (we want it rather low, but not too low, then it gives huge CN).

You should observe
1) Perfect prediction of y_cri. Note that now we are expecting the pair (y_aux,d).

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.

_____________________________________________________________________________________________________

2B: We check the performance of our computational scheme on an open scatterer, in particular a PEC plane, having the external source radiate at various frequencies.

Thus, for every single experiment:
h= 1
EP = 21
I = 1
y = 0 for the GAs, y > 0 (e.g. 0.1h) for the field calculation (y is like c_obs!!)
Gen = your choice (the same for every experiment)
Pop = your choice (the same for every experiment)
M = N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)
    ~50.
DO NOT FORGET TO SET M = N, OTHERWISE OUR METRICS WILL NOT BE INDICATING (actually, this is what my (hopefully) third paper is about!)!!!


Then, the critical surface should be, for every single experiment, -1.00

Frequencies:
k = pi/20

k = pi/10

k = pi/5

k = pi/4

k = 1 (you have already done that)

k = pi/2

k = pi

You should check
1) if the error is good (and stable, see the CN)
2) If c_aux coincides with the y_cri I provided you above
3) the product k*d (we want it rather low, but not too low, then it gives huge CN).

You should observe
1) Perfect prediction of y_cri. Note that now we are expecting the pair (y_aux,d).

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.
_____________________________________________________________________________________________________

* There is a chance that you will not observe such thing: Fikioris claims that for the ellipse the critical surface is calculated exactly even for the dynamic (big dimensions, high frequency) case. We shall see.
If we cannot calculate the c_cri, run the following experiment, in order to understand what we are calculating.

-----------------------------------------------------------------------------------------------------

2C: You know the drill, this is the Gen/Pop test.
!!!!!!!!!DO IT ONLY IF YOU CANNOT PREDICT PERFECTLY THE Y_CRI!!!!!!!!!!!!!!


Thus, for every single experiment:
k = 1
h = 1
EP = 21
I = 1
y = 0 for the GAs, y > 0 (e.g. 0.1h) for the field calculation (y is like c_obs!!)
M = N = your choice (at I'd rather have the same N, but you can play should you encounter low errors; always check the CN and if you have doubts, draw the error function)
    ~50.
DO NOT FORGET TO SET M = N, OTHERWISE OUR METRICS WILL NOT BE INDICATING (actually, this is what my (hopefully) third paper is about!)!!!

Then, the critical surface should be, for every single experiment, -1

Gen/Pops

G*P = 1.0*x

G*P = 1.5*x

G*P = 2*x

G*P = 2.5*x

G*P = 3*x

G*P = 3.5*x

G*P = 4*x

x: your choice (that will be constant for all the experiment)

You must run two series of simulations: the first one you elect beforehand a Pop and increase Gen, so as to get the products above (x is you choice). In the second
one you elect a Gen and increase the Pop, so as to get the SAME products above 

You should check
1) if the error is good (and stable, see the CN)
2) If c_aux coincides with the c_cri I provided you above
3) The product k*d (we want it rather low, but not too low, then it gives huge CN).

You should observe
1) Perfect prediction of y_cri. Note that now we are expecting the pair (y_aux,d).

You should include in your output:
1) Every single parameter you have included in gen_pop_tests (the file on Github)
2) The evolution of the error per generation, you have forgotten them after the cylinders (the file on Github) tests.
_________________________________________________________________________________________________
