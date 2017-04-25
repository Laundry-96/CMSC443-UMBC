import miller_rabin
import random
random.seed()

def get_prime():
    a = random.getrandbits(512)
    while(not miller_rabin(a)):
        a = random.getrandbits(512)

p = get_prime()
q = get_prime()

found = False

while not found:
    n = random.getrandbits(512)
    if n%2 == 0:
        n+=1
    found = miller_rabin(n)

phi = (p-1) * (q-1)
n 
