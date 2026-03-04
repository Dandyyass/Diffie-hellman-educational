"""
Diffie-Hellman Key Exchange - Complete Implementation

Generates all values from scratch: p, g, a, A
Then computes shared key K and encrypts message

Configuration: Adjust PRIME_DIGITS for security level
- 25 digits: Minimum (exam requirement, weak security)
- 50 digits: Moderate (better security)
- 100 digits: Strong (excellent security, takes longer)
"""

import secrets

PRIME_DIGITS = 25  # Change this to 50 or 100 for stronger security


# PRIME NUMBER GENERATION AND VERIFICATION


def miller_rabin(n, k=40):
    """Miller-Rabin primality test with k rounds of testing"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    for _ in range(k):
        a = secrets.randbelow(n - 3) + 2
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True


def generate_large_prime(min_digits):
    """Generate a prime number with at least min_digits digits"""
    min_value = 10 ** (min_digits - 1)
    max_value = 10 ** min_digits
    
    print(f"Generating a prime number with at least {min_digits} digits...")
    print("This may take a moment...\n")
    
    while True:
        candidate = secrets.randbelow(max_value - min_value) + min_value
        if candidate % 2 == 0:
            candidate += 1
        
        if miller_rabin(candidate):
            print(f" Prime found: {candidate}")
            print(f"  Digits: {len(str(candidate))}")
            return candidate



# FIND PRIMITIVE ROOT


def prime_factors(n):
    """Returns the set of prime factors of n"""
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return factors


def find_primitive_root(p):
    """Find a primitive root modulo p"""
    print(f"\nFinding primitive root of p...")
    
    if p == 2:
        return 1
    
    phi = p - 1
    factors = prime_factors(phi)
    
    print(f"  Prime factors of (p-1): {factors}")
    
    for g in range(2, p):
        is_primitive = True
        
        for factor in factors:
            if pow(g, phi // factor, p) == 1:
                is_primitive = False
                break
        
        if is_primitive:
            print(f" Primitive root found: g = {g}")
            return g
    
    return 2



# KEY GENERATION


def generate_secret_key(min_digits=10):
    """Generate a secret key with at least min_digits digits"""
    min_value = 10 ** (min_digits - 1)
    max_value = 10 ** min_digits
    
    secret_key = secrets.randbelow(max_value - min_value) + min_value
    print(f"\n Secret key a generated: {secret_key}")
    print(f"  Digits: {len(str(secret_key))}")
    return secret_key


def compute_public_key(g, a, p):
    """Compute public key A = g^a mod p"""
    A = pow(g, a, p)
    print(f" Public key A = g^a mod p computed")
    return A



# SHARED KEY AND ENCRYPTION


def compute_shared_key(B, a, p):
    """Compute shared key s = B^a mod p"""
    shared_key = pow(B, a, p)
    print(f"\n Shared key s = B^a mod p computed")
    return shared_key


def extract_last_80_bits(shared_key):
    """Extract the last 80 bits of the shared key"""
    shared_key_hex = hex(shared_key)[2:]
    K_hex = shared_key_hex[-20:].zfill(20)
    
    print(f" K (last 80 bits) extracted: {K_hex}")
    return K_hex


def encrypt_message(message, K_hex):
    """Encrypt message using XOR with repeating key K"""
    message_bytes = [ord(c) for c in message]
    K_bytes = [int(K_hex[i:i+2], 16) for i in range(0, len(K_hex), 2)]
    
    cipher_bytes = [message_bytes[i] ^ K_bytes[i % len(K_bytes)] 
                    for i in range(len(message_bytes))]
    
    cipher_hex = ''.join(f'{b:02x}' for b in cipher_bytes)
    
    print(f" Message encrypted")
    print(f"  Plaintext: {message}")
    print(f"  Ciphertext (hex): {cipher_hex}")
    
    return cipher_hex


def format_ciphertext_bytes(cipher_hex):
    """Format ciphertext as space-separated bytes (00-FF)"""
    cipher_bytes = [cipher_hex[i:i+2] for i in range(0, len(cipher_hex), 2)]
    return ' '.join(cipher_bytes).upper()



# MAIN PROGRAM


def main():
    print("="*70)
    print("DIFFIE-HELLMAN KEY EXCHANGE PROTOCOL")
    print("="*70)
    print(f"\nConfiguration: {PRIME_DIGITS}-digit prime numbers")
    
    # Step 1 & 2: Generate and verify prime
    p = generate_large_prime(min_digits=PRIME_DIGITS)
    p_hex = hex(p)[2:]
    
    # Step 3: Find primitive root
    g = find_primitive_root(p)
    g_hex = hex(g)[2:]
    
    # Step 4 & 5: Generate secret and public keys
    a = generate_secret_key(min_digits=10)
    A = compute_public_key(g, a, p)
    A_hex = hex(A)[2:]
    
    print("\n" + "="*70)
    print("YOUR PUBLIC VALUES (Share these with Bob):")
    print("="*70)
    print(f"p (hex): {p_hex}")
    print(f"g (hex): {g_hex}")
    print(f"A (hex): {A_hex}")
    
    # Step 6: Get Bob's public key
    print("\n" + "="*70)
    print("WAITING FOR BOB'S PUBLIC KEY")
    print("="*70)
    B_hex = input("Enter Bob's public key B (in hexadecimal): ").strip().replace("0x", "")
    B = int(B_hex, 16)
    
    # Step 7: Compute shared key
    shared_key = compute_shared_key(B, a, p)
    shared_key_hex = hex(shared_key)[2:]
    
    # Step 8: Extract last 80 bits as K
    K_hex = extract_last_80_bits(shared_key)
    
    # Step 9: Encrypt message
    print("\n" + "="*70)
    print("MESSAGE ENCRYPTION")
    print("="*70)
    message = input("Enter your message (at least 16 characters): ")
    
    while len(message) < 16:
        print("Message must be at least 16 characters!")
        message = input("Enter your message (at least 16 characters): ")
    
    cipher_hex = encrypt_message(message, K_hex)
    cipher_formatted = format_ciphertext_bytes(cipher_hex)
    
    # Display results
    print("\n" + "="*70)
    print("RESULTS - COPY THESE TO EXCEL")
    print("="*70)
    print(f"\np (hex):        {p_hex}")
    print(f"g (decimal):    {g}")
    print(f"A (hex):        {A_hex}")
    print(f"B (hex):        {B_hex}")
    print(f"K (hex):        {K_hex}")
    print(f"\nCiphertext (byte format for Excel):")
    print(f"{cipher_formatted}")
    
    # Verification
    print("\n" + "="*70)
    print("VERIFICATION")
    print("="*70)
    
    K_bytes = [int(K_hex[i:i+2], 16) for i in range(0, len(K_hex), 2)]
    cipher_bytes = [int(cipher_hex[i:i+2], 16) for i in range(0, len(cipher_hex), 2)]
    decrypted_bytes = [cipher_bytes[i] ^ K_bytes[i % len(K_bytes)] 
                       for i in range(len(cipher_bytes))]
    decrypted_message = ''.join(chr(b) for b in decrypted_bytes)
    
    print(f" Prime p: {len(str(p))} digits")
    print(f" Secret key a: {len(str(a))} digits")
    print(f" Message length: {len(message)} characters")
    
    print(f"\n Decryption test:")
    print(f"  Original:  {message}")
    print(f"  Decrypted: {decrypted_message}")
    
    if message == decrypted_message:
        print("\n SUCCESS! Encryption/decryption verified!")
    else:
        print("\n ERROR: Decryption doesn't match!")
    
    print("\n" + "="*70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\n ERROR: {e}")
        print("\nPlease check your input values and try again.")