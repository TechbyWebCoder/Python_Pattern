#Pattern 18
#Mirror Number Pattern

"""
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
"""

for i in range(1, 6):
    print(" " * (5-i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()
