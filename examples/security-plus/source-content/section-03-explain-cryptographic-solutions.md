# Section 3: Explain Cryptographic Solutions

_Domain D1 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 3.1 Introduction To Cryptography And Hashing
- 3.2 Encryption
- 3.3 Cryptographic Modes Of Operation & Cipher Suites
- 3.4 Cryptographic Use Cases
- 3.5 Longevity, Salting, Stretching & Other Cryptographic Technologies
- 3.6 Certificates, PKIs, RAs & CSRs
- 3.7 Digital Certificates
- 3.8 Key Management
- 3.9 Certificate Management

## Content

```
SECTION 3 -
EXPLAIN CRYPTOGRAPHIC
SOLUTIONS

  3.1 Introduction To Cryptography And Hashing

Cryptography is a secure communication Technique that allows only the
Sender and Receiver of a Message to view it.
Plaintext - An Unencrypted Message
Ciphertext - An Encrypted Message
Cipher - The Process (Algorithm) Used to Encrypt and Decrypt a Message
Cryptanalysis - The Art of Cracking Cryptographic Systems


There Are Three Main Types Of Cryptographic Algorithms:
 Hashing Algorithms
 Symmetric Encryption Cipher
 Asymmetric Encryption Cipher
Hashing Algorithms - the simplest type of cryptographic operation and
produces a fixed length string from an input plaintext that can be of any
length. A hashing collision occurs when two different plain texts produce the
exact same hash value. encryption algorithms must demonstrate collision
avoidance.




                                                                                21
Hashing Algorithms
 Secure Hash Algorithm (Sha) - Considered to be the Strongest Algorithm
  with the most Popular Being The Sha-256 which produces A 256-Bit
  Digest.
 Message Direct Algorithm #5 (Md5) - produces A 128-Bit Digest
Birthday Attack - a brute force attack aimed at exploiting collisions in hash
functions. could be used for forging a digital signature




  3.2 Encryption

An encryption algorithm is a type of cryptographic process that encodes data so that it can
be recovered or decrypted.
The use of a key, with the encryption cipher ensures that decryption can only be performed
by authorized persons.
A substitution cipher involves replacing units in the plain text with different cipher text. e.g
rot13 rotates each letter 13 places so a becomes n
The cipher text “uryyb jbeyq” means “hello world”




                                                                                                   22
In contrast to substitution ciphers, the units in a transposition cipher stay the same in plain
text and cipher text but their order is changed according to some mechanism.
Consider the cipher text “hloolelwrd”
hlool
elwrd
The letters are simply written as columns and the rows are concatenated.
Symmetric Encryption - here both encryption and decryption are performed by the same
secret key and can be used for confidentiality. It is very ast and is used or bulk encryption
of large amounts of data but can be vulnerable if the key is stolen.




There are two types - Stream ciphers & block ciphers
Stream cipher - The plaintext is combined with a separate randomly generated message
calculated from the key and an initialization vector (iv). each byte or bit of data is encrypted
one at a time.
Block cipher - The plaintext is divided into equal-size blocks (usually 128-bit). if there is not
enough data in the plaintext, it is padded to the correct size. e.g, a 1200-bit plaintext would
be padded with an extra 80 bits to fit into 10 x 128-bit blocks.
Asymmetric Encryption - Here both encryption and decryption are performed by two
different but related public and private keys in a key pair. Each key is capable of reversing
the operation of its pair and they are linked in such a way as to make it impossible to derive
one from the other.



                                                                                                    23
Can be used to Prove Identity as the holder of the Private Key
Cannot be Impersonated by anyone Else.
The Major Drawback of this Encryption is that it Involves
Substantial Computing Resources.
Mostly Used for Authentication and Non-Repudiation and for
Key Agreement and Exchange.
Asymmetric Encryption is often referred to as Public Key
Cryptography and the Products are Based on The Rsa
Algorithm.
Ron Rivest, Adi Shamir and Leonard Adleman Published The
RSA cipher In 1977.




                                                                 24
  3.3 Cryptographic Modes Of Operation & Cipher Suites

A mode of operation is a means of using a cipher within a product to achieve a security
goal such as confidentiality or integrity.
Public Key Cryptography can authenticate a Sender while Hashing can Prove Integrity.
Both can be combined to authenticate a sender and prove the integrity of a message and
this usage is called a digital signature.
Symmetric encryption can encrypt and decrypt large amounts of data but it's difficult to
distribute the secret key securely.
Asymmetric (pkc) encryption can distribute the key easily but cannot be used for large
amounts of data.
Digital Certificates - public keys are used and are freely available but how can anyone trust
the identity of the person or server issuing a public key
A third party known as a certificate authority (ca) can validate the owner of the public key
by issuing the subject with a certificate.
The Process of Issuing and Verifying Certificates Is Called Public Key Infrastructure (Pki)
Cipher Suite - This is the combination of ciphers supported and is made Up of
 Signature Algorithm - Used to Assert the Identity of The Server’s Public Key and
  Facilitate Authentication
 Key Exchange/Agreement Algorithm - Used by the Client and Server to Derive The
  Same Bulk Encryption Symmetric Key.




                                                                                                25
  3.4 Cryptographic Use Cases

Cryptography supporting authentication & non-repudiation - a single hash function,
symmetric or asymmetric cipher is called a cryptographic primitive. a complete cryptographic
system or product is likely to use multiple cryptographic primitives such as within a cipher
suite.
Authentication & non-repudiation depend on the recipient not being able to encrypt the
message or the recipient would be able to impersonate the sender. Basically the recipient
must be able to use the cryptographic process to decrypt authentication and integrity data
but not to encrypt it.
Cryptography supporting confidentiality - cryptography removes the need to store data
in secure media as even if the cipher text is stolen, the threat actor will not be able to
understand or change what has been stolen.
Cryptography supporting integrity & resiliency - integrity is proved by hashing algorithms
which allow two parties to derive the same checksum and show that a message or data
has not been tampered with. Cryptography can be used to design highly resilient control
systems and secure computer code.
A developer can make tampering more difficult through obfuscation which is the art
of making a message difficult to understand. Cryptography is a very effective way of
obfuscating code but it also means the computer might not be able to understand and
execute the code.




                                                                                               26
  3.5 Longevity, Salting , Stretching & Other Types Of
      Cryptographic Technologies

Longevity - This Refers to the Measure of Confidence That People have in a Given Cipher. In
Another Sense, it is the Consideration of how Long data must be kept secure.
Salting - passwords stored as hashes are vulnerable to brute force and dictionary attacks. a
password hash cannot be decrypted as they are one-way. however, an attacker can
generate hashes to try and find a match for the captured password hash through a brute
force or dictionary attack.
A Brute Force Attack Will Run Through a Combination of Letters, Numbers and Symbols
while a Dictionary Attack Creates Hashes of Common Words and Phrases.


Both Attacks can be Slowed Down by Adding a Salt Value when Creating
the Hash.
(Salt + Password) * Sha = Hash
The salt is not kept secret because any system verifying the hash must know the value of
the salt but it's presence means that an attacker cannot use pre-computed tables of hashes.
Key Stretching - this takes a key that's generated from a user password plus a random salt
value and repeatedly converts it to a longer and more random key. this means the attacker
will have to do extra processing for each possible key value thus make the attack even
slower.
This can be performed by using a particular software library to hash and save passwords
when they are created. the password-based key derivation function 2 (pbkdf2) is widely
used for this purpose.
Homomorphic Encryption - This Is The Conversion of Data Into Cipher text that can be
analyzed and Worked with As If It Were Still In Its Original Form.
It enables Complex Mathematical Operations to be Performed on encrypted data without
Compromising The Encryption.
Blockchain - This is a concept in which an expanding list of transactional records is secured
using cryptography. Each record is referred to as a block and is run through a hash function.
The hash value of the previous block in the chain is added to the hash calculation of the next
block and thus ensures that each successive block is cryptographically linked.
Steganography - This is a technique for obscuring the presence of a message such as
hiding a message in a picture. the container document or file is called the cover text.




                                                                                                 27
  3.6 Certificates, Pkis, Ras & Csrs

Public & Private Key Usage
When you want others to send you confidential messages, you give them your public key to
encrypt the message and then you decrypt the message with your private key.
When You Want To Authenticate Yourself To Others, you create a Signature and Sign
It Using Your Private Key To Encrypt It. You give others your Public Key to Decrypt the
Signature.
Certificate Authority - This is the Entity Responsible for Issuing and Guaranteeing
Certificates.


Pki Trust Models Include:
 Single CA - A Single CA issues certificates to Users and the Users Trust Certificates by
  that CA exclusively. If the CA Is Compromised, the Entire Pki Collapses
 Hierarchical (Intermediate Ca) - A single CA called the root issues certificates to several
  intermediate CAs. The intermediate CAs issue certificates to subjects (leaf or end
  entities). Each leaf certificate can be traced back to the root ca along the certification
  path and this is referred to as a certificate chain or chain of trust. the root is still a single
  point of failure but it can be taken off-line as most of the regular CA activities are
  handled by the intermediate CA servers.



                                                                                                      28
   Online Versus Offline Cas - An online CA is one that is available to accept and process
   certificate signing requests and management tasks. Because of the high risk posed by
   a compromised root CA, a secure configuration will involve making the root an off-line
   CA meaning it is disconnected from any network and only brought back on line to add
   or update intermediate CAs.
Registration authorities and CSRS - registration is the process by which end users create
an account with the CA and become authorized to request certificates.
When a subject Wants to Obtain a Certificate, It Completes a Certificate Signing Request
(CSR) and Submits It to the CA.
The CA Reviews The Certificate and checks that the Information is Valid. If the Request Is
accepted, The CA Signs the Certificate and Sends It to the Subject.




                                                                                              29
  3.7 Digital Certificates

A Digital Certificate is essentially a Wrapper for a Subject’s Public Key. As well as the
Public Key, It Contains Information about The Subject and the Certificate’s Issuer.


                                                    Field                      Usage
                                                                A number uniquely identifying the
                                          Serial number         certificate within the domain of its
                                                                CA.
                                                                The algorithm used by the CA to sign
                                          Signature algorithm
                                                                the certificate.

                                          Issuer                The name of the CA.

                                                                Date and time during which the
                                          Valid from/to
                                                                certificate is valid.
                                                                The name of the certificate holder,
                                                                expressed as a distinguished name
                                                                (DN). Within this, the common name
                                          Subject               (CN) part should usually match either
                                                                the fully qualified domain name
                                                                (FQDN) of the server or a user email
                                                                address.
                                                                Public key and algorithm used by the
                                          Public key
                                                                certificate holder.
                                                                V3 certificates can be defined with
                                                                extended attributes, such as friendly
When Certificates Were First              Extensions            subject or issuer names, contact
Introduced, The Common Name                                     email addresses, and intended key
(CN) Attribute was Used to Identify                             usage.
The FQDN by Which The Server is                                 This extension field is the preferred
Accessed.                                 Subject alternative   mechanism to identify the DNS
                                          name (SAN)            name or names by which a host is
The Subject Alternative Name                                    identified.
(SAN) Extension Field is
Structured to Represent Different
Types of Identifiers Including
Domain Names.
A Wildcard Domain Such as
*.Comptia.Org means that the
Certificate Issued to the Parent
Domain Will be accepted as Valid
for all Subdomains.




                                                                                                        30
Eku Field - Can Have The Following Values
 Server Authentication
 Client Authentication
 Code Signing
 Email Protection


Web Server Certificate Types Include:
 Domain Validation (Dv) - Proves The Ownership Of A Particular Domain
 Extended Validation (Ev) - Subjecting To A Process That Requires More Rigorous Checks
  On The Subject’s Legal Identity And Control Over The Domain.


Other Certificate Types Include:
 Machine/Computer Certificates
 Email/User Certificates
 Code Signing Certificates
 Root Certificate
 Self-Signed Certificates




  3.8 Key Management

This Refers To Operational Considerations For The Various Stages In A Key’s Life Cycle And
Can Be Centralized Meaning One Admin Controls The Process Or Decentralized In Which
Each User Is Responsible For His Or Her Keys.


Key Life Cycle

        Key Generation                                Revocation
        Certificate Generation                        Expiration And Renewal
        Storage




                                                                                             31
If the key used to decrypt data is lost or damaged, encrypted data cannot be recovered
unless a backup of the key exists. however making too many backups can make it more
difficult to keep the key secure.
Escrow means that something is held independently which in terms of key management,
means a third party is trusted to store the key securely.




  3.9 Certificate Management

When you are renewing a certificate, it is possible to use the existing key referred to
specifically as key renewal or generate a new key in which case, the certificate is rekeyed.

Certificates are issued with a limited duration set by the ca policy for the certificate type e.g
a root certificate might have a 10 year expiry date while a web server certificate might be
issued for 1 year only.

A certificate may be revoked or suspended. a revoked certificate is no longer valid and
cannot be reinstated while a suspended certificate can be re-enabled. A certificate may be
revoked or suspended for a variety of reasons such as the private key compromise,
business closure or a user leaving the company. These reasons are codified under


 Unspecified
 Key Compromise
 Ca Compromise
 Superseded
 Cessation Of Operation
A suspended Key is given the Code Certificate Hold




                                                                                                    32
```
