# Section 9: Evaluate Network Security Capabilities

_Domain D4 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 9.1 Benchmarks & Secure Configuration Guides
- 9.2 Hardening Concepts
- 9.3 Wi-Fi Authentication Methods
- 9.4 Network Access Control
- 9.5 Network Security Monitoring
- 9.6 Web Filtering

## Content

```
SECTION 9
 EVALUATE NETWORK
 SECURITY CAPABILITIES
   9.1 Bench Marks & Secure Configuration Guides

 Although frameworks provide a “high-level” view of how to plan its services, they
 generally don’t provide detailed implementation guidance.
 At a system level, the deployment of servers and applications is covered by benchmarks and
 secure configuration guides.

 Center For Internet Security (CIS)
 A non profit organization that publishes the well-known (the cis critical security controls).
 They also produce benchmarks for different aspects of cybersecurity e.g benchmarks for
 compliance with it frameworks include pci dss and iso 27000.
 There are also product-focused benchmarks such as windows desktop, windows server,
 macos and web & email servers.




Os/Network Appliance Platform/
Vendor-Speci ic Guides
Operating System (OS) best practice                Department of Defense Cyber
configuration lists the settings and                Exchange Provides Security Technical
controls that should be applied for a               Implementation Guides (STIGs) with
computing platform to work in defined               Hardening Guidelines for a Variety of
roles such as workstation, server,                  Software and Hardware Solutions.
network switch/router etc.
                                                   National Checklist Program (NCP)
Most vendors will provide guides,                   by NIST provides Checklists And
templates and tools for configuring and             Benchmarks for A Variety of Operating
validating the deployment of network                Systems and Applications.
appliances and operating systems and
these configurations will vary not only by
vendor but by device and version as well.

                                                                                                 95
Application Servers
Most Application Architectures use a Client/Server Model which Means Part of The
Application is a Client Software Program Installed and run on Separate Hardware to the
Server Application Code.
Attacks can Therefore be Directed at The Client, Server or The Network Channel Between
Them.


Open Web Application Security Project (OWASP)
A Non Profit Online Community That Publishes Several Secure Application Development
Resources Such As The Owasp Top 10 That Lists The Most Critical Application Security Risks.



  9.2 Hardening Concepts

Network equipment, software, and operating systems use default settings from the
developer or manufacturer which attempt to balance ease of use with security. Unfortunately
these default configurations are an attractive target for attackers as they usually include well-
documented credentials, allow simple passwords and use insecure protocols which increase
the likelihood of successful cyberattacks. Therefore, it’s crucial to change these default
settings to improve security.
Hardening refers to the methods used to improve a device’s security by changing its default
configuration. There are various ways for hardening switches, routers, server hardware and
operating systems.


Switches & Routers
 Change default credentials
 Disable unnecessary services and
  interfaces
 Use secure management protocols such
  as SSH and HTTPS instead of Telnet or
  HTTP
 Implement Access Control Lists
 Configure port security
 Enforce strong password policies




                                                                                                    96
Server Hardware and Operating
Systems
 Change default credentials                         Secure configuration
 Disable unnecessary services                       Enable logging and monitoring
 Apply security patches and updates                 Use Antivirus and Antimalware
 Use firewalls and intrusion detection               solutions
  systems                                            Enforce physical security




  9.3- Wi-Fi Authentication Methods




Wi-Fi Authentication Comes In Three Types - Open, Personal And Enterprise.
Within The Personal Category, There Are Two Methods:
 Pre-Shared Key Authentication (PSK)
 Simultaneous Authentication Of Equals (SAE)
WPA2 pre-shared key authentication - In WPA2, pre-shared key (PSK) authentication uses
a passphrase to generate the key for encryption.
The passphrase length is typically between 8 and 63 ASCII characters and is then
converted to a 256-bit HMAC value.
Wpa3 personal authentication - WPA3 also uses a passphrase like WPA2 but it changes
the method by which this secret is used to agree on session keys. this scheme is called
password authenticated key exchange (PAKE)
Wi- i protected setup (WPS) - This is a feature of both WPA and WPA2 that allows
enrollment in a wireless network based on an 8-digit pin.
It is vulnerable to brute force attacks and is set to be replaced by the easy connect method
in WPA3 which uses quick response (qr) codes of each device.




                                                                                               97
Open authentication and captive portals - Open authentication means that the client is
not required to authenticate however it can be combined with a secondary authentication
mechanism via a browser.
When the client launches the browser, the client is redirected to a captive portal or splash
page where they will be able to authenticate to the hotspot provider’s network.
Enterprise/ieee 802.1x authentication - When a wireless station requests to join the
network, its credentials are passed to an aaa server on the wired network for validation.
Once authenticated, the aaa server transmits a master key (mk) to the station and then both
of them will derive the same pairwise master key (pmk) from the mk.
Extensible authentication protocol (eap) - This defines a framework for negotiating
authentication mechanisms rather than the details of the mechanisms themselves.
Eap implementations can include smart cards, one-time passwords and biometric identifiers.




PEAP, EAP-TTLS and EAP-FAST- in                   servers into a radius hierarchy or mesh.
protected extensible authentication
                                                  Rogue access points & evil twins - a rogue
protocol (PEAP), an encrypted tunnel is
                                                  access point is one that has been installed
established between the supplicant and
                                                  on the network without authorization.
authentication server but only a server-
side public key certificate is required.          A rogue wap masquerading as a legitimate
                                                  one is called an evil twin. an evil twin might
EAP with flexible authentication via secure
                                                  have a similar ssid as the real one or the
tunneling (EAP-FAST) - is also similar to
                                                  attacker might use some dos technique to
PEAP but instead of a server side
                                                  overcome the legitimate wap.
certificate, it uses a protected access
credential (PAC) which is generated for           A rogue hardware WAP can be identified
each user from the authentication server’s        through physical inspections. there are
master key.                                       also various wi-fi analyzers that can detect
                                                  rogue waps including inssider and kismet
Radius federation - most implementations
of EAP use a radius server to validate the        Disassociation and replay attacks - a
authentication credentials for each user.         disassociation attack exploits the lack of
                                                  encryption in management frame traffic to
Radius federation means that multiple
                                                  send spoofed frames.
organizations allow access to one
another’s users by joining their radius



                                                                                                   98
One type of disassociation attack injects management frames that spoof the MAC address
of a single victim causing it to be disconnected from the network.
Another variant broadcasts spoofed frames to disconnect all stations.
Jamming Attacks - A Wi-Fi Jamming Attack can be Performed by Setting up a WAP with a
Stronger Signal.
The Only Way To Defeat This Attack Is To Either Locate The Offending Radio Source And
Disable It Or To Boost The Signal From The Legitimate Equipment.



  9.4 Network Access Control


     Network Access Control (NAC ) not
     only authenticates users and devices
     before allowing them access to the
     network but also checks and enforces
     compliance with established security
     policies. By evaluating the operating
     system version, patch level, antivirus
     status, or the presence of specific
     security software, NAC ensures that
     devices meet a minimum set of security
     standards before being granted
     network access.
     NAC also can restrict access based on
     user profile, device type, location, and
     other attributes, to ensure users and
     devices can only access the resources
     necessary to complete their duties.
     NAC plays a crucial role in identifying
     and quarantining suspicious or
     noncompliant devices.




                                                                                         99
NAC and virtual local area networks (VLANs) work together to improve and automate
network security. One of the primary ways NAC integrates with VLAN protections is through
dynamic VLAN assignment. Dynamic VLAN assignment is a NAC feature that assigns a VLAN
to a device based on the user’s identity attributes, device type, device location, or health
check results.

Agent vs Agentless Configurations
NAC can enforce security policies using agent-based and agentless methods.
In an agent-based approach, a software agent is installed on the devices that connect to the
network. This agent communicates with the NAC platform, providing detailed information
about the device’s status and compliance level. An agent-based NAC implementation can
enable features such as automatic remediation, where the NAC agent can perform actions
like updating software or disabling specific settings to bring a device into compliance with
mandatory security configurations.
In contrast, an agentless NAC approach uses port-based network access control or network
scans to evaluate devices. For example, agentless NAC may use DHCP fingerprinting
to identify the type and configuration of a device when it connects, or it might perform a
network scan to detect open ports or active services.




  9.5 Network Security Monitoring


    Network-based intrusion detection systems - An IDS is a means of using
    software tools to provide real-time analysis of either network traffic or system and
    application logs. a network-based ids captures traffic via a packet sniffer referred
    to as a sensor. when traffic matches a detection signature, it raises an alert but will
    not block the source host.
    Taps & port mirrors - Typically the packet capture sensor is placed inside a firewall
    or close to an important server and the idea is to identify malicious traffic that has
    managed to get past the firewall. depending on network size and resources, one
    or just a few sensors will be deployed to monitor key assets and network paths.




                                                                                               100
Network-based intrusion prevention systems (IPS) - An ips provides an active response to
any network threat.
Typical responses to a threat can include blocking the attacker’s ip address (shunning),
throttling the bandwidth to attacking hosts and applying complex firewall filters.
Next generation firewall (NGFW) - HGFW is a product that combines application-aware
filtering with user account-based filtering and the ability to act as an ips.
Uni ied threat management (UTM) - This refers to a security product that centralizes many
types of security controls - firewall, antimalware, spam filtering, VPN etc into a single
appliance. The downside is that this creates a single point of failure that can affect the
entire network. they can also struggle with latency issues if they are subject to too much
network activity.




      Content/url filter - A firewall typically has to sustain high loads of traffic
      which can increase latency and even cause network outages. a solution is
      to treat security solutions for server traffic differently from that of user traffic.
      A Content Filter Is Designed To Apply A Number Of User-Focused Filtering
      Rules Such As Applying Time-Based Restrictions To Browsing.




                                                                                              101
Content filters are now implemented as a class of product called secure web gateway (SWG)
which can also integrate filtering with the functionality of data loss prevention.

Host-based IDS - a host-based ids (HIDS) captures information from a single host. the core
ability is to capture and analyze log files but more sophisticated systems can also monitor
OS kernel files, monitor ports and network interfaces.

One other core feature is file integrity monitoring (FIM). FIM software will audit key system
files to make sure they match the authorized versions.

Web Application Firewall (WAF) - a WAF is designed to specifically protect software running
on web servers and their back-end databases from code injection and dos attacks.
they use application-aware processing rules to filter traffic and perform application-specific
intrusion detection.




  9.6 Web Filtering

     Its primary function is to block users from accessing malicious or inappropriate
     websites, thereby protecting the network from potential threats.
     Web filters analyze web traffic, often in real time, and can restrict access based
     on various criteria such as URL, IP address, content category, or even specific
     keywords.

     Agent-Based Web Filtering
     Agent-based web filtering involves installing a software agent on desktop
     computers, laptops, and mobile devices. The agents enforce compliance with the
     organization’s web filtering policies.
     Agents communicate with a centralized management server to retrieve filtering
     policies and rules and then apply them locally on the device.




                                                                                                 102
Centralized Web Filtering
A centralized proxy server plays a crucial role in web content filtering by acting as an
intermediary between end users and the Internet.
When an organization routes Internet traffic through a centralized proxy server, it can
effectively control and monitor all inbound and outbound web content.
The primary role of the proxy in web content filtering is to analyze web requests from users
and determine whether to permit or deny access based on established policies.

Centralized Web Filtering Techniques
 URL Scanning - Where the proxy server examines the URLs requested by users.
 Content Categorization - Classifies websites into categories
 Block Rules - Uses the proxy server to implement block rules based on various factors
  such as the website’s URL, domain, IP address and even specific keywords within the
  web content.
 Reputation-Based Filtering - This leverages continually updated databases that score
  websites based on their observed behavior and history.




                                                                                               103
```
