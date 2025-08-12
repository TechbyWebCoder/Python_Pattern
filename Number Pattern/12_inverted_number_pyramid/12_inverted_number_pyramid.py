#Pattern 12
#Inverted Number Pyramid Pattern

"""
1 2 3 4 5 
1 2 3 4 
1 2 3
1 2
1
"""

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
