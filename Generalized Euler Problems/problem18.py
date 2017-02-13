"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler018
------------
Description:

For T test cases, given a pyramid of integers with N rows, find the descending path between adjacent nodes such that the
 value of the path is maximal.
------------
Constraints:

1 <= T <= 10
1 <= N <= 15
------------
Algorithm:

A difficult problem to solve top-down, however approaching the problem from a bottom up approach makes it really trivial.
The max value of a node is the maximal value of a path originating from it, hence the value of each node in the bottom
row is itself, and the value of the second to last row is the value of the node itself plus the value of its maximal
adjacent node and so on and so forth.
------------
"""

t = int(input())

def maxPathSum(arr):
    for i in reversed(range(len(arr)-1)):
        l = len(arr[i])
        for j in range(l):
            arr[i][j] += max(arr[i+1][j],arr[i+1][j+1])
    return arr[0][0]

for a0 in range(t):
    row = int(input())
    triangle = []
    for r in range(row):
        triangle.append([int(x) for x in input().strip().split( )])
    print(maxPathSum(triangle))



