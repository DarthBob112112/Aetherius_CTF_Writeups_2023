Based on the description of the challenge, I looked at the wikipedia for RSA where i found this under faulty key generation
```
The numbers p and q should not be "too close", lest the Fermat factorization for n be successful. If p − q is less than 2n1/4 (n = p⋅q, which even for "small" 1024-bit values of n is 3×1077), solving for p and q is trivial.
```
So I found [code](./decrypt.py) for fermat factorization and let it run on `n`. The program spat out `p` and `q` pretty quickly (<10sec).
Feeding `n`, `p`, `q`, `e` to a RSA decoder, we get the flag.

# Flag
```aetherius{Wait-till-the-quantum-computers-take-over-c2599e17-36c3-4cea-9b98-8cbdabb604bf}```