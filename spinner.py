from random import random



def assign(outcome, arcs):
    '''
    returns the index of the proper index to assign
    the outcome to.
    '''
    previous = -1
    for i in range(len(arcs)):
        threshold = arcs[i]
        if outcome > previous and outcome <= threshold:
            return i
        previous = threshold

    return i+1


def main():

    num_of_trials = 10000000

    arcs = [ .5, (.5 + (1.0/3.0)) ] # create three arcs of length 1/2, 1/3, and 1/6 along a circle with unit circumference.

    buckets = dict() # Assignment space for the occurences in each arc.

    for i in range(len(arcs)+1):
        buckets[i] = 0


    for i in range(num_of_trials):
        if i % 100000 == 0:
            print('passing trial # ', i)
        outcome = random()
        buckets[assign(outcome, arcs)] += 1


    for bucket in buckets:
        print('Bucket #: ', bucket, ' yields: ', (buckets[bucket]*1.0)/num_of_trials)

if __name__ == '__main__':
    main()
