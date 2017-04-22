alpha = "abcdefghijklmnopqrstuvwxyz"

def brute_force(ciph):
    for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
        for b in range(26):
            print("{}, a: {}, b: {}", decrypt_str(ciph, a, b), a, b)
        
def decrypt_str(cipher, a, b):
    deciph = ""
    for c in cipher.lower():
        #print("{} {}", alpha[(ord(c) - 97 + key) % 26], (ord(c) - 97 + key) % 26)
        deciph += alpha[(a*ord(c) + b) % 26]
    return deciph

brute_force("yjsmxjmsjpb")
