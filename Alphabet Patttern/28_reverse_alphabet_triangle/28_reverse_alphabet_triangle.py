#Pattern 28
#Reverse_Alphabet Triangle Pattern

"""
A B C D E 
A B C D 
A B C
A B
A
"""

for i in range(5, 0, -1):
    for j in range(65,65+i):
        print(chr(j), end=" ")
    print()
