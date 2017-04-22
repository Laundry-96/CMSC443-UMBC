import math
def pollard(n,B):
        a = 2
        for j in range(2,B):
            a = a**j % n
        d = math.gcd(a-1,n)
        if 1 < d and d < n:
            return d
        return -a

print(pollard
