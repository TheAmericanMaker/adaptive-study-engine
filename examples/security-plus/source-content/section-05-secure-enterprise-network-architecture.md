# Section 5: Secure Enterprise Network Architecture

_Domain D3 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 5.1 Secure Network Designs
- 5.2 Network Segmentation, Topology & DMZs
- 5.3 Device Placement & Attributes
- 5.4 Secure Switching And Routing
- 5.5 Routing & Switching Protocols
- 5.6 Using Secure Protocols
- 5.7 Attack Surface
- 5.8 Firewalls
- 5.9 Firewall Implementation
- 5.10 Remote Access Architecture

## Content

```
SECTION 5 -
SECURE ENTERPRISE
NETWORK ARCHITECTURE

  5.1 Secure Network Designs

Switches - forward frames between nodes in a cabled network.
They work at layer 2 of the OSI model and make forwarding messages based on the
hardware or media access control (MAC) address of attached nodes.
They can establish network segments that either map directly to the underlying cabling or to
logical segments created in the switch configuration as virtual LANs (VLans)
Wireless access points - provide a bridge between a cabled network and wireless clients or
stations. They also work at layer 2 of the OSI model.
Load balancers - distribute traffic between network segments or servers to optimize
performance. They work at layer 4 of the OSI model or higher
Routers - forward packets around an internetwork, making forward decisions based on
IP addresses. They work at layer 3 of the OSI model. They can apply logical IP subnet
addresses to segments within a network.
Firewalls - they apply an access control list (ACL) to filter traffic passing in or out of a
network segment. They can work at layer 3 of the OSI model or higher.
Domain name system (DNS) servers - host name records and perform name resolution to
allow applications and users to address hosts and services using fully qualified domain
names (FQDNs) rather than IP addresses.
DNS works at layer 7 of the OSI model.




                                                                                               43
  5.2 Network Segmentation, Topology & Dmzs

A network segment is one where all the hosts attached to the segment can use local (layer
2) forwarding to communicate freely with one another.

Segregation means that the hosts in one segment are restricted in the way they
communicate with hosts in other segments.

Freely means that no network appliances or policies are preventing communications.
a network topology is a description of how a computer network is physically or logically
organized.

The main building block of a topology is a zone which is an area of the network where the
security configuration is the same for all hosts within it.

Zones can be segregated with VLANs while the traffic between them can be controlled
using a security device, typically a firewall.




                                                                                            44
Network Zones
 Intranet (Private Network) - This Is A Network Of Trusted Hosts Owned And Controlled
  By The Organization.
 Extranet - This Is A Network Of Semi-Trusted Hosts Typically Representing Business
  Parties, Suppliers Or Customers.
 Internet/Guest - This Is A Zone Permitting Anonymous Access By Untrusted Hosts Over
  The Internet.
Demilitarized Zones (DMZs) - The Most Important Distinction between Different
Security Zones Is Whether A Host Is Internet-Facing.
An Internet-Facing Host accepts Inbound Connections from and makes Connections To
Hosts on The Internet.
Such hosts are placed in a DMZ (perimeter or edge network). in a DMZ, external clients
are allowed to access data on private systems such as web servers without
compromising the security of the internal network as a whole.
Triple-Homed Firewall - A DMZ can also Be Established Using One Router/Firewall
Appliance With three Network Interfaces, Referred To As Triple-Homed.
 One Interface is the DMZ
 The Second is the Public One
 The Third Connects to the LAN
East-West Traffic - traffic that goes to and from a data center is referred to as north-south.
This traffic represents clients outside the data center making requests.

However in data centers that support cloud services, most traffic is actually between
servers within that data center and this traffic is referred to as east-west traffic.

Zero trust - this is based on the idea that perimeter security is unlikely to be robust enough.
as such in a zero trust model, continuous authentication and conditional access are used to
mitigate threats.

Zero trust also uses a technique called microsegmentation. this is a security process that is
capable of applying policies to a single node as though it was in a zone of its own.




                                                                                                  45
  5.3 Device Placement & Attributes

The process of choosing the type and placement of security controls to ensure the goals of
the CIA triad and compliance with any framework requirements.
The selection of effective controls is governed by the principle of defense in depth.

 Preventive Controls - Are often placed at the border of a network segment or zone.
  Preventive controls such as firewalls enforce security policies on traffic entering and
  exiting the segment, ensuring confidentiality and integrity. A load balancer control
  ensures high availability for access to the zone.
 Detective Controls - Might be placed within the perimeter to monitor traffic exchanged
  between hosts within the segment. This provides alerting of malicious traffic that has
  evaded perimeter controls.
 Preventive, Detective & Corrective Controls - Might be installed on hosts as a layer of
  endpoint protection in addition to the network infrastructure controls.




                                                                                             46
Attributes determine the precise way in which a device can be placed within the network
topology
A passive security control is one that does not require any sort of client or agent
configuration or host data transfer to operate.
An active security control that performs scanning must be configured with credentials and
access permissions and exchange data with target hosts. An active control that performs
filtering requires hosts to be explicitly configured to use the control. This might mean
installing agent software on the host, or configuring network settings to use the control as a
gateway.

Inline vs Monitor
A device that is deployed inline becomes part of the cable path. No changes in the IP or
routing topology are required. The device’s interfaces are not configured with MAC or IP
addresses.




SPAN (Switched Port Analyzer)/Mirror Port - This means that the sensor is attached to
a specially configured monitor port on a switch that receives copies of frames addressed
to nominated access ports (or all the other ports). This method is not completely reliable.
Frames with errors will not be mirrored and frames may be dropped under heavy load
Test Access Point (TAP) - This is a box with ports for incoming and outgoing network cabling
and an inductor or optical splitter that physically copies the signal from the cabling to a
monitor port. Unlike SPAN every single frame is copied or received.




                                                                                                 47
Fail-Open versus Fail-Closed
A security device could enter a failure state for a number of reasons. There could be a
power or hardware fault, an irreconcilable policy violation, or a configuration error. Hardware
failure can be caused by power surges, overheating, and physical damage.
Software failure can occur because of bugs, security vulnerabilities, and compatibility issues.
Configuration issues can be caused by human errors such as inattention, fatigue, or lack of
training.
When a device fails, it can be configured to fail-open or fail-closed

 Fail-open means that network or host access is preserved. This mode prioritizes
  availability over confidentiality and integrity.
 Fail-closed means that access is blocked. This mode prioritizes confidentiality and
  integrity over availability.



  5.4 Device Placement & Attributes

Man-In-The-Middle & Layer 2 Attacks -
Most Attacks At Layer 1 And 2 Of The Osi
Model Are Typically Focused On Information
Gathering Through Network Mapping And
Eavesdropping.
A MITM can also be performed on this layer
due to the lack of security.
MAC cloning or MACaddress spoofing -
Changes the hardware address of an adapter
to an arbitrary one either by overriding the
original address in software via os commands
or with the use of packet crafting software.
Arp Poisoning Attack - Arp poisoning attack
uses a packet crafter such as ettercap to
broadcast unsolicited arp reply packets.
Because arp has no security mechanism, the
receiving devices trust this communication
and update their mac:ip address cache table
with the spoofed address.




                                                                                                  48
MAC flooding attacks - Where arp poisoning is directed at hosts, mac flooding is
used to attack a switch.
The idea here is to exhaust the memory used to store the switch’s mac address
table which is used by the switch to determine which port to use to forward unicast
traffic to its correct destination.
Overwhelming the table can cause the switch to stop trying to apply mac-based
forwarding and simply flood unicast traffic out of all ports.




Router / Switch Security
 Physical Port Security - Access to physical switch ports and hardware should be
  restricted to authorized staff by using a secure server room or lockable hardware
  cabinets.
 Mac Limiting/Filtering - Configuring mac filtering on a switch means defining which
  mac addresses are allowed to connect to a particular port by creating a list of valid mac
  addresses. mac limiting involves specifying a limit to the number of permitted addresses
  that can connect to a port.
 Dhcp Snooping - Dynamic host configuration protocol is one that allows a server to
  assign an ip address to a client when it connects to a network. dhcp snooping inspects
  this traffic arriving on access ports to ensure that a host is not trying to spoof its mac
  address. with dhcp snooping, only dhcp messages from ports configured as trusted are
  allowed.
 Network Access Control - Nac products can extend the scope of authentication to allow
  admins to devise policies or profiles describing a minimum security configuration that
  devices must meet to be granted network access. This is called a health policy.
 Route Security - A successful attack against route security enables the attacker to
  redirect traffic from its intended destination. routes between networks and subnets
  can be configured manually, but most routers automatically discover routes by
  communicating with each other.




                                                                                               49
routing is subject to numerous vulnerabilities
 Spoofed Routing Information (Route Injection) - Traffic is misdirected to a monitoring
  port (sniffing) or continuously looped around the network causing dos.
 Source Routing - This uses an option in the ip header to pre-determine the route a
  packet will take through the network. This can be used to spoof ip addresses and bypass
  router/firewall filters.
 Software Exploits In The Underlying Operating System - Cisco devices typically use the
  internetwork operating system (ios) which suffer from fewer exploitable vulnerabilities
  than full network operating systems.




                                                                                            50
   5.5 Routing & Switching Protocols

Layer 3 Forwarding Or Routing Occurs Between Both Logically And Physically Defined
Networks. A Single Network Divided Into Multiple Logical Broadcast Domains Is Said To Be
Subnetted.
At Layer 3, Nodes Are Identified By Ip Addresses.

Address Resolution Protocol (Arp) - This Maps A Mac Address To An Ip Address.
Normally A Device That Needs To Send A Packet To An Ip Address But Does Not Know The
Receiving Device’s Mac Address Broadcasts Will Broadcast An Arp Request Packet And The
Device With The Matching Ip Responds With An Arp Reply.




Internet Protocol (Ip)
This Provides The Addressing Mechanism For Logical Networks And Subnets.
172.16.1.101/16
The /16 Prefix Indicates That The First Half Of The Address (172.16.0.0) Is The Network Id
While The Remainder Uniquely Identifies A Host On That Network. Networks Also Use 128-



                                                                                             51
Bit Ipv6 Addressing.
2001:Db8::Abc:0:Def0:1234
The First 64-Bits Contain Network Information While The Last Are Fixed As The Host’s
Interface Id.
A Route To A Network Can Be Configured Statically But Most Networks Use Routing
Protocols To Transmit New And Updated Routes Between Routers.

Some Common Routing Protocols Include
 Border Gateway Protocol (Bgp)
 Open Shortest Path First (Ospf)
 Enhanced Interior Gateway Routing Protocol (Eigrp)
 Routing Information Protocol (Rip)




  5.6 Using Secure Protocols

Secure protocols have places in many parts of your network and infrastructure. Security
professionals need to be able to recommend the right protocol for each of the following
scenarios:
 Voice and video rely on a number of common protocols. Videoconferencing tools often
  rely on HTTPS, but secure versions of the Session Initiation Protocol (SIP) and the Real-
  time Transport Protocol (RTP) exist in the form of SIPS and SRTP, which are also used to
  ensure that communications traffic remains secure.
 A secure version of the Network Time Protocol (NTP) exists and is called NTS, but NTS
  has not been widely adopted. Like many other protocols you will learn about in this
  chapter, NTS relies on TLS. Unlike other protocols, NTS does not protect the time data.
  Instead, it focuses on authentication to make sure that the time information is from a
  trusted server and has not been changed in transit.
 Email and web traffic relies on a number of secure options, including HTTPS, IMAPS,
  POPS, and security protocols like Domain-based Message Authentication Reporting
  and Conformance (DMARC), DomainKeys Identified Mail (DKIM), and Sender Policy
  Framework (SPF) as covered earlier in this chapter.
 File Transfer Protocol (FTP) has largely been replaced by a combination of HTTPS file
  transfers and SFTP or FTPS, depending on organizational preferences and needs.
 Directory services like LDAP can be moved to LDAPS, a secure version of LDAP.




                                                                                              52
 Remote access technologies—including shell access, which was once accomplished via
  telnet and is now almost exclusively done via SSH—can also be secured. Microsoft’s RDP
  is encrypted by default, but other remote access tools may use other protocols, including
  HTTPS, to ensure that their traffic is not exposed.
 Domain name resolution remains a security challenge, with multiple efforts over time
  that have had limited impact on DNS protocol security, including DNSSEC and DNS
  reputation lists.
 Routing and switching protocol security can be complex, with protocols like Border
  Gateway Protocol (BGP) lacking built-in security features. Therefore, attacks such as BGP
  hijacking attacks and other routing attacks remain possible. Organizations cannot rely on
  a secure protocol in many cases and need to design around this lack.
 Network address allocation using DHCP does not offer a secure protocol, and network
  protection against DHCP attacks relies on detection and response rather than a secure
  protocol.
 Subscription services such as cloud tools and similar services frequently leverage HTTPS
  but may also provide other secure protocols for their specific use cases. The wide
  variety of possible subscriptions and types of services means that these services must
  be assessed individually with an architecture and design review, as well as data flow
  reviews all being part of best practices to secure subscription service traffic if options are
  available.




                                                                                                   53
  5.7 Attack Surface

The network attack surface refers to all the points at which a threat actor could gain access
to hosts and services.
Using the OSI model we can analyze the potential attack surface:
 Layer 1/2 - Allows the attacker to connect to wall ports or wireless networks and
  communicate with hosts within the same broadcast domain
 Layer 3 - Allows the attacker to obtain a valid network address possibly by spoofing and
  communicate with hosts in other zones
 Layer 4/7 - Allows the attacker to establish connections to TCP or UDP ports and
  communicate with application layer protocols and services.
Each layer requires its own type of security controls to prevent, detect, and correct
attacks. Provisioning multiple control categories and functions to enforce multiple layers of
protection is referred to as defense in depth.
Security controls deployed to the network perimeter are designed to prevent external
hosts from launching attacks at any network layer. The division of the private network into
segregated zones is designed to mitigate risks from internal hosts that have either been
compromised or that have been connected without authorization.




Typical weaknesses in a network include:
 Single points of failure
 Complex dependencies
 Availability over confidentiality and
  integrity
 Lack of documentation
 Over dependence on perimeter security




                                                                                                54
  5.8 Firewalls

Packet Filtering Firewalls - These are the earliest type of firewalls and are configured by
specifying a group of rules called an access control list (acl).
Each rule defines a specific type of data packet and the appropriate action to take when a
packet matches the rule. an action can either be to deny or to accept the packet.
This firewall can inspect the headers of ip packets meaning that the rules can be based on
the information found in those headers.in certain cases, the firewall can control only inbound
or both inbound and outbound traffic and this is often referred to as ingress and egress
traffic or filtering.
A basic packet filtering firewall is stateless meaning that it does not preserve any information
about network sessions. The least processing effort is required for this but it can be
vulnerable to attacks that are spread over a sequence of packets.
Stateful Inspection Firewalls - This type of firewall can track information about the session
established between two hosts and the session data is stored in a state table.
When a packet arrives, the firewall checks it to confirm that it belongs to an existing
connection and if it does then the firewall would allow the traffic to pass unmonitored to
conserve processing effort.
Stateful inspection can occur at two layers: transport and application.
Transport Layer (Osi Layer 4) - Here, the firewall examines the tcp three-way handshake to
distinguish new from established connections.



syn > syn/ack > ack
Any deviations from this sequence can be dropped as malicious flooding or session
hijacking attempts.
Application Layer (OSI Layer 7) - This type of firewall can inspect the contents of packets at
the application layer and one key feature is to verify the application protocol matches the
port e.g http web traffic will use port 80.
IP Tables - Iptables is a command on Linux that allows admins to edit the rules enforced by
the linux kernel firewall.
IPtables works with chains which apply to the different types of traffic such as the input
chain for traffic destined for the local host. Each chain has a default policy set to drop or
allow traffic that does not match a rule.
The rules in this example will drop any traffic from the specific host 10.1.0.192 and allow icmp
echo requests (pings), dns and http/https traffic either from the local subnet (10.1.0.0/24) or
from any network (0.0.0.0/0)




                                                                                                   55
56
  5.9 Firewall Implementation


Firewall Appliances - This Is A Stand-Alone Firewall Deployed To Monitor Traffic Passing Into
And Out Of A Network Zone. It Can Be Deployed In Two Ways:
 Routed (Layer 3) - The Firewall Performs Forwarding Between Subnets
 Bridged (Layer 2) - The Firewall Inspects Traffic Between Two Nodes Such As A Router
  And A Switch.
Application-Based Firewalls
 Host-Based (Personal) - Implemented As A Software Application Running On A Single
  Host Designed To Protect The Host Only.
 Application Firewall - Software Designed To Run On A Server To Protect A Particular
  Application Only
 Network Operating System (Nos) Firewall - A Software Based Firewall Running Under A
  Network Server Os Such As Windows Or Linux.
Proxies And Gateways - A Firewall That Performs Application Layer Filtering Is Likely To Be
Implemented As A Proxy.
Proxy Servers Can Either Be Non-Transparent Or Transparent.
 Non-Transparent Means The Client Must Be Configured With The Proxy Server Address
  And Port Number To Use It
 Transparent (Forced Or Intercepting) Intercepts Client Traffic Without The Client Having
  To Be Reconfigured
Reverse Proxy Servers - These Provide For Protocol-Specific Inbound Traffic.
A Reverse Proxy Can Be Deployed On The Network Edge And Configured To Listen For
Client Requests From A Public Network




                                                                                                57
  5.10 Remote Access Architecture

Most remote access is implemented as a virtual private network (VPN) running over the
internet but it can be more difficult to ensure the security of remote workstations and
servers than those on the LAN. A VPN can also be deployed in a site-to-site model to
connect two or more private networks and is typically configured to operate automatically
Open VPN - this is an open source example of a TLS VPN. openvpn can work in tap
(bridged) mode to tunnel layer 2 frames or in tun (routed) mode to forward IP packets.
Another option is Microsoft's secure sockets tunneling protocol (SSTP) which works by
tunneling point-to-point protocol (PPP) layer 2 frames over a TLS session.
Internet protocol security (IPSEC) - TLS is applied at the application level either by using a
separate secure port or by using commands in the application protocol to negotiate a
secure connection.
IPSEC operates at the network layer (layer 3) so it can operate without having to configure
specific application support.
Authentication Header (AH) - this performs a cryptographic hash on the whole packet
including the IP header plus a shared secret key and adds this HMAC in its header as
integrity check value (ICV)
The recipient performs the same function on the packet and key and should derive the
same value to confirm that the packet has not been modified.
Encapsulation Security Payload (ESP) - this provides confidentiality and/or authentication
and integrity. it can be used to encrypt the packet rather than simply calculating an HMAC.
ESP attaches three fields to the packet: a header, a trailer (providing padding for the
cryptographic function) and an ICV.


Ipsec Transport And Tunnel Modes - Ipsec Can Be Used In Two Modes:


 Transport Mode - This Mode Is Used To Secure Communications Between Hosts On A
  Private Network. Here The Ip Header For Each Packet Is Not Encrypted, Just The Payload
  Data. If Ah Is Used In This Mode, It Can Provide Integrity For The Ip Header.




  Ip Header             AH           ESP      TCP/UDP      Payload               Trailer
                        ICV




                                                                                                 58
   Tunnel Mode - This Mode Is Used For Communications Between DNS Gateways Across
   An Unsecure Network And Is Also Referred To As Router Implementation. With Esp, The
   Whole Ip Packet (Header And Payload) Is Encrypted And Encapsulated As A Datagram
   With A New Ip Header.



    NEW Ip
                 ESP     IP Header   TCP/UDP    Payload          Trailer               ICV
    Header



Internet Key Exchange (IKE) - ipsec's encryption and hashing functions depend on a shared
secret. the secret must be communicated to both hosts and the hosts must confirm one
another's identity (mutual authentication) otherwise the connection is vulnerable to MITM
and spoofing attacks. the IKE protocol handles authentication and key exchange referred to
as security associations (SA).

IKE negotiations take place over two phases:

Phase 1 establishes the identity of the two hosts and performs key agreement using the dh
algorithm to create a secure channel. digital certificates and pre-shared key are used for
authenticating hosts. Phase 2 uses the secure channel created in phase 1 to establish which
ciphers and key sizes will be used with ah and/or esp in the IPSEC session.

VPN Client Configuration - to configure a VPN client, you may need to install the client
software if the VPN type is not natively supported by the OS.

Always-on VPN - this means that the computer establishes the VPN whenever an Internet
connection over a trusted network is detected, using the user's cached credentials to
authenticate.

When a client connected to a remote access VPN tries to access other sites on the Internet,
there are two ways to manage the connection:

Split tunnel - the client accesses the internet directly using its "native" ip configuration and
DNS servers.

Full tunnel - internet access is mediated by the corporate network, which will alter the
client's IP address and DNS servers and may use a proxy. Full tunnel offers better security
but the network address translations and DNS operations required may cause problems with
some websites especially cloud services.

Out-of-band management - remote management methods can be described as either in-
band or out-of-band (OOB).

                                                                                                   59
An In-Band Management Link Is One That Shares Traffic With Other
Communications On The “Production” Network While A Serial Console
Or Modem Port On A Router Is A Physically Out-Of-Band Management
Method.
Secure Shell - This Is The Principal Means Of Obtaining Secure
Remote Access To A Command Line Terminal. Mostly Used For Remote
Administration And Secure File Transfer (Sftp).
Ssh Servers Are Identified By A Public/Private Key Pair (The Host Key).




                                                                          60
```
