#50, 5%
def solution(n):
    #sieve of eratosthenes, to calculate all primes till n
    def sieve(n):
        isprime = [True for i in range(n + 1)]
        isprime[1] = False
        p = 2
        while p * p <= n:
            if isprime[p]:
                for q in range(p*p, n + 1, p):
                    isprime[q] = False
            p += 1

        return isprime
    
    isprime = sieve(n)
    primes = [p for p in range(n + 1) if isprime[p]] 
    # stored all primes till n
    N = len(primes)
    
    # sumtill[i] is the sum of all primes upto the i-th prime
    sumtill = [0]
    for i in range(1, N):
        sumtill.append(sumtill[-1] + primes[i])
        
    
    consec_sum = [] 
    # store instances when the sum from the i-th 
    # to the j-th prime is also a prime
    maxprime, maxlength = [], 0
    
    # calculate the consecutive sums starting with 2
    # the length of such a series must be even
    for i in range(2, N, 2):
        candidate = sumtill[i]
        try:
            if isprime[candidate]:
                consec_sum.append((0, i, i, candidate))
                if i >= maxlength:
                    maxlength = i
                    maxprime = consec_sum[-1]
        except IndexError: break
    
    # calculate consecutive sums starting with other primes
    # the length of such a series now must be odd
    for j in range(1, N):
        for i in range(j + 1, N, 2):
            candidate = sumtill[i] - sumtill[j]
            try:
                if isprime[candidate]:
                    consec_sum.append((j, i, i - j, candidate))
                    if i - j >= maxlength:
                        maxlength = i - j
                        maxprime = consec_sum[-1]
            except IndexError: break
            
    # Now consec_sum stores all instances of sum of consecutive primes 
    # being a prime, and maxprime stores the one with maximum length
    return maxprime

print(solution(10**6))