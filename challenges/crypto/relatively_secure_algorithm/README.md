# Relatively Secure Algorithm

## How To
```bash
# we are given the values
n = 6468851584...
e = 65537
c = 2471596768...

# Taking the modulos "n" value and passing it to factordb.com we are returned with 5 prime numbers
# adding these prime factors to an array called primes
primes = [ <prime_1>, ... ]

# we then import retuired libraries 
import Crypto.PublicKey import RSA # not required but needed to produce a private key file
from math import prod
import binascii, gmpy2

# test that the product of the primes is the modulos
assert(n==prod(primes))

# fine phi
phi = prod([p-1 for p in primes])

# find the private exponent
d = gmpy2.invert(e,phi)

# create key and print if needed
key = RSA.construct( (n,e,d) )
fd = open('private.pem','wb')
fd.write(key.exportKey())
fd.close()

# decrypt the ciphertext "c" message
m = pow(c,d,n)
pt = binascii.unhexlify(hex(m)[2:]).decode()

# print the flag
print(pt)
```

## Flag
`flag{Rs4_1s_s1mpl3_t0_us3_4nd_4t7ack}`
