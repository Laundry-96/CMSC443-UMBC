from math import gcd
def multInvByForce(a,m):
        b = 1
        if(gcd(a,m) != 1):
            return -1
        while  (a * b) % m != 1:
            b += 1

        return b

for i in range(1, 26):
    a = multInvByForce(i,26)
    for j in range(1, 26):
        if a != -1:
            if((a * (10 - j) % 26) == 5 and a * (13 - j) % 26 == 16):
                print(a, j)
            
