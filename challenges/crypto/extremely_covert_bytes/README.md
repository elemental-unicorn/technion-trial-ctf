# Extremely Covert Bytes

## How To
This challenge required identifying the encryption schema, its block size and deriving the flag through known plain text derevation. 

```python
# find buffer size (code sample tells you) by filling the buffer with all of the same char so 2 blocks have the same output

c.send(b'A'*32)

# This will present 2 blocks that match though vary between runs as a new key is used on connection
# next we need to send through 1 byte less and capture the response - note i originally did this, and the solve shows, with 2 halves of a 16 byte block

c.send(b'A'*31)
baseline = c.recvline().decode().rstrip()

# we then loop through all combinations of a byte to get a match - note we doing actually need to loop over all as its a ctf and ascii chars so limiting to decimal 33-128

for i in range(33,129):
	guess = binascii.unhexlify( hex(i) )
	c.send(b'A'*31 + guess)
	resp = c.recvline().decode().rstrip()
	if resp == baseline:
		print(b"Match with byte -> ", guess

# this is then put in a loop to slowly take the guesses and push them to a master_guess variable which is added in place of the reducing b'A' buffer fill until the plaintext is derived.
```

# Flag 
`flag{1_byt3_4t_a_t1me}`

