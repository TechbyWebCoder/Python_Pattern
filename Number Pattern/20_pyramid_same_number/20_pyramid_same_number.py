#Pattern 20
#Pyramid Same Number Pattern

"""
    1 
   2 2 
  3 3 3
 4 4 4 4
5 5 5 5 5
"""

for i in range (1, 6):
    print(" " * (5-i) + (str(i)+ " ") * i)
