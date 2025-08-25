#Pattern 25
#Alphabet Pyramid Pattern

"""
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""

for i in range(1, 6):
    print(" "* (5-i), end="")
    for j in range (65, 65+i):
        print(chr(j), end="")
    for j in range(65 +i-2,64,-1):
        print(chr(j), end="")
    print()
