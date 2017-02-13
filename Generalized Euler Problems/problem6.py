"""
Find (1+2+...+n)**2 - 1**2 + 2**2 + ... + n**2 for T test cases
Trivial in python
"""

t = int(input())

MAX_N = 10**4
regSum=0
regSums=[]
squaredSum=0
squaredSums=[]
sumOf = lambda n: n*(n+1)//2

for i in range(MAX_N+1):
    regSums.append(sumOf(i)**2)
    squaredSum += i**2
    squaredSums.append(squaredSum)

for a0 in t:
    n = int(input())
    print(regSums[n]-squaredSums[n])
