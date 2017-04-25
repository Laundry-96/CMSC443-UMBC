from miller_rabin import miller_rabin
import random
random.seed()

def get_prime():
    a = random.getrandbits(512)
    while(not miller_rabin(a)):
        a = random.getrandbits(512)

p = get_prime()
q = get_prime()
phi = (p-1) * (q-1)
n = p*q
b = random.randrange(2, phi-1)
while gcd(b,z) != 1:
    b = random.randrange(2,phi-1)
print(p)
print(q)
print(b)
