# Section 2: Explaining Threat Actors And Threat Vectors

_Domain D2 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 2.1 Vulnerability, Threat And Risk
- 2.2 Attributes Of Threat Actors
- 2.3 Threat Actors
- 2.4 Attack Surface & Attack Vectors
- 2.5 Vulnerable Software & Network Vectors
- 2.6 Lure-Based & Message-Based Vectors
- 2.7 Third Party Risks
- 2.8 Intro To Social Engineering

## Content

```
SECTION 2 -
EXPLAINING THREAT
ACTORS AND THREAT
VECTORS

  2.1 Vulnerability, Threat And Risk

Vulnerability - this is a weakness that could be triggered accidentally or exploited
intentionally to cause a security breach. threats can exist even when there are no
vulnerabilities.

Threats can exist without risks but a risk needs an associated threat to exist
the path or tool used by a malicious threat actor can be referred to as the attack vector.

Risks are often measured based on the probability that an event might occur as well as the
impact of the event on the business.

Threat assessment is the combination of a threat actor’s intentions to harm combined with
an assessment of that actor’s capability to carry out those intentions.

Risk assessment involves identification of security risks through the analysis of assets,
threats and vulnerabilities, including their impacts and likelihood.

Risks are event focused (the database server goes down) while threats focus on intentions
(a hacker wants to take down the database server)




                                                                                             13
  2.2 Attributes Of Threat Actors

Location - An external threat or actor is one that has no account or authorized access to
the target system. such threats must use malware and or social engineering to infiltrate
the security system. Conversely, an internal or insider threat actor is one that has been
granted permissions on the system and typically means either an employee or a third party
contractor.
Intent/motivation - Intent describes what an attacker hopes to achieve from the attack while
motivation is the reason for perpetuating the attack.motivation could be driven by greed,
curiosity or grievance.
Threats can either be structured or unstructured. A criminal gang attempting to steal
financial data is a structured targeted threat while a script kiddie launching a series of spam
emails is unstructured and opportunistic.
Level of sophistication/capability - the technical abilities and resources/funding the
adversary possesses must also be considered. capability refers to a threat actor’s ability to
craft novel exploit techniques and tools.



  2.3 Threat Actors

 Script kiddie - Use hacker tools without necessarily understanding how they work or
  have the ability to craft new attacks.
 Black hats - Very skilled and have financial interests
 White hat - Hack systems and networks with full authorization typically to discover
  vulnerabilities and test current security setup.
 Gray hats - Are very skilled and typically employ black hat tactics for white hat objectives
 Hacktivists ** - Hacking for a cause. they might attempt to obtain and release confidential
  information to the public or deface a website. (anonymous, wikileaks)
 State actors & advanced persistent threats - The term atp was coined to understand the
  behavior underpinning modern types of cyber adversaries. it refers to the ongoing ability
  of an adversary to compromise network security and maintain access by using a variety
  of tools and techniques.
 Criminal syndicates - Criminal syndicates can operate across the internet from different
  jurisdictions than its victim, increasing the complexity of prosecution.
 Insider threats - These include, compromised employees, disgruntled employee (ex,)
  second streamer, spy/saboteur, shadow it, unintentional




                                                                                                  14
  2.4 Attack Surface & Attack Vectors

Attack Surface - This refers to all the points at which a malicious threat actor could try to
exploit a vulnerability. The attack surface for an external actor is and should be far smaller
than that for an insider threat. Minimizing the attack surface means restricting access so that
only a few known endpoints, protocols/ports and services are permitted.
The attack vector is the path that a threat actor uses to gain access to a secure system and
can include



          Direct Access                                   Supply Chain
          Removable Media                                 Web & Social Media
          Email                                           Cloud
          Remote & Wireless




  2.5 Vulnerable Software & Network Vectors

Vulnerable software is one that contains a flaw in its code or design that can be exploited to
circumvent access control or to crash the process.
Unsupported systems & applications - An unsupported system is one whose vendor no
longer develops updates or patches for it.
One strategy for dealing with unsupported apps that cannot be replaced is to try to isolate
them from other systems. The idea is to reduce opportunities for a threat actor to access the
vulnerable app and run exploit code. Using isolation as a substitute for patch management is
an example of a compensating control.
Network Vectors - An exploit technique for any given software vulnerability can be classed
as either remote or local.
 Remote means the vulnerability can be exploited by sending code to the target over a
  network.
 Local means that the exploit code must be executed from an authenticated session on
  the computer.


                                                                                                  15
An unsecure network is one that lacks the attributes
of CIA while a secure network uses an access control
framework and cryptographic solutions to identify,
authenticate, authorize and audit network users, hosts and
traffic.


Some specific threat vectors associated with
unsecure networks are:
 Direct Access - Getting physical access to an unlocked
  workstation, stealing a PC or maybe using a boot disk
  to install malicious tools.
 Wired Network - A threat actor attaches an
  unauthorized device to a physical network port and is
  able to launch eavesdropping or DoS attacks.
 Remote & Wireless Network - The attacker either
  obtains credentials for a remote access or wireless
  connection to the network or cracks the security
  protocols used for authentication
 Cloud Access - The attacker is likely to target the
  accounts used to develop services in the cloud or
  manage cloud systems. They may also try to attack the
  cloud service provider (CSP) as a way of accessing the
  victim system.
 Bluetooth Network - The threat actor exploits a
  vulnerability or misconfiguration to transmit a malicious
  file to a user’s device over the Bluetooth personal area
  wireless networking protocol.
 Default Credentials - The attacker gains control of
  a network device or app because it has been left
  configured with a default password
 Open Service Port - The threat actor is able to
  establish an unauthenticated connection to a logical
  TCP or UDP network port




                                                              16
  2.6 Lure-Based & Message-Based Vectors

This is something superficially attractive that causes its target to want it even though it may
be concealing something dangerous.
In cybersecurity terms, when the target opens the file bait, it delivers a malicious payload
hook that will typically give the threat actor control over the system or perform service
disruption

 Removable Device - The attacker conceals malware on a USB thumb drive or memory
  card and tries to trick employees into connecting the media to a PC or smartphone
  typically through a drop attack.
 Executable File - The threat actor conceals exploit code in a program file (Trojan
  Malware).
 Document Files - Malware is concealed by embedding it in word processing and PDF
  format files.
 Image Files - The exploit code is concealed in an image file that targets a vulnerability in
  browser or document editing software.




                                                                                                  17
Message-Based Vectors
 Email - The attacker sends a malicious file attachment via email that allows attachments
  (phishing).
 Short Message Service (SMS)
 Instant Messaging - Most apps for this are more secure than SMS because they use
  encryption but they can still contain software vulnerabilities.
 Web & Social Media - Malware may be concealed in files attached to posts or presented
  as downloads.
The most powerful exploits are zero-click which means that simply receiving an attachment
or viewing an image on a web page can trigger the exploit.




  2.7 Third Party Risks

Vendor Management is the process of choosing supplier companies and evaluating the
risks inherent in relying on a third party product or service.
Within vendor management, system integration refers to the process of using components
from multiple vendors to implement a business workflow.
There are two main Data Risks When Using Third Parties

 The vendor may need to be granted access to your data
 The vendor may have to be used to host the data or the data backups

Data Storage
The Following Precautions Should Be Taken:
 Ensure the same protections For Data as though it were stored
  On-Premises.
 Monitor and Audit Third-Party access to the Data
 Evaluate compliance impacts from Storing Personal Data on a
  Third-Party System




                                                                                             18
  2.8 Intro To Social Engineering

This is the exploitation of human emotions and interactions to extract valuable information.
more dangerous than traditional methods of hacking as it relies on human error which is
subjective & less predictable than software/hardware vulnerabilities.
Social engineering relies heavily on human emotions such as fear, curiosity, excitement,
anger and guilt.
Phishing - Relies on creating a sense of excitement or panic in the target using emails.
Spear phishing - A phishing attack against a very specific individual or organization
Angler phishing - A phishing attack directed specifically at social media users
Whaling - A phishing attack targeted at senior executives of an organization
Tailgating - The attacker without access authorization closely follows an authorized person
in a reserved area




                                                                                               19
Vishing - Relies on creating a sense of
excitement or panic in the target using a
phone call
Smishing - Relies on creating a sense of
excitement or panic in the target using a text
message
Hoaxes - The hacker impersonates an
employee or angry customer
Baiting - Dropping infected usb drives in the
parking lot to influence employees.
Piggybacking - An attacker enters a secure
building with the permission of an employee
Shoulder Surfing - Obtaining sensitive
information by spying
Dumpster Diving - Obtaining sensitive
information by going through the company
trash
Credential Darvesting - Using phishing
emails and spamming campaigns to gather
information which can then be sold.
Pharming - Redirecting victims to a malicious
website using dns cache poisoning.
Watering Hole Attack - An attack that aims to
compromise a specific group of end-users by
infecting existing websites or creating a new
one that will attract them.
Typo Squatting / url Hijacking - Hackers
register misspelled domain names of
popular websites hoping to capture sensitive
information. e.g facbook.com. instagarm.com
Influence Campaigns - A major program
launched by an adversary with a high level
of capability such as a nation-state actor
or terrorist group. the goal is to shift public
opinion on some topic and when deployed
along with espionage, disinformation/fake
news and hacking, it can be characterized as
hybrid warfare.




                                                  20
```
