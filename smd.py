import numpy as np

def rnorm(pop_mu, tips):
    pop_std = np.std(tips)
    pop = np.random.normal(pop_mu, pop_std, 1000)
    return pop