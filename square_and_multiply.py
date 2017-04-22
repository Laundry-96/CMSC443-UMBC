def square_and_multiply(x,c,n):
    bits = []
    while(c != 0):
        bits.append(c % 2)
        c = c/2

    z = 1
    bits.reverse()
    for i in bits:
        z = z**2 % n
        if i == 0:
            z = z*x % n

    return z

print(square_and_multiply(72993,432,1001))
