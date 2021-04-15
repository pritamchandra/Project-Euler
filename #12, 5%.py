#12, 5%
# Let d(n) = # divisors of n.
# if n = m(2^k), where m is a odd number, then d(n) = (k + 1)d(m)
def count_factors(n, two_power = 1):
    if n%2 == 0:
        return count_factors(int(n/2), two_power + 1)
    
    m, count = sqrt(n), 0
    for div in range(1, ceil(m), 2):
        if n%div == 0: count += 2
            
    if m == int(m): count += 1
        
    return count*two_power

# store n and d(n) for whichever n we come across
master = {1:1}

lim = 500
n, num_div = 1, 0

while num_div <= lim:
    if n%2 == 0: a, b = int(n/2), n + 1
    else: a, b = n, int((n + 1)/2)

    try: num_div = master[a]*master[b]
    except KeyError:
    # if never seen b before calculate d(b) and store in master
        master[b] = count_factors(b)
        continue

    n += 1
        
print(a*b)