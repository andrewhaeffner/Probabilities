import numpy as np
import matplotlib.pyplot as plt
from random import random

def gen_outcome(lam):
    '''
    Generates an outcome for an exponential
    distribution, given a lambda.
    '''
    return -lam*np.log(random())

def run_trial(start, finish, lam, subintervals, num_of_points):
    '''
    Runs a trial given a set of parameters.
    Returns the area scaled heights of rectangles
    for a histogram.
    '''

    results = [0 for i in range(subintervals)]

    bucket_step = (finish - start) / subintervals
    divisions = [i * bucket_step for i in range(subintervals+1)]

    i = 0
    while i < num_of_points:
        outcome = gen_outcome(lam)
        if start < outcome < finish:
            prev = 0
            j = 1
            while j < len(divisions): # place each outcome into the proper bucket.
                if divisions[prev] < outcome < divisions[j]:
                    results[j-1] += 1
                    break
                prev = j
                j += 1
            i += 1

    for event in range(len(results)):
        results[event] /= (num_of_points * bucket_step)

    return results

if __name__ == '__main__':

    fig, ax = plt.subplots()

    start = 0
    finish = 120
    lam = 30 # lam signifies the average time between events for an exponential distribution of probabilities.
    subintervals = 24
    num_of_points = 100000 # Number of random outcomes selected.

    x = np.linspace(start, finish, 256)
    k = 1/lam
    y = (k)*np.exp(-k*x) # graph that fits the histogram.

    results = run_trial(start, finish, lam, subintervals, num_of_points)

    # The histogram step has to be different from the bucket step
    # because the histogram uses start and finish as endpoints AND
    # delineators. Adjusting the subintervals down by 1 creates
    # the proper spacing for rectangles. I found this frustrating.
    hist_step = (finish - start) / (subintervals-1) 

    divisions = [(i * hist_step) for i in range(subintervals)]

    ax.plot(x,y)
    ax.hist(divisions, subintervals, weights=results)

    plt.show()
