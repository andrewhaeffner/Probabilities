from random import random


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

in_the_circle = lambda x,y: (x - .5)**2 + (y - .5)**2 <= .25
dummy = lambda x,y: True

def select_satisfying_points(condition, num_of_trials):
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


def main():

    num_of_trials = 1000

    print('Sanity Check: ', select_satisfying_points(dummy, num_of_trials))
    print('Sanity Check ~250: ', select_satisfying_points(lambda x,y: x < .5 and y < .5, num_of_trials))
    print('\npi estimate : ', 4.0 * select_satisfying_points(in_the_circle, 1000)/ 1000.0)


    

if __name__ == '__main__':
    main()
