# Created by: Luke Heary
# Date: 12/3/19

import math
from scipy import stats
from scipy.special import factorial
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def likelihood(theta, n, x):
    return (factorial(n) / (factorial(x) * factorial(n - x))) * (theta ** x) * ((1 - theta) ** (n - x))


def posterior_prob(prior, posterior, n_occured, n_events):
    return pd.Series(map(lambda theta: likelihood(theta, n_events, n_occured), prior))


def generative_model(n_events, p):
    return np.random.binomial(n_events, p)


def ABC(n_occured, n_events, n_draws=1000):
    prior = pd.Series(sorted(np.random.uniform(0, 1, size=n_draws)))
    sim_data = [generative_model(n_events, p) for p in prior]
    posterior = prior[list(map(lambda x: x == n_occured, sim_data))]
    posterior_probability = posterior_prob(prior, posterior, n_occured, n_events)

    # let's see what we got
    f, ax = plt.subplots(1)
    ax.plot(prior, posterior_probability)
    ax.set_xlabel("Theta")
    ax.set_ylabel("Likelihood")
    ax.grid()
    ax.set_title("Likelihood of Theta for New Campaign")
    plt.show()


ABC(5, 16)
