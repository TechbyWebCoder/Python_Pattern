#Pattern 13
#Right Aligned Number Triangle

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

for i in range(1,6):
    print(" " * (5-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    print()
