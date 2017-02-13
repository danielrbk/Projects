"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler017
------------
Description:

For T test cases,  print out N in worded numbers, i.e: 13 is thirteen
------------
Constraints:

1 <= T <= 10
1 <= N <= 10**12
------------
Algorithm:

A bit of a pain to implement the algorithm, however it is trivial and implemented in such a way that this is algorithm
is easily expendable to far greater orders of magnitude for N
------------
"""

def countDigits(n):
    c = 0
    while (n != 0):
        c += 1
        n //= 10
    return c


def unit(d,original):
    if original<10 and d == 0:
        return ["Zero"]
    elif d == 1:
        return ["One"]
    elif d == 2:
        return ["Two"]
    elif d == 3:
        return ["Three"]
    elif d == 4:
        return ["Four"]
    elif d == 5:
        return ["Five"]
    elif d == 6:
        return ["Six"]
    elif d == 7:
        return ["Seven"]
    elif d == 8:
        return ["Eight"]
    elif d == 9:
        return ["Nine"]
    else:
        return [""]


def tens(d,original):
    if d == 10:
        return ["Ten"]
    elif d == 11:
        return ["Eleven"]
    elif d == 12:
        return ["Twelve"]
    elif d == 13:
        return ["Thirteen"]
    elif d == 14:
        return ["Fourteen"]
    elif d == 15:
        return ["Fifteen"]
    elif d == 16:
        return ["Sixteen"]
    elif d == 17:
        return ["Seventeen"]
    elif d == 18:
        return ["Eighteen"]
    elif d == 19:
        return ["Nineteen"]
    ten = d // 10
    if ten == 0:
        return unit(d % 10,original)
    elif ten == 2:
        return ["Twenty"] + unit(d % 10,original)
    elif ten == 3:
        return ["Thirty"] + unit(d % 10,original)
    elif ten == 4:
        return ["Forty"] + unit(d % 10,original)
    elif ten == 5:
        return ["Fifty"] + unit(d % 10,original)
    elif ten == 6:
        return ["Sixty"] + unit(d % 10,original)
    elif ten == 7:
        return ["Seventy"] + unit(d % 10,original)
    elif ten == 8:
        return ["Eighty"] + unit(d % 10,original)
    elif ten == 9:
        return ["Ninety"] + unit(d % 10,original)


def hundred(n,original):
    if n < 100:
        return tens(n,original)
    return unit(n // 100,original) + ["Hundred"] + tens(n % 100,original)


def numberToString(n):
    prefix = [["Thousand"], ["Million"], ["Billion"], ["Trillion"]]
    s = []
    l = countDigits(n)
    original = n
    while l >= 4:
        temp = n
        c = 0
        while temp >= 1000:
            c += 1
            temp //= 1000
        hund = n//(10 ** (3 * c))
        if hund!=0:
            s += hundred(hund,original) + prefix[(l - 1) // 3 - 1]
        n = n % (10 ** (3 * c))
        l = countDigits(n)
    s += hundred(n,original)
    s = [x for x in s if x!=""]
    return " ".join(s)

t = int(input())
for a0 in range(t):
    n = int(input())
    print(numberToString(n))
