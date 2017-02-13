"""
Challenge Link: https://www.hackerrank.com/challenges/equal

Given an array of n integers in the value 1 <= x <= 10000, print how many operations are needed to equalize the array.
This number must be the minimum number of operations needed.

The operations are:
    1. Add one to every cell other than a chosen one.
    2. Add two to every cell other than a chosen one.
    3. Add five to every cell other than a chosen one.

Categorized under dynamic programming, this problem can be solved without using dynamic programming at all once we
observe the following:
Adding x to every cell other than one is equivalent to subtracting x from a chosen cell since we only care if the array
is equalized.

Thus we need to find the focal point that we will equalize the array to, for our purposes we will choose the minimum
value of the array as our focal point, m.

Next, observe that the sequence m-4,m-3,m-2,m-1,m is the only sequence of numbers where each number may serve as a
legitimate minimum focal point. (Because m-5 = m with the subtraction of 5, our third operator, thus we have rotated)

Count the number of operations for each of these points and print out the minimum.
"""


t = int(input())

def equalize(arr):
    arr = sorted(arr)
    ops = 0
    resOps = []
    m = arr[0]
    for minVal in range(m-4,m+1,1):
        ops = 0
        for a in arr:
            if a != minVal:
                ops += (a-minVal)//5
                a -= ((a-minVal)//5)*5
                ops += (a-minVal)//2
                a -= ((a-minVal)//2)*2
                ops += a-minVal
        resOps.append(ops)
    return min(resOps)

for a0 in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split( )]
    print(equalize(arr))
