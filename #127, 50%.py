#127, 50%
from math import sqrt, ceil, log

N = 120001

# Make a sieve to calculate primes till N
is_prime = [True for n in range(N)]
is_prime[0], is_prime[1] = False, False

for p in range(2, ceil(sqrt(N))):
    if is_prime[p]:
        for mul in range(p*p, N, p):
            is_prime[mul] = False
            
primes = []
for p in range(2, N):
    if is_prime[p]: primes.append(p) 
        
# calculate rad(n) for all n <= N
rad = [None, 1, 2, 3, 2]                
for c in range(5, N):
    for prime in primes:
        if c%prime == 0:
            break
    
    power = prime*prime
    while c%power == 0: power = power*prime
    rad.append(prime*rad[int(c*prime/power)])
    
def ordered(x, y):
    if x > y: return (y, x)
    return(x, y)

def is_coprime(x, y):
    x, y = ordered(x, y)
    if x == 1: return True
    if x == y: return False
    if is_prime[y]: return True
    if is_prime[x]:
        if y%x == 0: return False
        return True
    
    for prime in primes:
        if prime > x: break
        if x%prime == 0 and y%prime == 0: return False

    return True

# Make the final checks
Sum = 0
hits = []

for c in range(5, N):
    if is_prime[c]: continue
 
    for a in range(1, ceil(c/2)):
        b = c - a
        if rad[a]*rad[b]*rad[c] > c: continue
            
        if is_coprime(rad[a], rad[b]):
            hits.append((a, b, c))
            Sum += c
            
print(Sum)