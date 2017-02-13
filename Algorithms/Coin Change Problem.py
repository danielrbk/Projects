"""
Challenge link: https://www.hackerrank.com/challenges/coin-change

Classical dynamic programming problem, we sort the coins via descending value order.
We create a matrix where the column implies how many types of coins we can use, where the first column is all coins
and the last column means we can use no coins.

The subset of problems is:
O(Value,Coins) = sum(O(Value - i*max(Coins), Coins \ max(Coins)) while i*max(Coins)<=Value))

"""

n,m = [int(x) for x in input().strip().split( )]
coins = [int(x) for x in input().strip().split( )]

coins = sorted(coins)[::-1]
zeroes = [0]*(m+1)
maxVal = []
for i in range(n+1):
    maxVal.append(zeroes.copy())

maxVal[0] = [1]*(m+1)

smallestCoin = coins[-1]


for i in range(smallestCoin,n+1,1):
    for j in reversed(range(len(coins))):
        maxVal[i][j] = sum([maxVal[i-x][j+1] for x in range(0,i+1,coins[j]) if i-x>=0])

print(maxVal[n][0])
