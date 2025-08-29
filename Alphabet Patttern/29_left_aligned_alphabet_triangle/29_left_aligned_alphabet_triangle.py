#Pattern 29
#Left Aligned Alphabet Triangle

"""
A
A B
A B C
A B C D
A B C D E
"""

for i in range (65,70):
    for j in range(65, i+1):
        print(chr(j), end="")
    print()
