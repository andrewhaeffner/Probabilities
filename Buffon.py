from random import random
from math import sin, pi



easy_buffon = lambda d, theta: d <= (.5)*sin(theta)


def run_trial(condition, n):

    counter = 0
    for i in range(n):
        d = random() * .5
        theta = random() * pi * .5
        if condition(d, theta):
            counter += 1

    return counter / float(n)



if __name__ == '__main__':
    e = easy_buffon
    r = run_trial
    s = [100, 1000, 10000]
    L = [r(e,s[0]), r(e,s[1]), r(e,s[2])]

    for i in range(len(L)):
        print('Pi for ', s[i], ' trials:')
        print('\t', 2.0/L[i])
