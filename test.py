import math

def extended_gcd(a, b):
    # Extended Euclidean algorithm to find gcd(a, b) and coefficients s, t
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    
    while r != 0:
        q = old_r // r
        (old_r, r) = (r, old_r - q * r)
        (old_s, s) = (s, old_s - q * s)
        (old_t, t) = (t, old_t - q * t)
    
    return (old_r, old_s, old_t)

def encrypt(message, public_key, modulus):
    # RSA encryption: c ≡ m^e (mod N)
    return pow(message, public_key, modulus)

def decrypt(ciphertext, private_key, modulus):
    # RSA decryption: m ≡ c^d (mod N)
    return pow(ciphertext, private_key, modulus)

# Given values
p = 347
q = 463
e = 7
N = p * q
phi = (p - 1) * (q - 1)
d = extended_gcd(e, phi)[1] % phi

m = 5645

# Encrypt the message
c = encrypt(m, e, N)

# Decrypt the message
m_decrypted = decrypt(c, d, N)

print("Encrypted message:", c)
print("Decrypted message:", m_decrypted)
