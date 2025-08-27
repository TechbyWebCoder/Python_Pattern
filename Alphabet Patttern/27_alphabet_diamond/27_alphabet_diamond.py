#Pattern 27
#Alphabet Diamond

"""
    A
   BBB
  CCCCC
 DDDDDDD
EEEEEEEEE
 DDDDDDD
  CCCCC
   BBB
    A
"""

n = 5
for i in range(1, n+1):
    print(" "* (n-i) + chr(64+i)*(2*i-1))
for i in range(n-1, 0, -1):
    print(" " * (n-i)+ chr(64+i)* (2*i-1))
