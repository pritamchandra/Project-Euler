#193, 55%

from math import sqrt, floor, ceil

N = 2**50
M = ceil(sqrt(N))
is_prime = [True for n in range(M)]

# sieve to calculate primes till sqrt(N)
for p in range(2, ceil(sqrt(M))):
    if is_prime[p]:
        for mul in range(p*p, M, p):
            is_prime[mul] = False
            
# collecting all prime squares less than N
sq_primes = []
for p in range(2, M):
    if is_prime[p]: sq_primes.append(p**2) 

'''
use PIE. Traverse lexicographically through the subsets of the prime 
squares list obtained. Break whenever the product of a subset exceeds 
N. In this way the sum space is reduced exponentially; because for 
products that exceed N, floor(N/product) contributes 0 to the sum. 
'''
n = len(sq_primes)
Sum = 0

def make_next_product(product, sign, last):
    global Sum
    Sum += floor(N/product)*sign
    
    for j in range(last, n):
        new_prod = product*sq_primes[j]
        if new_prod > N: break
        make_next_product(new_prod, -1*sign, j + 1)
        
make_next_product(1, 1, 0)
Sum