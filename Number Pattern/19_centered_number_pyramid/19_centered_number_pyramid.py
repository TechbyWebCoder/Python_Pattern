#Pattern 19
#Centered Number Pyramid

"""
    1
   121
  12321
 1234321
123454321
"""

for i in range(1 , 6):
    print(" " * (5-i) , end="")
    for j in range (1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end ="")
    print()
