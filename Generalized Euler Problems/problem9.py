"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler009
------------
Description:

Find a pythagorean triplet a**2 + b**2 = c**2 such that a+b+c = N with the maximal product a*b*c and print the product.
------------
Constraints:

1 <= T <= 3000
1 <= N <= 3000, although my algorithm runs extremely fast for far larger N's
------------
Algorithm:

denote a = m**2 - n**2, b = 2*m*n, c = m**2 + n**2 such that m>n>0 and gcd(m,n)=1.
Then all for all such m,n we can generate a primitive pythagorean triplet.
To support non-primitive triplets, we multiply all members of the triplet by t and use the following property:
n = k / (2 * t * m) - m, deduced by the equation a+b+c = k for which k is given.
Note that if a triplet exists such that a+b+c=k, then k is divisible by k/(2*t*m), thus we can limit m to all factors
of k/(2*t) for every t up to k/2.
We can generate the factors of k/(2*t) in a short amount of time using the Sieve of Eratosthenes.
------------
"""

import sys

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

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


def getPrimeFactors(n):
    """
    Factors a number into its prime components
    :param n: The number to factor
    :return: A list of the form (p,e) where n = p1**e1 * p2**e2 ...
    """
    primes = primes2(n)
    factors = []
    for i in range(len(primes)):
        if n % primes[i] == 0:
            temp = n
            exp = 0
            while (temp % primes[i] == 0):
                temp /= primes[i]
                exp += 1
            factors.append(tuple([primes[i], exp]))
    return factors


def getAllFactors(n):
    """
    Factors a number into all possible composites, sorted by size.
    :param n: The number to factor
    :return: A list of all factors of the number
    """
    factors = []

    def generateFactor(primeFactors, currIndex, mul=1):
        if currIndex >= len(primeFactors):
            factors.append(mul)
        else:
            p, e = primeFactors[currIndex]
            for i in range(e + 1):
                generateFactor(primeFactors, currIndex + 1, mul * (p ** i))

    primeFactors = getPrimeFactors(n)
    generateFactor(primeFactors, 0)
    return sorted(factors)


def getTriplet(k):
    if k%2!=0:
        print(-1)
        return
    found = False
    for t in range(1, k // 2 + 1):
        if k % (2 * t) != 0:
            continue
        factors = getAllFactors(k // (2 * t))
        for m in reversed(factors):
            n = k // (2 * t * m) - m
            if n >= m or n <= 0 or (m%2!=0 and n%2!=0) or gcd(m,n)!=1:
                continue
            found = True
            break
        if found:
            a = t * (m ** 2 - n ** 2)
            b = t * 2 * m * n
            c = t * (m ** 2 + n ** 2)
            print("{0}".format(a * b * c))
            break
    if not found:
        print(-1)

def getPrimitiveTriplets(k):
    if k%2!=0:
        return 0
    found = False
    t = 1
    factors = getAllFactors(k // (2 * t))
    for m in reversed(factors):
        n = k // (2 * t * m) - m
        if n >= m or n <= 0 or (m%2!=0 and n%2!=0) or gcd(m,n)!=1:
            continue
        found = True
        break
    if found:
        a = t * (m ** 2 - n ** 2)
        b = t * 2 * m * n
        c = t * (m ** 2 + n ** 2)
        print("{0} + {1} + {2} = {3}".format(a,b,c,k))
        print("{0}".format(a * b * c))
        return 1
    return 0


t = int(input().strip())
for n in range(3000):
    getTriplet(n)

