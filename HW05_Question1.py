# Created by: Luke Heary and Dylan Jackson
# Date: 12/2/19

import matplotlib.pyplot as plt
from random import randrange
import numpy as np
import math
from scipy import stats
from scipy.special import factorial
from matplotlib import pyplot as plt



from scipy.special import factorial
from matplotlib import pyplot as plt
import pandas as pd


def likelihood(theta, n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (theta ** x) * ((1 - theta) ** (n - x))


def posterior_prob(prior, posterior, n_occured, n_events):
    return pd.Series(map(lambda theta: likelihood(theta, n_events, n_occured), prior))


def generative_model(n_events, p):
    return np.random.binomial(n_events, p)


# cherry = 0
# lime = 1
def makeData(cherryCount, limeCount):
    dataSet = list()
    for x in range(0, cherryCount):
        dataSet.append(0)
    for x in range(0, limeCount):
        dataSet.append(1)
    return dataSet

def chooseTen(dataSet):
    chooses = []
    for x in range(10):
        chooses.append(dataSet[randrange(100)])
    return chooses

def main():
    bag1 = .10
    bag2 = .20
    bag3 = .40
    bag4 = .20
    bag5 = .10

    h1 = makeData(100, 0)
    h2 = makeData(75, 25)
    h3 = makeData(50, 50)
    h4 = makeData(25, 75)
    h5 = makeData(0, 100)

    h1c = chooseTen(h1)
    h2c = chooseTen(h2)
    h3c = chooseTen(h3)
    h4c = chooseTen(h4)
    h5c = chooseTen(h5)


    hTest = []
    for x in range(100):
        hTest.append(1)

    prior = pd.Series(sorted(h2))
    sim_data = hTest
    posterior = prior[list(map(lambda x: x == 10, sim_data))]
    posterior_probability = posterior_prob(prior, posterior, 10, 10)

    # let's see what we got
    f, ax = plt.subplots(1)
    ax.plot(prior, posterior_probability)
    ax.set_xlabel("Theta")
    ax.set_ylabel("Likelihood")
    ax.grid()
    ax.set_title("Likelihood of Theta for New Campaign")
    plt.show()


main()
