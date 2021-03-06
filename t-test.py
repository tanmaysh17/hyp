# Hypothesis Testing Assignment

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

tips = [20.8, 18.7, 19.1, 20.6, 21.9, 20.4, 22.8,
        21.9, 21.2, 20.3, 21.9, 18.3, 21.0, 20.3,
        19.2, 20.2, 21.1, 22.1, 21.0, 21.7];
mu = 20
m = np.mean(tips)
alpha = 0.06

plt.axis([18,22, 0.0, 1.6])
x = np.arange(18, 23, 0.01)
y = stats.norm.pdf(x, mu, np.std(tips)/pow(len(tips), 0.5))
plt.plot(x, y, color='red')
plt.plot(m, 0, 'g^')
plt.text(m, 0.1, "Sample mean = %0.2f" % m)

# t-test

t = (m - mu)/(np.std(tips, ddof=1)/pow(len(tips), 0.5))
p = (1-stats.t.cdf(t,len(tips)-1))
tp = 2*p

print "t is %f" % t
print "one-sided p-value is %f" % p
print "two-sided p-value is %f" % tp
if p > alpha:
    print "p-value (from t-test) = %f" % tp, ", Reject H1"
else:
    print "p-value (from t-test) = %f" % tp, ", Reject H0"

plt.show()