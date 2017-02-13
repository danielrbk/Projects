"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler015
------------
Description:

For T test cases, in a NxM grid, starting from the top left corner and moving only left and right,
calculate the number of ways to reach the bottom right corner.
------------
Constraints:

1 <= T <= 10**3
1 <= N <= 500
1 <= M <= 500
------------
Algorithm:

Can be calculated using binomial coefficients easily, however I preferred using the property that the number of ways to
reach the bottom right is the number of ways to reach the bottom right from the cell to the right plus number of ways
to reach the bottom right from the cell to the left.
Thus, we can calculate the solution bottom up for the grid.

Another option could be to precalculate the grid for the max values and just return [n,m] for each test case.
------------
"""

def f(n, m):
    l = [1] * n
    for trash in range(1, m):
        l[0] = 1
        for i in range(1, len(l)):
            l[i] = l[i] + l[i - 1]
    return l[n - 1]


t = int(input())
for a0 in range(t):
    n, m = [int(x) + 1 for x in input().strip().split()]
    print(f(n, m) % (10 ** 9 + 7))
