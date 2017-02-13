"""
Challenge Link: https://www.hackerrank.com/contests/projecteuler/challenges/euler001
------------
Description:

For T test cases, sum all the multiples of 3 and 5 up to N.
------------
Constraints:

1 <= T <= 10**5
1 <= N <= 10**5
------------
Algorithm:

Very simple, sum of 3 increasing arithmetic series and 5 increasing arithmetic series minus 15 increasing series.
All these series can be computed in close form, resulting in an extremely fast algorithm.
------------

"""

from fileinput import input

lines = input()
n = int(lines[0])
nums = []
for i in range(1,n+1):
    nums.append(int(lines[i]))

def printSum(n):
    len = lambda div: n//div if n%div!=0 else n//div - 1
    last = lambda div: (n//div)*div if n%div!=0 else (n//div - 1)*div
    series = lambda div: len(div)*(div+last(div))//2
    print(series(3)+series(5)-series(15))

for x in nums:
    printSum(x)
