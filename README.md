In Progress...


We offer a simple way to encrypt data. We have 3 different ways of doing this.<br />

Fernet - Cryptographys algorithm that contains "symmetric ciphers, message digests, and key derivation functions" (pypi.org), this is pretty basic encryption.<br />
AES256 - It is the "current encryption standard" (idera.com), it can slow down slower processors but should be fine on most systems.<br />
Public Key - It uses a pair of keys (public and private) to encrypt data. It encrypts the data with the public key, but the data can only be unencrypted with the private key.<br />
SHA - Secure Hash Algorithm, used for cryptographic security. Cryptographic hash algorithms produce irreversible and unique hashes. The larger the number of possible hashes, the smaller the chance that two values will create the same hash. The higher number sha means more unique hashes.<br />
Custom - A custom Ascii scrambler that I made. It is not the most secure so I wouldn't recommend using it alone, but using it in combination with some other methods provided by this package removes the possibility of the same thing being created. **WARNING** This cannot be used in combination with SHA hashing because of the checking methods.<br /><br />

This is a very simple library that I made for one of my projects, so there might be bugs please report these in the github issues. Although it might be simple it is pretty powerful.<br />

**WARNING** Don't delete the .key files or you cant unencrypt the data that you have encrypted with that key.<br />

# Information

[![Python](https://img.shields.io/pypi/pyversions/easyencryption.svg)](https://pypi.python.org/pypi/easyencryption)
[![PyPi](https://img.shields.io/pypi/v/easyencryption.svg)](https://pypi.org/project/easyencryption)

# Downloads

[![Downloads](https://pepy.tech/badge/easyencryption)](https://pepy.tech/project/easyencryption)
[![Downloads](https://pepy.tech/badge/easyencryption/month)](https://pepy.tech/project/easyencryption)
[![Downloads](https://pepy.tech/badge/easyencryption/week)(https://pepy.tech/project/easyencryption)