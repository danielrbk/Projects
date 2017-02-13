"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler004
------------
Description:

For T test cases, print the largest palindrome product smaller than n composed of two 3 digit numbers.
------------
Constraints:

1 <= T <= 100
101101 < N < 10**6
------------
Algorithm:

If we denote a palindrome number by its base notation, i.e 103 = 1*10**2 + 0*10**1 + 3*10**1, we can observe that
palindromes composed of the product of two numbers are divisible by 11, thus we can greatly reduce our search time.
------------
"""

def biggestPalindrome(n):
    string = ""
    palindrome = False
    max = 0
    for i in reversed(range(10**3)):
        for j in reversed(range(0,10**3,11)):
            palindrome = True
            string = str(i*j)
            for k in range(len(string)):
                if string[k]!=string[len(string)-1-k]:
                    palindrome=False
                    break
            if palindrome:
                if n>i*j>max:
                    max = i*j
    return max

t = int(input())
for a0 in range(t):
    n = int(input())
    print(biggestPalindrome(n))
