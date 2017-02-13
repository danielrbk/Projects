"""
For n, find the maximum product of k consecutive digits in n.
Also pretty trivial
"""

t = int(input())

for a0 in range(t):
    n,k = [int(x) for x in input().strip().split( )]
    n = int(input())
    n = [int(x) for x in list(str(n))]
    prod=1
    maxProd = 0
    count=0
    finished=False
    for i in range(len(n)):
        if n[i]==0:
            finished=False
            count=0
            prod=-1
        elif count<k:
            prod*=n[i]
            count+=1
            if count==k:
                prod = -prod if prod<0 else prod
                if prod>maxProd:
                    maxProd = prod
        elif count==k:
            prod = -prod if prod<0 else prod
            prod//=n[i-k]
            prod*=n[i]
            if prod>maxProd:
                maxProd = prod
    print(maxProd)

