import streamlit as st
import random
from math import gcd

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def find_e(phi):
    e = 65537
    if gcd(e, phi) == 1:
        return e
    for candidate in range(3, phi, 2):  
        if gcd(candidate, phi) == 1:
            return candidate

def RSA(a, b):
    primes = [i for i in range(a, b) if is_prime(i)]
    if len(primes) < 2: 
        return None

    p = random.choice(primes)
    q = random.choice(primes)
    while q == p:
        q = random.choice(primes)

    phi = (p-1)*(q-1)
    e = find_e(phi)
    d = pow(e, -1, phi)
    n = p * q

    return {
        "p": p,
        "q": q,
        "phi": phi,
        "e": e,
        "d": d,
        "n": n
    }

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(ciphertext, d, n):
    return ''.join(chr(pow(c, d, n)) for c in ciphertext)


st.set_page_config(
   page_title="RSA-kryptering",
   layout="wide",
   initial_sidebar_state="expanded",
)

st.title("RSA-kryptering")
st.header("Interaktiv RSA-implementering")

st.write(
    """
    Denne app genererer RSA-nøgler baseret på to input (laveste og højeste tal for primtal), 
    og viser hvordan nøgleparametrene er relateret.
    """
)

with st.sidebar:
    st.header("Indstillinger")
    lower_bound = st.number_input("Laveste tal (minimum 100)", min_value=10, max_value=100000, value=1000, step=1)
    upper_bound = st.number_input("Højeste tal (maksimum 100000)", min_value=lower_bound+1, max_value=100000, value=5000, step=1)

message = st.text_input("Indtast en besked til kryptering", "Ahvabehar")

if lower_bound >= upper_bound:
    st.error("Laveste tal skal være mindre end højeste tal!")
else:
    if st.button("Generer nøgler og krypter"):
        keys = RSA(lower_bound, upper_bound)
        if keys is None:
            st.error("Kunne ikke finde to primtal i det givne interval. Prøv et andet interval.")
        else:
            st.subheader("Genererede nøgler")
            st.write(f"Primtal p = **{keys['p']}**")
            st.write(f"Primtal q = **{keys['q']}**")
            st.write(f"n = p • q = **{keys['n']}**")
            st.write(f"Euler's totient φ(n) = (p-1) • (q-1) = **{keys['phi']}**")
            st.write(f"Public exponent e = **{keys['e']}**")
            st.write(f"Private exponent d (modular invers af e mod φ) = **{keys['d']}**")

            st.markdown("---")
            st.subheader("Matematiske formler og nøglerelationer")

            st.latex(r"""
            \begin{cases}
            n = p \cdot q \\
            \varphi(n) = (p-1)(q-1) \\
            \text{Find } e \text{ således at } 1 < e < \varphi(n) \text{ og } \gcd(e, \varphi(n)) = 1 \\
            d \equiv e^{-1} \pmod{\varphi(n)}
            \end{cases}
            """)

            st.markdown("---")
            st.subheader("Kryptering og dekryptering")

            st.latex(r"""
            c \equiv m^e \pmod{n}
            """)

            st.latex(r"""
            m \equiv c^d \pmod{n}
            """)

            cipher = encrypt(message, keys['e'], keys['n'])
            st.write("Krypteret besked (tallene):")
            st.write(cipher)

            decrypted = decrypt(cipher, keys['d'], keys['n'])
            st.write("Dekrypteret besked:")
            st.write(decrypted)
