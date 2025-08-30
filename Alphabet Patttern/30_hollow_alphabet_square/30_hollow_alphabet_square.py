#Pattern 30
#Hollow Alphabet Square Pattern

"""
A B C D E 
A       E 
A       E
A       E
A B C D E
"""

for i in range (5):
    for j in range(5):
        if i ==0 or i ==4 or j ==0 or j==4:
            print(chr(65+j), end=" ")
        else:
            print(" ", end=" ")
    print()
