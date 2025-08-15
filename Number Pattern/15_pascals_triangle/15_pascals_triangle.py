#Pattern 15
#Pascals Triangle Pattern

"""
     1 
    1 1 
   1 2 1
  1 3 3 1
 1 4 6 4 1
"""

from math import comb
n = 5
for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(comb(i, j), end=" ")
    print()
