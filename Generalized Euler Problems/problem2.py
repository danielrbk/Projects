"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler002
------------
Description:

For T test cases, find the sum of all even fibbonaci numbers up to N.
------------
Constraints:

1 <= T <= 10**5
10 <= N <= 4*10**16
------------
Algorithm:

Also simple if one notices every third fibbonaci number is even.
Can be computed efficiently if we transform the fibbonaci equation to one which generates only even numbers.

Define G(n) = fibbonaci(3*n), then:
G(n+2) = 4*G(n+1) + G(n)
Which can be proven using algebra.

Initial values:
G(1) = 2
G(2) = 8
------------


"""

from fileinput import input

lines = input()
n = int(lines[0])
nums = []
for i in range(1,n+1):
    nums.append(int(lines[i]))

for n in nums:
    a = 2
    b = 8
    sum = 10
    while 4*b+a<=n:
        a,b = b,4*b+a
        sum += b
    print(sum)

