from random import random
from math import sin, pi, log

# Exercise 3
#
# Estimate the area of a circle of radius 1/2
# with center at (1/2,1/2) inside the unit
# square by choosing 1000 points at random.
# Compare your results with the true value of
# pi/4. Use your results to estimate pi.


# Exercise 4
#
# Estimate area under the graph of y = sin(pi x)
# inside the unit square by choosing 10K points
# at random. Estimate pi.

# Exercise 5
#
# Estimate the area under the graph of
# y = 1/(x+1) in the unit square in the same
# way as E4. Calculate the true value of this
# area and use the simulation to estimate the
# value of log 2.

in_the_circle = lambda x,y: (x - .5)**2 + (y - .5)**2 <= .25 # circle of radius 1/2.
under_the_sine = lambda x,y: y < sin(pi * x) # graph of sin(pi*x)
under_the_inverse = lambda x,y: y < 1.0 / (x + 1.0) # inverse f'n.

def simulate(condition, num_of_trials):
    '''
    Given a condition and the number of trials,
    randomly selects points within the unit
    square and counts how many of them satsify
    the condition.

    Returns the count.
    '''
    counter = 0
    for i in range(num_of_trials):
        x = random()
        y = random()
        if condition(x,y):
            counter += 1

    return float(counter)


if __name__ == '__main__':

    n = 1000
    print('\nFinding pi with a circle of r=.5 (' + str(n) + ' random points):')
    print('pi estimate = ', 4.0 * simulate(in_the_circle, n)/ float(n))
    print('pi actual   = ', pi)

    n = 10000
    print('\nFinding pi with y = sin(pi * x) (' + str(n) + ' random points): ')
    print('pi estimate = ',2.0 / (simulate(under_the_sine, n)/float(n)))
    print('pi actual   = ', pi)

    n = 10000
    print('\nLog2 estimate with y = 1/(x+1) (' + str(n) + ' random points): ')
    print('ln(2) estimate = ', simulate(under_the_inverse, n)/float(n))
    print('ln(2) actual   = ', log(2))

    
