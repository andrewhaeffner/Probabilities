from random import random



def assign(outcome, arcs):
    '''
    returns the index of the proper index to assign
    the outcome to.
    '''
    previous = -1
    threshold = 0
    for i in range(len(arcs)):
        threshold += arcs[i]
        if outcome > previous and outcome <= threshold:
            return i
        previous = threshold

    return i+1


def main():

    num_of_trials = 10000000

    #arcs = [ 1.0/2.0, 1.0/3.0, 1.0/6.0 ] # create three arcs of length 1/2, 1/3, and 1/6 along a circle with unit circumference.

    arcs = [1.0/3.0, 1.0/4.0, 1.0/5.0, 1.0/6.0, 1.0/20.0]

    buckets = dict() # Assignment space for the occurences in each arc.

    for i in range(len(arcs)):
        buckets[i] = 0


    for i in range(num_of_trials):
        if i % (num_of_trials / 10) == 0:
            print('passing trial # ', i)
        outcome = random()
        buckets[assign(outcome, arcs)] += 1


    for bucket in buckets:
        print('Arc of length: ', arcs[bucket], '\nlanded on with prob: ', (buckets[bucket]*1.0)/num_of_trials)

if __name__ == '__main__':
    main()
