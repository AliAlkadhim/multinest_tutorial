# goal: characterize the posterior distribution of a parameter given a set of data
# p(theta | data) = p(data | theta) * p(theta) / p(data) -> p(theta) =  L(theta) * pi(theta)/Z  
#  but Z = p(data) = \int p(data | theta) pi(theta) d^d theta = \int L(theta) pi(theta) d^d theta is intractable 
# so it is the area under the L vs pi(theta) curve
# Z = \int L(theta) pi(theta) d^d theta = 
# let X = \int pi(theta) d^d theta
# so 
# data -> [multinest] -> p(theta | data), Z
#
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def L(theta, nu, N, M):
    #L1 = poisson(N, theta + nu)
    L1 = stats.poisson.pmf(N, theta + nu)
    L2 = stats.poisson.pmf(M, nu)
    return L1 * L2
