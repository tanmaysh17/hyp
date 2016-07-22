import numpy as np
import random as rm
import smd


TRIALS = 5000
tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7];
mu = 20
m = np.mean(tips)


def sample(data, N):   # Function for bootstrapping
    global TRIALS
    X_ = []
    for i in range(0, TRIALS):
        samples = []
        sample_indice = rm.sample(range(0, len(data)), N)
        for j in range(0, N):
            k = data[sample_indice[j]]
            samples.append(k)
        X_.append(np.mean(samples))
    print X_
    return X_

pop = sorted(smd.rnorm(mu, tips))
X_ = sample(pop, len(tips))
greater = np.sum(X_ >= m)
op = float(greater)/float(TRIALS)
tp = 2*op

print("Observed mean = %0.3f" % m)
print("num greater than mean(tips) = %0.3f" % greater)
print("p-value from bootstrapping (ratio of X_ >= mean(tips) is %0.3f" % tp)
