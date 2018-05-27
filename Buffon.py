from random import random
from math import sin, cos, pi


easy_buffon = lambda d, theta: d <= (.5)*sin(theta)
laplace_buffon = lambda d, theta: d[0] <= .5*sin(theta) or d[1] <= .5*cos(theta)


def run_trial(condition, n):

    counter = 0
    for i in range(n):
        d = random() * .5
        theta = random() * pi * .5
        if condition(d, theta):
            counter += 1

    return counter / float(n)


def laplace_trial(condition, n):

    counter = 0 # this whole function is repetitive. fix.
    for i in range(n):
        d = (random() * .5, random() * .5)
        theta = random() * pi * .5
        if condition(d, theta):
            counter += 1
    return counter / float(n)


if __name__ == '__main__':
    e = easy_buffon
    r = run_trial
    s = [100, 1000, 10000]
    L = [r(e,s[0]), r(e,s[1]), r(e,s[2])]


    print('Running Trials for Simple Buffon.')
    print('--------------------------------')
    for i in range(len(L)):
        print('Pi for ', s[i], ' trials:')
        print('\t', 2.0/L[i])
    print('--------------------------------')


    e = laplace_buffon
    r = laplace_trial
    L = [r(e,s[0]), r(e,s[1]), r(e,s[2])]
    # double gridded buffon needle problem.
    print('Running Trials for Laplace Buffon.')
    print('----------------------------------')
    for i in range(len(L)):
        print('Pi for ', s[i], ' trials:')
        print('\t', 3.0/L[i])
    print('----------------------------------')
