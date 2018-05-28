from random import random

# This creates script creates a spinner with unit
# circumference. It then uses a random number generator
# to simulate 'spins'. It then records the proportion
# of occurences for each event. Here, events are
# divided into portions of arc along the spinner.

def assign(outcome, arcs):
    '''
    Takes as arguments the randomly generated
    outcome and the arcs along the spinner.

    Returns the index of the arc in which the
    outcome falls.
    '''

    # for each piece of arc, check if the outcome falls
    # inside that piece.
    previous = -1
    threshold = 0
    for i in range(len(arcs)):
        threshold += arcs[i]
        if outcome > previous and outcome <= threshold:
            return i
        previous = threshold

    return i+1

if __name__ == '__main__':

    num_of_trials = 10000000

    # Represents the splitting of the unit circle into arcs
    # that sum up to 1.
    # In the event of an overflow or underflow of arclength
    # 1, this program ignores it.
    arcs = [1.0/3.0, 1.0/4.0, 1.0/5.0, 1.0/6.0, 1.0/20.0]

    # occurences is a dictionary that creates labels 0 .. n
    # for each length of arc. At each locus it will keep
    # a memory of how many times the random variable
    # lands that locus' respective arc.
    occurences = dict()
    for i in range(len(arcs)):
        occurences[i] = 0

    print('Spinner simulation running with ', num_of_trials, ' trials.\n')
    print('Starting...\n')

    for i in range(num_of_trials):
        if i % (num_of_trials / 10) == 0 and not i == 0:
            print(str(int(i*100/num_of_trials)) + '% complete.')
        outcome = random()
        occurences[assign(outcome, arcs)] += 1

    print('Complete\n')
    print('Results of Simulation')
    print('---------------------')

    for event in occurences:
        print('Arc of length: ', arcs[event], ' was landed on:\n\t', str((occurences[event]*100.0)/num_of_trials) + '% of the time.')

    print('---------------------\n')
