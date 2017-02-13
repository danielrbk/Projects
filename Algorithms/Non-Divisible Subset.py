"""
Challenge link: https://www.hackerrank.com/challenges/non-divisible-subset

Given a set of n integers in the range 1 <= x <= 10**9
Print the size of the maximal subset where no 2 numbers add up to a number divisible by k.

Premise to solve this problem is simple but not at all trivial to find.
If we counter the occurrences of a remainder, we can sort the remainders in a descending order, and then for each
remainder if we haven't added its additive inverse we add it to the subset (because we're looking for the max subset)

Note that under algebraic fields, there exists only one additive inverse such that a + b = 0 (mod k)

Special cases include:
    1. Half of k if k is even, where we can add only one number otherwise we can add up to k
    2. 0, same reasoning.

Constraints:
1 <= n <= 10**5
1 <= k <= 100

"""

from collections import Counter

trash, k = [int(x) for x in input().strip().split()]
a = [int(x) % k for x in input().strip().split()]
d = Counter(a)
a = sorted(a, key=lambda a: [d[a], a])
a = a[::-1]
disallowed = set()
count = 0
i = 0

l = len(a)
while i < l:
    key = a[i]
    i += d[key]
    if key not in disallowed:
        if (k % 2 == 0 and key == k / 2) or key == 0:
            count += 1
        else:
            count += d[key]
        other = -key % k
        if d.get(other, -1) != -1:
            disallowed.add(other)

print(count)
