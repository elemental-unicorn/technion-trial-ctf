# Ducking 

## How To
```bash
steghide extract -xf - -sf ducking.jpg -p $(exiftool ducking.jpg | grep Comment | sed -E 's/.*passphrase:(\w+).*/\1/')
```

## Flag
`flag{qu4ck_qu4ck}`
