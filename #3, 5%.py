#3, 5%
# lpf: largest prime factor. 
# key insight: the smallest divisor of a number must be prime

def lpf(n):
    for div in range(2, int(sqrt(n)) + 1):
        if n%div == 0:
            return max(div, lpf(int(n/div)))
    
    return n

print(lpf(600851475143))