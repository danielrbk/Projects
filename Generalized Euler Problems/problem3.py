"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler003
------------
Description:

For T test cases, find the largest prime factor of N.
------------
Constraints:

1 <= T <= 10
10 <= N <= 10**12
------------
Algorithm:

Given the very weak constraint on N, none of the sieves proved to work fast enough to generate the primes without
timing out or completely filling the system memory.

Thus a different approach was used, by finding the largest prime factor directly:
I divided N by every number from 2 up to the square root of N as long as N is divisible and keeping the result in N.
Since the division is done in an ascending order, the first number to be divided into 1 is also the largest prime factor.
------------

"""


from fileinput import input

lines = input()
n = int(lines[0])
nums = []
for i in range(1,n+1):
    nums.append(int(lines[i]))

stopLoop = False

for x in nums:
    old = x
    cap = int(x**0.5)
    while x%2==0:
        x/=2
    if(x==1):
        print(2)
    else:
        stopLoop = False
        for i in range(3,cap+3,2):
            if stopLoop:
                break
            while x%i==0:
                if(x/i==1):
                    print(i)
                    stopLoop = True
                x//=i
        if not stopLoop:
            print(int(x))

