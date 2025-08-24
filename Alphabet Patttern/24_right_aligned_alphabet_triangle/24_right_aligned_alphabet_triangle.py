#Pattern 24
#Right Aligned Alphabet Triangle

"""
        A   
      A B
    A B C
  A B C D
A B C D E
"""

for i in range(1,6):
    print(" " *(5-i)+"".join(chr(64+j) for j in range(1,i+1)))
    
