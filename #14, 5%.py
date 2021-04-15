#14, 5%
N = 10**6
master = {1:1}

def collatz_length(n):
    global master
    try: return master[n]
    except: pass
    
    # store master[n] for every term you encounter    
    next_term = int(n/2) if n%2 == 0 else 3*n + 1
    master[n] = 1 + collatz_length(next_term)
    return master[n]

Max = 1
for n in range(2, N + 1):
    if collatz_length(n) > master[Max]: Max = n
        
print(Max)