"""
trivial in python
"""

t = int(input())
for a0 in range(t):
    n = int(input())
    n = str(2**n)
    print(sum([int(x) for x in n]))