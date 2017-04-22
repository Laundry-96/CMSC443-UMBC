import math
def mult_inv(a,b):
    q = math.floor(a/b)
    t_0 = 0
    t = 1
    r = a - (b*q)
    while(r > 0):
        temp = (t_0 - q*t) % a
        t_0 = t
        t = temp
        a = b
        b = r
        q = math.floor(a/b)
        r = a - q*b

    if b != 1:
        return -1
    return t
    
print(mult_inv(17,101))
print(mult_inv(357,1234))
print(mult_inv(3125,9987))
