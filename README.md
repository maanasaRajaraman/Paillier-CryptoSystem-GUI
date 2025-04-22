# Paillier-CryptoSystem-GUI

1 - Core algorithms
* is_prime checks primality; gcd, fastExponentiation, and modInverse implement number‑theoretic helpers.
* key_gen validates primes, computes modulus n = p q, sets generator g = n + 1, and appends the public pair (n, g) to a flat file keyed by username.
* encrypt chooses a random blinding factor r, verifies gcd(r,n)=1, and returns the standard Paillier ciphertext *c=g<sup>m</sup>r<sup>n</sup> (mod n<sup>2</sup>)*
* decrypt leverages the Carmichael function φ(n) to recover the plaintext. ​

2 - GUI flow
* Key Generation window gathers username and primes; duplicates are rejected.
* Encrypt window lets the sender pick a recipient from a combo‑box populated via getNames, enter a message (integer), and view the computed ciphertext.
* Decrypt window collects private primes and a ciphertext, returning the original message.
* The main window exposes the three actions plus an exit button.

Learning value – The script is ideal for classroom demos: students see every cryptographic step, experiment with small primes, and observe the effects of unsuitable inputs (e.g., non‑prime choices).
