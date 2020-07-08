import numpy as np
from scipy import special

for n in range(1,10):
    p = 0
    for x in range(n,6*n+1):
        p += special.binom(6*n,x)*(1/6)**x*(5/6)**(6*n-x)
    print(n, p)