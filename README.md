# Diffie-Hellman Key Exchange Implementation

A Python implementation of the Diffie-Hellman key exchange protocol for educational purposes.

## Overview

This project demonstrates the Diffie-Hellman key exchange protocol, including:
- Prime number generation using Miller-Rabin primality testing
- Primitive root finding
- Public/private key generation
- Shared secret computation
- Message encryption using XOR

## Educational Purpose Only

This implementation uses configurable parameters (default: 25-digit primes) to demonstrate:
- How the DH protocol works mathematically
- Why parameter size matters for security
- The discrete logarithm problem

**Security Warning:** Default parameters (25-digit primes) are intentionally weak for educational purposes and can be broken in seconds. DO NOT use for real security!

## Real-World Standards

Production systems use:
- **2048-bit primes** (617 decimal digits)
- **256-bit secret keys** (77 decimal digits)
- Estimated attack time: Billions of years

This implementation:
- **25-digit primes** (default, configurable)
- **10-digit secret keys**
- Estimated attack time: Seconds (intentionally weak)

## Usage

### Installation

No external libraries needed! Uses only Python built-in functions:


### Configuration

Adjust security level by changing the constant at the top of the file:
```python
PRIME_DIGITS = 25  # Change this value
```

**Options:**
- `25` digits: Fast (1-2 min), minimum requirement, **weak security**
- `50` digits: Moderate (2-5 min), better security
- `100` digits: Strong (5-15 min), excellent security

### Running the Program
```bash
python Diffie_Hellman_Key_Exchange.py
```

The program will:
1. Generate prime number p
2. Find primitive root g
3. Generate secret key a (private)
4. Compute public key A = g^a mod p
5. Wait for partner's public key B
6. Compute shared secret K
7. Encrypt your message
8. Display all values formatted for submission

### Example Output
```
======================================================================
DIFFIE-HELLMAN KEY EXCHANGE PROTOCOL
======================================================================

Configuration: 25-digit prime numbers
Generating a prime number with at least 25 digits...

✓ Prime found: 5960798427335641909088063
  Digits: 25

Finding primitive root of p...
✓ Primitive root found: g = 5

✓ Secret key a generated: 2024472989
  Digits: 10

YOUR PUBLIC VALUES (Share these):
p (hex): 4ee3f87bd5e2b5692cf3f
g (hex): 5
A (hex): 3008bb230063c832104c0
```

##  How It Works

### The Math Behind DH

1. **Alice generates:**
   - Prime p and generator g (public)
   - Secret key a (private)
   - Public key A = g^a mod p

2. **Bob generates:**
   - Same p and g (agreed upon)
   - Secret key b (private)
   - Public key B = g^b mod p

3. **Key Exchange:**
   - Alice computes: K = B^a mod p
   - Bob computes: K = A^b mod p
   - Both get the same K!

4. **The Magic:**
   - K = B^a = (g^b)^a = g^(ab) mod p
   - K = A^b = (g^a)^b = g^(ab) mod p
   - Same result, but secrets a and b never transmitted!

### Security

The security relies on the **Discrete Logarithm Problem (DLP)**:
- Given g, p, and A = g^a mod p
- Finding a is computationally hard for large primes
- With 25-digit primes: Solvable in seconds (weak!)
- With 2048-bit primes: Essentially impossible (strong!)

##  Learning Objectives

This project teaches:
-  Public-key cryptography fundamentals
-  Modular arithmetic in practice
-  The discrete logarithm problem
-  Importance of parameter sizing in cryptography
-  How to implement cryptographic protocols


##  Key Features

-  Miller-Rabin primality testing (40 rounds)
-  Primitive root finding
-  Cryptographically secure random number generation (CSPRNG)
-  Fast modular exponentiation (square-and-multiply)
-  XOR encryption with repeating key
-  Configurable security levels
-  Output formatting for easy submission
-  Built-in encryption verification

##  Security Analysis

### Parameter Size Impact

| Prime Size | Secret Size | Attack Time | Use Case |
|-----------|-------------|-------------|----------|
| 25 digits | 10 digits | ~10 seconds | Educational only |
| 50 digits | 10 digits | ~Minutes | Better learning |
| 100 digits | 10 digits | ~Hours | Demonstration |
| 617 digits (2048-bit) | 77 digits (256-bit) | Billions of years | Real-world use |


##  License

MIT License - See LICENSE file for details

This project is for educational purposes only.

##  Acknowledgments

Created as part of a cryptography course to understand:
- Mathematical foundations of public-key cryptography
- Practical implementation of DH protocol
- Security parameter selection



##  Additional Resources

- [Diffie-Hellman on Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [Khan Academy: Cryptography](https://www.khanacademy.org/computing/computer-science/cryptography)
- [Computerphile: Diffie-Hellman](https://www.youtube.com/watch?v=NmM9HA2MQGI)
- [NIST Standards](https://csrc.nist.gov/publications/detail/sp/800-56a/rev-3/final)

##  Future Improvements

Potential enhancements:
- [ ] Implement Elliptic Curve Diffie-Hellman (ECDH)
- [ ] Add Index Calculus attack implementation
- [ ] Benchmark different parameter sizes
- [ ] Create web interface
- [ ] Add support for safe primes (p = 2q + 1)
- [ ] Implement Schnorr groups

##  Contact

For questions or feedback, please open an issue on GitHub.

---

**Remember:** This is for educational purposes. Real-world applications should use established cryptographic libraries like `cryptography` or `PyCryptodome` with proper parameters!
