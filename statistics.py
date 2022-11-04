#### Statistics ####

# 1. What does the p-value mean in terms of hypothesis testing? With which level of errors is it associated?
# The p-value is the probability of having a similar or more extreme result that the observed.
# For the hypothesis to be accepted usually is taken the value of 5% (0.05) as a threshold, meaning if p-value is smaller than 0.05 we accept
# our case has differences significant enough between groups and otherwise if it is greater than 0.05 we consider the two groups are too similar
# the difference seen is not enough to be considered as such.

# 2. Generate 1000 samples from a normal distribution with fixed mean=500, variance=50 and size=100 for each sample.
import numpy as np

samples = []
for _ in range(1000):
    samples.append(np.random.normal(loc=500, scale=np.sqrt(50), size=100))

# 3. Then, for each sample check with ztest (use threshold of the p-value = 0.2), that the mean of a distribution is 500 (that’s our null hypothesis).
from statsmodels.stats.weightstats import ztest as ztest

ztest_values = []
for sample in samples:
    aux = ztest(sample, value=500)
    ztest_values.append(aux[1])

# 4. What ratio of accepting and rejecting the null hypothesis do you expect to receive and why?
# Since we created the samples ourselves, the acceptance should be very high, because we know that the null hypothesis is indeed true.
# However, randomness makes it not exact, so I would expect something around 90% acceptance and 10% rejection.

# 5. What ratio did you receive in practice?
print(len([value for value in ztest_values if value > 0.2])/len(ztest_values))
# Acceptance = 0.79 , Rejection = 0.21
