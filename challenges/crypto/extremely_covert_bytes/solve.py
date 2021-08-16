#!/usr/bin/python3

import pwn, binascii, time 

#server = "ctf.cs.technion.ac.il"
server = "127.0.0.1"
#port   = 4042
port   = 1337
block_size = 16
r = pwn.remote(server,port)

def getHexBytes(i):
    return binascii.unhexlify('{0:02x}'.format(i))

rec = b''
while not rec.decode().startswith("Enter the message"):
    rec = r.recvline()

#master_guess = b'flag{1_byt3_4t_a'
master_guess = b''
for n in range(31-len(master_guess),-1,-1):
    r.recv()
    baseline = b'A' * n
    r.send(baseline+b'\n')
    base_return = r.recvline().decode().rstrip()[32:64]
    
    print("basline_inject: ",baseline)
    print("base return: ",base_return)
    
    inj2 = b'A'*(n-1) 
    print("inject: ",inj2)
    for x in range(33,128): 
    #for x in range(100,110): 
        guess = getHexBytes(x)
        inj = baseline + master_guess + guess
        try:
            #print(inj)
            time.sleep(0.02)
            r.recv()
            r.send(inj+b'\n')
            iter_ret = r.recvline().decode().rstrip()[32:64]
            if iter_ret == base_return:
                print('----- [MATCH] ----- || block_size: %s || range: %s || guess: %s ' %(block_size,x,guess))
                print('match base: ',base_return)
                print('match ret:  ',iter_ret)
                master_guess += guess
                #print(guess.decode())
                break
            else:
                pass
        except:
            print(ss)
print("FLAG: ", master_guess)

#print(inj)
    

