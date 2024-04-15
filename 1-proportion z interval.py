from scipy.stats import norm
import math

'''A CBS News/New York Times poll found that 329 out of 763 adults said they would travel to outer space in their lifetime, given the chance. 
Estimate the true proportion of adults who would like to travel to outer space with 92% confidence.

Confidence Interval = p_hat(+/-)z*(sqrt((p_hat*q_hat)/n))
x_bar: sample mean
t: t-value that corresponds to the confidence level
s: sample standard deviation(Standard Error)
n: sample size

If we’re working with larger samples (n≥30), 
we can assume that the sampling distribution of the sample mean is normally distributed 
(thanks to the Central Limit Theorem) and can instead use the norm.interval() function from the scipy.stats library.
'''
#successes
successes = int(input("Number of successes: "))
sampleSize = int(input("Sample Size: "))

#Sample Proportion
pHat = float(successes/sampleSize)
#1 - Sample Proportion
qHat = 1 - pHat
#sample size
n = sampleSize


#Z-score
Z_star = norm.ppf(0.92)
print("Z-value", Z_star)

#standard error for sample proportion
SE = math.sqrt((pHat*qHat)/n)

#Margin of Error(MoE)
MoE = (Z_star * SE)
print("Margin of Error:", MoE)


upperLimit = pHat + (Z_star * SE)
lowerLimit = pHat - (Z_star * SE)

print(f"Confidence interval:({lowerLimit} ,{upperLimit})")


