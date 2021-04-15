#18, 5%
from math import inf

def solution(A):
    T = [[0 for j in range(i)] for i in range(1, 16)]
    T[0][0] = A[0][0]
    
    # Define T[i][j]: maximum sum ending at the j-th element of i-th row
    # Recurrence, T[i][j] = A[i][j] + maximum {T[i - 1][j - 1], T[i - 1][j]}
    
    for i in range(1, 15):
        for j in range(i + 1):
            l, r = -inf, -inf
            
            # handle the corner cases for the beginning/end of a row
            try: l = T[i - 1][j - 1]
            except IndexError: pass
            try: r = T[i - 1][j]
            except IndexError: pass
            
            T[i][j] = max(l, r) + A[i][j]
    
    # the solution is the maximum element of the last row
    return max(T[14])

# The original triangle
A =               [[75],
                  [95, 64],
                 [17, 47, 82],
                [18, 35, 87, 10],
               [20, 4, 82, 47, 65],
              [19, 1, 23, 75, 3, 34],
             [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
           [41, 41, 26, 56, 83, 40, 80, 70, 33],
          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
       [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
      [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

print(solution(A))