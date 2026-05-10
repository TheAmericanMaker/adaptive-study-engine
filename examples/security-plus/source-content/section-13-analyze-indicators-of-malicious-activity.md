# Section 13: Analyze Indicators of Malicious Activity

_Domain D2 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 13.1 Malware Classification
- 13.2 Computer Viruses
- 13.3 Computer Worms & Fileless Malware
- 13.4 Spyware, Keyloggers, Rootkits, Backdoors, Ransomware & Logic Bombs
- 13.5 Malware Indicators & Process Analysis
- 13.6 Password Attacks
- 13.7 Tactics, Techniques & Procedures
- 13.8 Privilege Escalation & Error Handling
- 13.9 Uniform Resource Locator Analysis & Percent Encoding
- 13.10 API & Replay Attacks, CSRF, Clickjacking & SSL Strip Attacks
- 13.11 Injection Attacks

## Content

```
SECTION 13 -
ANALYZE INDICATORS OF
MALICIOUS ACTIVITY
    13.1 Malware Classification

Some malware classifications such as Trojan, virus and worm focus on the vector
used by the malware. the vector is the method by which the malware executes on a
computer and potentially spreads to other network hosts.


The Following Categories Describe Some Types Of Malware According
To Vector:
 Viruses & Worms - spread without any authorization from the user by being
  concealed within the executable code of another process.
 Trojan - Malware Concealed within an Installer Package for Software that Appears to
  be Legitimate
 Potentially Unwanted Programs/Applications (Pups/Puas) - These are software
  installed alongside a package selected by the user. unlike a Trojan, their presence
  isn’t necessarily malicious. they are sometimes referred to as grayware.


Other Classifications are Based on the Payload Delivered By the Malware. The
Payload Is the Action Performed by the Malware
Examples Of Payload Classification Include:
 Spyware
 Rootkit
 Remote Access Trojan (Rat)
 Ransomware




                                                                                        134
  13.2 Computer Viruses
This is a type of malware designed to replicate and spread from computer to
computer usually by “infecting” executable applications or program code.
The Following Categories Describe Some Types Of Malware According To
Vector:
 Non-Resident/File Infector - the virus is contained within a host executable file and
   runs with the host process. the virus will try to infect other process images on
   persistent storage and perform other payload actions.
 Memory Resident - when the host file is executed, the virus creates a new process
  for itself in memory. the malicious process remains in the memory even if the host
  process is terminated.
 Boot - the virus code is written to the disk boot sector and executes as a memory
  resident process when the OS starts.
 Script And Macro Viruses - the malware uses the programming features available
  in local scripting engines for the OS and/or browser such as PowerShell, javascript,
  Microsoft office documents or PDF documents with JavaScript enabled.

The term multipartite is used for viruses that use multiple vectors and polymorphic for
viruses that can dynamically change or obfuscate their code to evade detection.
Viruses must infect a host file or media. an infected file can be distributed through any
normal means - on a disk, on a network, a download from a website or email
attachment.




                                                                                            135
  13.3 Computer Worms & Fileless Malware

Computer Worms - this is a memory resident malware that can run without
user intervention and replicate over network resources. viruses need the user
to perform an action but worms can execute by exploiting a vulnerability in a
process and replicate themselves.
Worms can rapidly consume network bandwidth as the worm replicates and
they may be able to crash an operating system or server application. worms can
also carry a payload that may perform some other malicious action.
Fileless malware - as security controls got more advanced so did malware and
this new sophisticated modern type of malware is often referred to as fileless.
The Following Categories Describe Some Types Of Malware According To
Vector:
 Fileless malware do not write their code to disk. the malware uses memory
  resident techniques to run its own process within a host process or dynamic
  link library (DLL). the malware may change registry values to achieve
  persistence.
 Fileless malware uses lightweight shell code to achieve a back door
  mechanism on the host. the shell code is easy to recompile in an obfuscated
  form to evade detection by scanners. it is then able to download additional
  packages or payloads to achieve the actor’s objectives.
 Fileless malware may use “live off the land” techniques rather than compiled
  executables to evade detection. this means that the malware code uses
  legitimate system scripting tools like power-shell to execute payload actions.




                                                                                   136
   13.4 Spyware, Keyloggers, Rootkits, Backdoors,
   Ransomware & Logic Bombs

Spyware - This is malware that can perform adware-like tracking
but also monitor local application activity, take screenshots and
activate recording devices.
Adware - Grayware that performs browser reconfigurations such
as allowing cookies, changing default search engines, adding
bookmarks and so on.
Tracking cookies - Can be used to record pages visited, the
user’s ip address and various other metadata.
Keylogger - Spyware that actively attempts to steal confidential
information by recording keystrokes.
Backdoors & rats - A backdoor provides remote user admin
control over a host and bypasses any authentication method.
A remote access trojan is a backdoor malware that mimics
the functionality of legitimate remote control programs but is
designed specifically to operate covertly. a group of bots under
the same control of the same malware are referred to as a botnet
and can be manipulated by the herder program.
Rootkits - This malware is designed to provide continued
privileged access to a computer while actively hiding its presence.
it may be able to use an exploit to escalate privileges after
installation.software processes can run in one of several “rings”.
 Ring 0 is the most privileged and provides direct access to
  hardware
 Ring 3 is where user-mode processes run
 Ring 1 or 2 is where drivers and i/o processes may run.
Ransomware - This type of malware tries to extort money
from the victim by encrypting the victim’s files and demanding
payment. ransomware uses payment methods such as wire
transfer or cryptocurrency.
Logic bombs - Logic bombs are not always malware code. a
typical example is a disgruntled admin who leaves a scripted trap
that runs in the event his or her account is disabled or deleted.
anti-malware software is unlikely to detect this kind of script and
this type of trap is also referred to as a mine.




                                                                      137
  13.5 Malware Indicators & Process Analysis

There Are Multiple Indicators Of Malware:
 Antivirus Notifications
 Sandbox Execution
 Resource Consumption - Can Be Detected Using Task Manager Or Top Linux Utility.
 File System
Because shellcode is easy to obfuscate, it can easily evade signature-based a-v products.
Threat hunting and security monitoring must use behavioral-based techniques to identify
infections.
Along with observing how a process interacts with the file system, network activity is one of
the most reliable ways to identify malware.




  13.6 Password Attacks

Plain text/ unencrypted attacks - an attack that exploits unencrypted password storage such
as those used in protocols like http, pap and telnet.
Online attacks - The threat actor interacts directly with the authentication service using
either a database of known passwords or a list of passwords that have been cracked online.
This attack can be prevented with the use of strong passwords and restricting the number of
login attempts within a specified period of time.
Password spraying - A horizontal brute force attack where the attacker uses a common
password (123456) and tries it with multiple usernames.
Offline attacks - An offline attack means the attacker has gotten access to a database of
password hashes e.g %systemroot%\system32\config\sam or %systemroot%\ntds\ntds.dit
(the active directory credential store)
Brute force attack - Attempts every possible combination in the output space in order to
match a captured hash and guess the plaintext that generated it. the more the characters
used in the plaintext password, the more difficult it would be to crack.
Rainbow table attack - A refined dictionary attack where the attacker uses a precomputed
lookup table of all possible passwords and their matching hashes.



                                                                                                138
Hybrid attack - Uses a combination of brute force and dictionary attacks.
Password crackers - There are some windows tools including cain and l0phtcrack but the
majority of password crackers like hashcat run primarily on linux.

Password managers can be implemented with a hardware token or as a
software app:
 Password Key - Usb tokens for connecting to pcs and smartphones.
 Password Vault - Software based password manager typically using a cloud service to
  allow access from any device.




  13.7 Tactics, Techniques & Procedures

A tactic, technique or procedure (TTP) is a generalized statement of adversary
behavior. ttps categorize behaviors in terms of campaign strategy and approach
(tactics), generalized attack vectors (techniques) and specific intrusion tools and
methods (procedures).

An indicator of Compromise (IOC) is a residual sign that an asset or network has
been successfully attacked. in other words, an ioc is evidence of a ttp.

Examples Of Iocs Include
 Unauthorized Software And Files
 Suspicious Emails
 Suspicious Registry And File System Changes
 Unknown Port And Protocol Usage
 Excessive Bandwidth Usage
 Rouge Hardware
 Service Disruption And Defacement
 Suspicious Or Unauthorized Account Usage
Strictly speaking an IOC is evidence of an attack that was successful. The
term indicator of attack (IOA) is sometimes also used for evidence of an
intrusion attempt in progress.




                                                                                         139
  13.8 Privilege Escalation & Error Handling

Application Attack - this attacks a vulnerability in an os or application and a vulnerability
refers to a design flaw that can cause the application security system to be circumvented or
to crash. the purpose of this attack is to allow the attacker to run his/her own code on the
system and this is referred to as arbitrary code execution.
Where the code is transmitted from one computer to another, this is referred to as remote
code execution.
Privilege Escalation - a design flaw that allows a normal user or threat actor to suddenly
gain extended capabilities or privileges on a system.
 Vertical Privilege Escalation - The User or Application Is Able to Gain Access To
  Functionality Or Data That Shouldn’t be Available to Them.
 Horizontal Privilege Escalation - The User Or Application Is Able to Access Data Or
  Functionality Intended For Another User.
Error Handling - an application attack may cause an error message. as such applications in
the event of an error should not reveal configuration or platform details that can help the
attacker.
Improper Input Handling - good programming practice dictates that any input accepted by
a program or software must be tested to ensure that it is valid. most application attacks work
by passing invalid or maliciously constructed data to the vulnerable process.




                                                                                                 140
   13.9 Uniform Resource Locator
   Analysis & Percent Encoding

Uniform Resource Locator Analysis - besides pointing to the host or service location on
the internet, a url can encode some action or data to submit to the server host. this is a
common vector for malicious activity.
Http Methods - It Is Important To Understand how Http Operates.
 An Http Session Starts With A Client (Web Browser) Making A Request To An HTTP
  Server.
 The Connection Establishes a TCP Connection
 The connection can be used for multiple requests or a client can start new TCP
  connections for different requests.
A
request typically contains a method, resource (URL path), version number, headers and
body. the principal method is get but other methods include:
 Post - Send Data To The Server For Processing By The Requested Resource
 Put - Create Or Replace The Resource. Delete Can Be Used To Remove The Resource
 Head - Retrieve The Headers For A Resource Only (Not The Body)
Data can be submitted to the server using a post or put method and the http headers and
body or by encoding the data within the URL used to access the resource.
Data submitted via a URL is delimited by the ? character which follows the resource path
and query parameters are usually formatted as one or more name=value pairs, with
ampersands delimiting each pair.




                                                                                             141
Percent Encoding - a URL can contain only unreserved and reserved characters from the
ASCII set. reserved ASCII characters are used as delimiters within the URL syntax.
Reserved Characters : / ? # [ ] @ ! $ & ‘ ( ) * + , ; =
There are also unsafe characters which cannot be used in a URL. Control characters such
as null string termination, carriage return, line feed, end of file and tab are unsafe.




                                                                                          142
  13.10 Api & Replay Attacks, Cross-Site Request
  Forgery, Clickjacking & Ssl Strip Attacks

Application Programming Interface Attacks - web applications and cloud services
implement application program interfaces (APIs) to allow consumers to automate
services.
If the API isn’t secure, threat actors can easily take advantage of it to compromise the
services and data stored on the web application. API calls over plain http are not
secure and could easily be modified by a third party.

Some Other Common Attacks Against APIs Include
 Ineffective secrets management, allowing threat actors to discover an API key
  and perform any action authorized to that key.
 Lack of input validation allowing the threat actor to insert arbitrary parameters
  into api methods and queries. this is often referred to as allowing unsanitized
  input.
 Error Messages Revealing Clues to a Potential Adversary. (Username/Password)
 Denial of Service (DoS) by Bombarding the API with Bogus Calls.




                                                                                           143
Replay Attacks - session management enables web applications to uniquely identify a user
across a number of different actions and requests.
To establish a session, the server normally gives the client some type of token and a replay
attack works by sniffing or guessing the token value and then submitting it to re-establish
the session illegitimately.
HTTP by default is a stateless protocol meaning the server preserves no information about
the client but cookies allow for the preservation of data.
A cookie has a name, value and optional security and expiry attributes. cookies can either be
persistent and non-persistent.
Cross-Site Request Forgery - a client-side or cross-site request forgery (CSRF or XSRF) can
exploit applications that use cookies to authenticate users and track sessions.
In order to work, the attacker must convince the victim to start a session with the target site.
the attacker must then pass an http request to the victim’s browser that spoofs an action on
the target site such as changing a password or an email address.




                                                                                                   144
if the target site assumes the browser is authenticated because there is a valid session
cookie, it will accept the attacker’s input as genuine. this is also referred to as a confused
deputy attack.

Clickjacking - this is an attack where what the user sees and trusts as a web application with
some sort of login page or form contains a malicious layer or invisible iframe that allows an
attacker to intercept or redirect user input.

Clickjacking can be launched using any type of compromise that allows the adversary to run
arbitrary code as a script. it can be mitigated by using http response headers that instruct the
browser not to open frames from different origins.

SSL Strip - this is launched against clients on a local network as they try to make connections
to websites. the threat actor first performs a MITM attack via ARP poisoning to masquerade
as the default gateway. When a client requests an http site that redirects to an HTTPs site in
an unsafe way, the SSL strip utility proxies the request and response, serving the client the
http site with an unencrypted login form thus capturing any user credentials.




                                                                                                   145
   13.11 Injection Attacks

XML and LDAP injection attacks - an injection attack can target other types of protocols
where the application takes user input to construct a query, filter or document.
Extensible markup language (xml) injection - xml is used by apps for authentication and
authorizations and for other types of data exchange and uploading.
Lightweight directory access protocol (ldap) injection - ldap is another example of query
language. ldap is specifically used to read and write network directory databases. a threat
actor could exploit either unauthenticated access or a vulnerability in a client app to submit
arbitrary ldap queries. This could allow accounts to be created or deleted or for the attacker
to change authorizations and privileges.
For example a web form could construct a query from authenticating the valid credentials for
bob and pa$$w0rd like this:
(& (username = bob)(password = pa$$w0rd))
If the form input is not sanitized, the threat actor could bypass the password check by
entering a valid username plus an ldap filter string
(& (username = bob)(&))
Directory traversal & command injection attacks - directory traversal is another type of
injection attack performed against a web server.
The threat actor submits a request for a file outside the web server’s root directory by
submitting a path to navigate to the parent directory (../)
The threat actor might use a canonicalization attack to disguise the nature of the malicious
input.
Canonicalization refers to the way the server converts between different methods by which
a resource (file path or url) may be represented and submitted to the simplest method used
by the server to process the input.
Server-side request forgery (SSRF) - SSRF causes the server application to process an
arbitrary request that targets another service either on the same host or a different one.
It exploits both the lack of authentication between the internal servers and services
and weak input validation allowing the attacker to submit unsanitized requests or api
parameters.




                                                                                                 146
```
