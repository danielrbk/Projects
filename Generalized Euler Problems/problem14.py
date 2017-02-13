"""
Challenge link: https://www.hackerrank.com/contests/projecteuler/challenges/euler014
------------
Description:

For T test cases, print the value under N for which the longest collatz sequence is produced.
------------
Constraints:

1 <= T <= 10**4
1 <= N <= 5*10**6
------------
Algorithm:

To improve access times, we will use an array with the size of 5*10**6+1
a[i] will represent the length of the collatz sequence starting at i.
While calculating a sequence length, we will keep the visited indices up to the index for which we know the sequence
length and then update all the indices accordingly.
------------
"""

import array

t = int(input())

MAX = 5 * 10 ** 6
dict = array.array('I', [0] * (MAX + 1))

dict[1] = 1
i = 1
count = 1
while i < MAX:
    dict[i] = count
    i *= 2
    count += 1


def colzSeq(n):
    l = dict
    if l[n] == 0:
        j = n
        prev = []
        ap = prev.append
        while j >= MAX or l[j] == 0:
            ap(j)
            if j % 2 == 0:
                j //= 2
            else:
                j = 3 * j + 1
        seqL = l[j]
        length = len(prev)
        for i in reversed(range(length)):
            if prev[i] < MAX:
                l[prev[i]] = seqL + (length - i)


l = [0, 1, 2]
app = l.append
maxIndex = 2
max = 2
for n in range(3, MAX + 1):
    colzSeq(n)
    if dict[n] >= max:
        max = dict[n]
        maxIndex = n
    app(maxIndex)

for a0 in range(t):
    n = int(input())
    print(l[n])
