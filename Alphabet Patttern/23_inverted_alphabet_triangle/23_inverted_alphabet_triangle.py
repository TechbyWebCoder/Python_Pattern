#Pattern 23
#Inverted Alphabet Triangle Pattern

"""
A B C D E 
A B C D 
A B C
A B
A
"""

for i in range(69, 64, -1):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()
