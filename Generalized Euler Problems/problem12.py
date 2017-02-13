"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler012
------------
Description:

For T test cases, find the first triangle number to have over N divisors.
------------
Constraints:

1 <= T <= 10
1 <= N <= 10**3
------------
Algorithm:

Since we are searching for the smallest triangle number to have over N divisors, we can assume the number is composed
of relatively small primes, thus we can generate all the primes up to 10**6 and assume it'll do under the constraints.

Next, up until we find a triangle number that has over 10**3 divisors, we iteratively generate a list of the amount of
factors that each index is composed of.
By using the property that the nth triangle number is equal to n*(n+1)/2 and that gcd(n,n+1)=1, we can calculate the
number of factors for n*(n+1)/2 by directly calculating factors(n)*facotrs((n+1)/2), which are 2 previously computed
values.
This dynamic progamming iterative algorithm greatly reduces the runtime of the algorithm, allowing it to run under
the runtime constraint provided by hackerrank (10 seconds to successfully run all test cases).
------------
"""

from fileinput import input
from operator import mul
from functools import reduce

lines = input()
n = int(lines[0])
nums = []
for i in range(1,n+1):
    nums.append(int(lines[i]))

sort = sorted(list(zip(nums,range(len(nums)))))

def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    sieveCap = limit if limit<=2*10**8 else int(limit**0.5)

    segNumber = 0
    primes=[2]
    buf = [False] + [True] * (sieveCap-1)
    while segNumber*sieveCap*2<limit:
        i = 0
        while (primes[-1]**2-1)//2<sieveCap:
            if buf[i]:
                p = 2*(i+sieveCap*segNumber)+1
                primes.append(p)
                step = primes[-1]
                start = (step**2-1)//2
                buf[start::step] = [False]*((sieveCap-start-1)//step + 1)
            i += 1
        for j in range(i, sieveCap):
            if buf[j]:
                primes.append(2*(j+sieveCap*segNumber)+1)
        del buf
        segNumber+=1
        buf = [True] * sieveCap
        for i in range(1,len(primes)):
            p = primes[i]
            initialIndex = (p-1)//2
            currPageLastIndex = sieveCap*segNumber + sieveCap-1
            prevPageLastIndex = currPageLastIndex - sieveCap
            if (currPageLastIndex-initialIndex)//p!=(prevPageLastIndex-initialIndex)//p:
                start = (initialIndex + (((prevPageLastIndex-initialIndex)//p + 1)*p))%sieveCap
                for i in range(start, sieveCap, p):
                    buf[i] = False

    sliceIndex = 0
    for p in reversed(primes):
        if p>limit:
            sliceIndex+=1
    return primes[0:len(primes)-sliceIndex]

def calculateFactors(x):
    cap = int(x ** 0.5)
    cnt=0
    if x % 2 == 0:
        temp = x
        while temp%2==0:
            temp/=2
            cnt+=1
        return (1+cnt)*factors[x//(2**cnt)]
    for p in primes:
        if x % p == 0:
            temp = x
            while temp%p==0:
                temp/=p
                cnt+=1
            return (1+cnt)*factors[x//(p**cnt)]
        if p>=x:
            return 2
    return -1


primes = primes2(1000000)
factors=[0,1,2,2]
factorTriangle = [0,1,2]

i=3
while factorTriangle[-1]<=1000 and factorTriangle[-2]<=1000:
    factors.append(calculateFactors(i+1))
    factorTriangle.append(factors[i] * (factors[(i+1)//2]))
    i+=1
    factors.append(calculateFactors(i + 1))
    factorTriangle.append((factors[i//2]) * factors[i + 1])
    i += 1

i=0
sols=[]
for x,y in sort:
    while x>=factorTriangle[i]:
        i+=1
    sols.append([(i*(i+1))//2, y])

sols = sorted(sols, key=lambda pair: pair[1])
for x,y in sols:
    print(x)

