import numpy as np
import matplotlib.pyplot as plt
from random import random

def gen_outcome(lam):
    '''
    Generates an outcome for an exponential
    distribution, given a lambda.
    '''
    return -30*np.log(random())

def run_trial(start, finish, lam, subintervals, num_of_points):

    results = dict()
    for i in range(subintervals):
        results[i] = 0

    divisions = []
    current = start
    step = (finish - start) / subintervals
    for i in range(subintervals + 1):
        divisions.append(current)
        current += step


    i = 0
    while i < num_of_points:
        outcome = gen_outcome(lam)
        #print('outcome: ', outcome)
        #a = input()
        if start < outcome < finish:
            prev = 0
            j = 1
            while j < len(divisions):
                if divisions[prev] < outcome < divisions[j]:
                    results[j-1] += 1
                    break
                prev = j
                j += 1
        else:
            continue
        i += 1

    for event in results:
        results[event] /= num_of_points
        results[event] /= ((finish - start) / subintervals)
        print('yo: ', results[event])

    return results

if __name__ == '__main__':

    fig, ax = plt.subplots()

    start = 0
    finish = 120
    lam = 30 # lam signifies the average time between events for an exponential distribution of probabilities.
    subintervals = 24
    num_of_points = 10000

    x = np.linspace(start, finish, 256)
    k = 1/lam
    y = (k)*np.exp(-k*x)

    ax.plot(x,y)


    results = run_trial(start, finish, lam, subintervals, num_of_points)

    divisions = []
    current = start
    step = (finish - start) / subintervals
    for i in range(subintervals):
        divisions.append(current)
        current += step

    formatted_result = []
    for result in results:
        formatted_result.append(results[result])


    ax.hist(divisions, subintervals, weights=formatted_result)

    plt.show()

    for result in results:
        print('Result #', result)
        print('\t', results[result])
