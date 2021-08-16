#!/usr/bin/python3

import pwn 

server = "ctf.cs.technion.ac.il"
port   = 4091

def quickMath(line):
    return int(eval(" ".join(line)))

c = pwn.remote(server,port)

it_c = 0

while True:
    it_c += 1
    raw = c.recvline().decode().rstrip()
    s = raw.replace('?','').split()
    if s[0] == '>':
        s = s[3:]
    elif s[0] == 'What':
        s = s[2:]
    else:
        print("raw line: ",raw)
        break
    print("iteration: %s || line_raw: %s" % (it_c,raw))
    c.send( '{}\n'.format(quickMath(s) ).encode())
