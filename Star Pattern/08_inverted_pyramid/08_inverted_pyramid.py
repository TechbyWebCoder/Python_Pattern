#Pattern 8
#Inverted Pyramid Pattern

"""
 *********
  *******
   *****
    ***
     *
"""

for i in range(5, 0, -1):
    print(" "* (5-i) + "*" * (2*i-1))
