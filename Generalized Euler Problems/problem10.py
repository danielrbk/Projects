"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler010
------------
Description:

For T test cases, find the sum of all primes up to N.
------------
Constraints:

1 <= T <= 10**4
1 <= N <= 10**6
------------
Algorithm:

Generate all primes up to 10**6, precalculate all the sums between 1 to 10**6 iteratively, store in a list and run the
test cases.
------------
"""

from fileinput import input

lines = input()
n = int(lines[0])
nums = []
for i in range(1,n+1):
    nums.append(int(lines[i]))

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

primes = primes2(10**6)
sums = [0]*(10**6+1)
i=0
for p in primes:
    if p==2:
        sums[0:2] = [0,0]
        i=p
    else:
        sums[i:p+1]=[sums[i-1] + i]*(p+1-i)
        i=p

for num in nums:
    print(sums[num])
