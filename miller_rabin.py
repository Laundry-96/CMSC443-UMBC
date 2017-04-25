import numpy
import math
import random

def miller_rabin(n):
    print("Checking: " + str(n))
    is_prime = False
    for i in range(0, 10):
        m = 1
        k = 1
        while n - 1 != ((2**k)*m):
            m += 2
            if m*(2**k) > n-1:
                m = 1
                k += 1
        random.seed()
        rand = random.randint(1, n-1)
        b = a**m % n
        if b == 1:
            is_prime = True
        for i in range(0, k-1):
            if b == (-1 % n):
                is_prime = True
            else:
                b = b**2 % n
        return false

    return is_prime


