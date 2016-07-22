import numpy as np

def rnorm(pop_mu, tips):
    pop_std = np.std(tips, ddof=1)
    pop = np.random.normal(pop_mu, pop_std, len(tips))
    return pop