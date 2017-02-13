"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler007
------------
Description:
For T test cases, find the N'th prime number.
------------
Constraints:

1 <= T <= 10**3
1 <= N <= 10**4
------------
Algorithm:

Using Sieve of Eratosthenes, find all primes up to 10**4, reutrn the nth one.
------------
"""

def primes2(limit):
    if limit < 2: return []
    if limit < 3: return [2]
    sieveCap = limit if limit <= 2 * 10 ** 8 else int(limit ** 0.5)

    segNumber = 0
    primes = [2]
    buf = [False] + [True] * (sieveCap - 1)
    while segNumber * sieveCap * 2 < limit:
        i = 0
        while (primes[-1] ** 2 - 1) // 2 < sieveCap:
            if buf[i]:
                p = 2 * (i + sieveCap * segNumber) + 1
                primes.append(p)
                step = primes[-1]
                start = (step ** 2 - 1) // 2
                buf[start::step] = [False] * ((sieveCap - start - 1) // step + 1)
            i += 1
        for j in range(i, sieveCap):
            if buf[j]:
                primes.append(2 * (j + sieveCap * segNumber) + 1)
        del buf
        segNumber += 1
        buf = [True] * sieveCap
        for i in range(1, len(primes)):
            p = primes[i]
            initialIndex = (p - 1) // 2
            currPageLastIndex = sieveCap * segNumber + sieveCap - 1
            prevPageLastIndex = currPageLastIndex - sieveCap
            if (currPageLastIndex - initialIndex) // p != (prevPageLastIndex - initialIndex) // p:
                start = (initialIndex + (((prevPageLastIndex - initialIndex) // p + 1) * p)) % sieveCap
                for i in range(start, sieveCap, p):
                    buf[i] = False

    sliceIndex = 0
    for p in reversed(primes):
        if p > limit:
            sliceIndex += 1
    return primes[0:len(primes) - sliceIndex]

primes = primes2(110000)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primes[n-1])
