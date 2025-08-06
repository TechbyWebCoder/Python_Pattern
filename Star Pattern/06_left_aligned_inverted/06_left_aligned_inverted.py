#Pattern 6
#Left-Aligned Inverted Triangle

"""
* * * * *
  * * * *
    * * *
      * *
        *
"""

for i in range(5, 0, -1):
    print(" "* (5-i) + "*"* i)
