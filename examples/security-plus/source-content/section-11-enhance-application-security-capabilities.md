# Section 11: Enhance Application Security Capabilities

_Domain D4 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 11.1 DNS Security, Directory Services & SNMP
- 11.2 Secure Application Operations Protocols
- 11.3 File Transfer, Email & Video Services
- 11.4 Email Security
- 11.5 Secure Coding Techniques

## Content

```
SECTION 11
ENHANCE APPLICATION
SECURITY CAPABILITIES




  11.1 DNS Security, Directory Services & Snmp

DNS Security - to ensure dns security on a private network, local DNS servers should
only accept recursive queries from local authenticated hosts and not from the internet.
Clients should be restricted to using authorized resolvers to perform name resolution.
DNS footprinting means obtaining information about a private network by using its
DNS server to perform a zone transfer (all the records in a domain) to a rogue DNS.
Security Extensions (DNSSEC) - These Help to Mitigate against spoofing And
Poisoning Attacks by Providing a Validation Process For DNS responses.
Secure Directory Services - a network directory lists the subjects (users, computers and
services) and objects (directories and files) available on the network plus the permissions
subjects have over objects.

Most Directory Services Are Based on The Lightweight Directory
Access Protocol (LDAP) Running over Port 389.




                                                                                              111
Authentication Referred To As Binding To The Server Can Be Implemented By:
 No Authentication - Anonymous Access Is Granted
 Simple Bind - The Client Must Supply Its Distinguished Name And Password In Plaintext
 Simple Authentication And Security Layer (Sasl) - The Client And Server Negotiate The
  Use Of A Supported Authentication Mechanism Such As Kerberos.
 Ldap Secure (Ldaps) - The Server Is Installed With A Digital Certificate Which It Uses To
  Setup A Secure Tunnel For The User Credential Exchange. Ldaps Use Port 636.
Generally Two Levels Of Access To The Directory Can Be Granted Which Are Read-Only
Access (Query) And Read/Write Access (Update) And Is Implemented Using An Access
Control Policy.
Time Synchronization - Many Network Applications Are Time Dependent And Time Critical.
The Network Time Protocol (Ntp) Provides A Transport Over Which To Synchronize These
Time Dependent Applications
Ntp Works Over Udp On Port 123.




    NTP has Historically Lacked Any Sort Of Security Mechanism but There Are
    Moves to Create a Security Extension For the Protocol Called Network Time
    Security.
    Simple Network Management Protocol (SNMP) Security - This Is a Widely used
    Framework For Management And Monitoring And Consists of an SNMP Monitor
    and Agents. The agent is a Process (Software Or Firmware) running on a Switch,
    Router, Server or other SNMP-Compatible network device.
    This Agent Maintains a Database Called a Management Information Base (MIB)
    that Holds Statistics Relating to The activity Of the Device. The Agent Is also
    Capable Of Initiating a Trap Operation Where It Informs The Management System
    Of a Notable Event Like port failure.




  11.2 Secure Application Operations Protocols

HTTP enables clients to request resources from an HTTP server. The server acknowledges
the request and responds with the data or an error message.
HTTP is a stateless protocol which means the server preserves no information about the
client during a session.




                                                                                              112
Transport Layer Security - Secure Sockets Layer (SSL) was developed by Netscape in the
1990s to address the lack of security in HTTP and was quickly adopted as a standard named
Transport Layer Security (TLS).
To implement TLS, a server is assigned a digital certificate signed by some trusted CA. The
certificate proves the identity of the server and validates the server’s public/private key pair.
The server uses its key pair and the TLS protocol to agree mutually supported ciphers with
the client and negotiate an encrypted communications session.
SSL/TLS Version - A server can provide support for legacy clients meaning a TLS 1.2 server
could be configured to allow clients to downgrade to TLS 1.1 or 1.0
TLS 1.3 was approved in 2018 and the ability to perform downgrade attacks was mitigated by
preventing the use of unsecure features and algorithms from previous versions.
Cipher Suites - This is a set of algorithms supported by both the client and server to perform
the different encryption and hashing operations required by the protocol.
Prior to TLS 1.3, a cipher suite would be written like this




      ECDHE-RSA-AES128-GCM-SHA256
      This means that the server can use Elliptic Curve Diffie-Hellman Ephemeral mode
      for a session key agreement, RSA signatures, 128-bit AES-GCM (Galois Counter
      Mode) for symmetric bulk encryption and 256-bit SHA for HMAC functions.
      TLS 1.3 uses simplified and shortened suites

      TLS_AES_256_GCM_SHA384
      Only ephemeral key agreement is supported in 1.3 and the signature type is
      supplied in the certificate so the cipher suite only lists the bulk encryption key
      strength and mode of operation (AES_256_GCM) plus the cryptographic hash
      algorithm (SHA384).




  11.3 File Transfer, Email & Video Services

FTP - File Transfer Protocol is the most popular protocol for transferring files across
networks because it is very efficient and has wide cross-platform support but has no security
mechanism.



                                                                                                    113
SSH FTP (SFTP) & FTP over SSL (FTPS) - SFTP addresses the lack of security by encrypting
the authentication and data transfer between client and server. SFTP uses port 22.
Explicit TLS (FTPES) - Use the AUTH TLS command to upgrade and insecure connection
established on port 21 to a secure one.
Implicit TLS (FTPS) - Negotiates an SSL/TLS tunnel before the exchange of any FTP
commands. This mode uses the secure port 990 for the control connection.


Email Services: These use two types of protocols:
 The Simple Mail Transfer Protocol (SMTP) which specifies how mail is sent from one
  system to another.
 A mailbox protocol stores messages for users and allows them to download them to
  client computers or manage them on the server.


Secure SMTP (SMTPS) - communications can be secured using TLS and
there are two ways to do this:
 STARTTLS - This command will upgrade an existing unsecure connection to use TLS.
  Also referred to as explicit TLC or opportunistic TLS.
 SMTPS - This establishes the secure connection before any SMTP commands are
  exchanged. Also referred to as implicit TLS.




Typical SMTP configurations use the following ports and secure services:
 Port 25 - Used for message relay between SMTP servers or Message
  Transfer Agents (MTA)
 Port 587 - Used by mail clients to submit messages for delivery by an
  SMTP server
 Port 465 - Some providers and mail clients use this port for message
  submission over implicit TLS (SMTPS)
Secure POP (POP3S) - The Post Office Protocol v3 is a mailbox protocol
designed to store the messages delivered by SMTP on a server.




                                                                                           114
Secure IMAP (IMAPS) - The Internet Message Access Protocol v4 (IMAP4) supports
permanent connections to a server and connecting multiple clients to the same mailbox
simultaneously.
Secure/Multipurpose Internet Mail Extensions (S/MIME) - Is a means of applying both
authentication and confidentiality on a per-message basis.



  11.4 Email Security

Sender Policy Framework (SPF) - Is an email authentication method that helps detect and
prevent sender address forgery commonly used in phishing and spam emails.
SPF works by verifying the sender’s IP address against a list of authorized sending IP
addresses published in the DNS TXT records of the email sender’s domain.
DomainKeys Identified Mail (DKIM) - Leverages encryption features to enable email
verification by allowing the sender to sign emails using a digital signature, The receiving
email server uses a DKIM record in the sender’s DNS record to verify the signature and the
email’s integrity.
Domain-based Message Authentication, Reporting & Conformance (DMARC) - Uses the
results of SPF and DKIM checks to define rules for handling messages, such as moving
messages to quarantine or spam, rejecting them outright or tagging the message.
An email gateway - Is the control point for all incoming and outgoing email traffic. It acts as
a gatekeeper, scrutinizing all emails to remove potential threats before they reach inboxes.
Email gateways utilize several security measures, including anti-spam filters, antivirus
scanners, and sophisticated threat detection algorithms to identify phishing attempts,
malicious URLs, and harmful attachments.




                                                                                                  115
The combined use of SPF, DKIM, and DMARC significantly enhances email security
by making it much more difficult for attackers to impersonate trusted domains,
which is one of the most common tactics used in phishing and spam attacks.




                                                                                 116
  11.5 Secure Coding Techniques

Input Validation - malicious input could be crafted to perform an overflow attack or some
type of script or SQL injection attack. To mitigate this, there should be routines to check user
input and anything that does not conform to what is required must be rejected.

Normalization and Output Encoding - normalization means that a string is stripped of illegal
characters or substrings and converted to the accepted character set. this ensures that the
string is in a format that can be processed correctly by the input validation routines.

Output encoding means that a string is re-encoded safely for the context in which it is being
used.

Server-side versus Client-side Validation - a web application can be designed to perform
code execution and input validation locally (on the client) or remotely (on the server). The
main issue with client-side validation is that the client will always be more vulnerable to
some sort of malware interfering with the validation process.

Main issue with server-side validation is that it can be time-consuming as it may involve
multiple transactions between the server and client. Client-side validation is usually
restricted to informing the user that there is some sort of problem with the input before
submitting it to the server. relying on client-side validation only is poor programming
practice.

Web Application Security In Response Headers
A Number Of Security Options Can Be Set In The Response Header

 Http Strict Transport (HST) - Forces Browser to Connect Using HTTPS Only, Mitigating
  Downgrade Attacks Such as SSL Stripping.
 Content Security Policy (CSP) - Mitigates Clickjacking, Script Injection And Other Client-
  Side Attacks.
 Cache Control - Sets Whether The Browser can Cache Responses. Preventing Caching
  Of Data Protects Confidential And Personal Information Where The Client Device Might
  Be Shared By Multiple Users.
Data Exposure And Memory Management - Data Exposure is a Fault that allows
Privileged Information such as a Password or Personal Data to be Read without being
Subject to the appropriate access controls.
A Well-Written application must be able to Handle Errors and Exceptions Gracefully. Ideally
the Programmer should have Written a Structured Exception Handler (SEH) to dictate what
the application should then do.



                                                                                                   117
The Error Must Not Reveal Any Platform Information Or Inner Workings Of The Code To An
Attacker.
Secure Code Usage - A Program May Make Use Of Existing Code In The Following Ways:
 Code Reuse - using a block of code from elsewhere in the same application or from
  another application to perform a different function.
 Third-Party Library - using a binary package (such as a dynamic link library) that
  implements some sort of standard functionality such as establishing a network
  connection.
 Software Development Kit (SDK) - using sample code or libraries of pre-built functions
  from the programming environment used to create the software.
 Stored Procedures - Using a Pre-Built Function to Perform a database query.




Unreachable code and dead code
Unreachable code is a part of application source code that can never be executed (if ... then
conditional logic that is never called because the conditions are never met).
Dead code is executed but has no effect on the program flow (a calculation is performed but
the result is never stored as a variable or used to evaluate a condition).
Static code analysis - this is performed against the application code before it is packaged
as an executable process. The software will scan the source code for signatures of known
issues.
Human analysis of software source code is described as a manual code review. It is
important that the code be reviewed by developers other than the original coders to try to
identify oversights, mistaken assumptions or a lack of experience.
Dynamic code analysis - static code review will not reveal any vulnerabilities that exist in the
runtime environment. dynamic analysis means that the application is tested under real world
conditions using a staging environment.
Fuzzing is a means of testing that an application‘s input validation routines work well.
fuzzing will deliberately generate large amounts of invalid or random data and record the
responses made by the application.
Associated with fuzzing is the concept of stress testing an application to see how an
application performs under extreme performance or usage scenarios.
Finally, the fuzzer needs some means of detecting an application crash and recording which
input sequence generated the crash.




                                                                                                   118
```
