# Section 4: Implement Identity and Access Management

_Domain D4 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 4.1 Identity Access Management
- 4.2 Authentication Factors, Design And Attributes
- 4.3 Biometric Authentication
- 4.4 Password Concepts
- 4.5 Authorization Solutions - Part 1
- 4.6 Authorization Solutions - Part 2
- 4.7 Account Attributes & Access Policies
- 4.8 Privileged Access Management
- 4.9 Local, Network & Remote Authentication
- 4.10 Kerberos Authentication & Authorization

## Content

```
SECTION 4 -
IMPLEMENT IDENTITY AND
ACCESS MANAGEMENT

  4.1 Identity Access Management

Covers The Authentication & Authorization Aspects Of A System And How Privileged
Users Are Managed.

There Are Four Phases Involved               IM Tools & Techniques
In IAM                                        Identity Manager
 Identity - Supply Identification            Fraud Analytics
  Information
                                              Multi Factor Authentication
 Authenticate - Identity Information
  Is Verified
                                             Am Tools & Techniques
 Authorize - Allows Actions Based
  On Verified Identification                  Single Sign On
 Audit - Keeps Track Of Actions              Behavior Analytics
  Performed With The Identification
                                              Role Based Approach

Identity & Access Threats
 Spoofing
 Identity Theft
 Keylogging
 Escalation Of Privilege
 Information Leakage




                                                                                   33
  4.2 Authentication Factors, Design And Attributes

Authentication Factors
 Something You Know - This Includes Passwords, Passphrases Or Pins. A
  Knowledge Factor Is Also Used For Account Reset Mechanisms.
 Something You Have - An Ownership Factor Means That The Account Holder
  Possesses Something That No One Else Does Such As A Smart Card, Hardware
  Token Or Smartphone.
 Something You Are/Do - A Biometric Factor Uses Either Physiological Identifiers
  Like Fingerprints Or Behavioral Identifiers Such As The Way Someone Walks And
  Talks.
Multi Factor Authentication - This Combines The Use Of More Than One Authentication
Factor And Can Either Be 2factor Or 3 Factor Authentication.
Multifactor authentication requires a combination of different technologies. for
example, requiring a pin along with a date of birth isn’t multifactor.


Authentication Attributes
Compared to the authentication factors, an authentication attribute is either a non-
unique property or a factor that cannot be used independently.
 Somewhere you are - This could be a geographic location measured using a
  device’s location service or ip address. This isn’t used as a primary authentication
  factor but may be used as a continuous authentication mechanism.
 Something you can do - Behavioral characteristics such as the way you walk or
  hold your smartphone can be used to identify you to a considerable degree of
  activity.
 Something you exhibit - This also refers to a behavioral-based authentication and
  authorization with specific emphasis on personality traits such as the way you use
  smartphone apps or web search engines.
 Someone you know - This uses a web of trust model where new users are vouched
  for by existing users.




                                                                                         34
  4.3 Biometric Authentication

The first step is enrollment and the chosen biometric is scanned by a biometric reader and
converted to binary information. The biometric template is kept in the authentication server
database and when a user wants to access a resource, they are scanned and the scan is
compared to the template to determine if access will be granted or denied.
 False rejection rate (FRR) - Where a legitimate user is not recognized. also referred to as
  a type 1 error or false non-match rate (FNMR).
 False acceptance rate (FAR) - Where an interloper is accepted. also referred to as type 2
  error or false match rate (FMR)
 Crossover error rate (CER) - The point at which FRR and FAR meet. the lower the CER,
  the more efficient and reliable the technology.
Fingerprint & facial recognition - Fingerprint recognition is the most widely used as it’s
inexpensive and non-intrusive. facial recognition records multiple factors about the size and
shape of the face




Facial Recognition
 Retinal Scan - An Infrared Light Is Shone Into The Eye To Identify The Pattern Of Blood
  Vessels. It Is Very Accurate, Secure But Also Quite Expensive
 Iris Scan - Matches Patterns On The Surface Of The Eye Using Near-Infrared Imaging
  And Is Less Intrusive Than Retinal Scan.




                                                                                                35
Behavioral Technology - A Template Is Created By Analyzing A Behavior Such As Typing Or
Walking.
 Voice Recognition - Relatively Cheap But Subject To Impersonation And Background
  Noise
 Gait Analysis - Human Movement
 Signature Recognition - Records The User Applying Their Signature (Stroke, Speed And
  Pressure Of The Stylus)
 Typing - Matches The Speed And Pattern Of A User’s Input Of A Passphrase
Continuous Authentication Verifies That The User Who Logged On Is Still Operating The
Device.




  4.4 Password Concepts

Password Length - Enforces a minimum length for passwords.
Password Complexity - Enforces password complexity rules
Password Aging - Forces the user to select a new password after a set period
Password Reuse and History - Prevents the selection of a password that has been used
already.
Under the most recent NIST guidelines:
Complexity rules should not be enforced and the only restriction should be to block common
passwords.
Aging policies should not be enforced. Users should be able to select if and when a
password should be changed
Password hints should not be used.
Password Managers - These are used to mitigate poor credential management practices
that are hard to control.
The main risks involved are selection of a weak master password, compromise of the
vendor’s cloud storage or systems and impersonation attacks designed to trick the manager
into filling a password to a spoofed site.




                                                                                             36
  4.5 Authorization Solutions - Part 1

An important consideration when designing a security system is to determine how users
receive rights or permissions.
The different models are referred to as access control schemes.
Discretionary Access Control (DAC) - it is very flexible but also the easiest to compromise as
it's vulnerable to insider threats and abuse of compromised accounts.
This is based on the primacy of the resource owner and this means the owner has full
control over the resource and can decide who to grant rights to.
Role-Based Access Control (RBAC) - RBAC can be partially implemented through the use of
security group accounts.
This adds an extra degree of centralized control to the DAC model where users are not
granted rights explicitly (assigned directly) but rather implicitly (through being assigned a
role)
File System Permissions (Linux) - In Linux, There Are Three Basic
Permissions:

 Read(R) - The Ability To Access And View The File
 Write(W) - The Ability To Modify The File
 Execute(X) - The Ability To Run A Script Or Program Or Perform A Task On That Directory.
These Permissions Can Be Applied In The Context Of The Owner User(U), A Group
Account(G) And All Other Users/World(O).
D Rwx R-X R-X Home
The String Above Shows That For The Directory(D), The Owner Has Read, Write And Execute
Permissions While The Group Context And Others Have Read And Execute Permissions
The Chmod Command Is Used To Modify Permissions And Can Be Used Either In Symbolic
Or Absolute Mode.


In Symbolic Mode, The Command Works As Follows:
Chmod G+W, O-X Home
The Effect Of This Command Is to append Write Permission To The Group Context And
Remove Execute Permission From The Other Context.
By Contrast, The Command Can Also Be Used To Replace Existing Permissions.
Chmod U=Rwx, G=Rx, O=Rx Home



                                                                                                 37
D rwx r-x r-x home
In absolute mode, permissions are assigned using octal notation where r=4, w=2 and x=1
Chmod 755 home
Mandatory Access Control (MAC) - this is based on the idea of security clearance levels
(labels) instead of ACLs. In a hierarchical one, subjects are only permitted to access objects
at their own clearance level or below.
Attribute-Based Access Control (ABAC) - this is the most fine-grained type of access control
mode and it is capable of making access decisions based on a combination of subject and
object attributes plus any system-wide attributes.
This system can monitor the number of events or alerts associated with a user account or
track resources to ensure they are consistent in terms of timing of requests.
Rule-based access control - this is a term that can refer to any sort of access control model
where access control policies are determined by system-enforced rules rather than system
users.
As such RBAC, ABAC and MAC are all examples of rule-based (or non-discretionary) access
control.




  4.6 Authorization Solutions - Part 2

Directory services - Directory services are the principal means of providing privilege
management and authorization on an enterprise network as well as storing information
about users, security groups and services.
The types of attributes, what information they contain and the way object types are defined
through attributes is described by the directory schema.
Cn - common name ou - organizational unit c - country dc - domain component
E.G the distinguished name of a web server operated by widget in the uk might be:
Cn = widgetweb, ou = marketing, o = widget, c= uk, dc = widget, dc = foo
Federation - Federation means that the company trusts accounts created and managed by a
different network.
This is the notion that a network needs to be accessible to more than just a well-defined
group of employees. In business, a company might need to make parts of its network open
to partners, suppliers and customers.
Cloud versus on-premises requirements - Where a company needs to make use of
cloud services or share resources with business partner networks, authorization and
authentication design comes with more constraints and additional requirements.



                                                                                                 38
Oauth and openid connect - Many public clouds use application programming interfaces
(apis) based on representational state transfer (rest) rather than soap.
Authentication and authorization for a restful api is often implemented using the open
authorization (oauth) protocol. Oauth is designed to facilitate sharing of information within a
user profile between sites.




  4.7 Account Attributes & Access Policies

A user account is defined by a unique security identifier (sid), a name and a credential. Each
account is associated with a profile which can be defined with custom identity attributes
describing the user, such as full name, email address, contact number etc.
Each account can be assigned permissions over files and other network resources. These
permissions might be assigned directly to the account or inherited through membership
of a security group or role. On a windows active directory network, access policies can be
configured via group policy objects (gpos)




                                                                                                  39
Location-Based Policies - A User Or Device Can Have A Logical Network Location Identified
By An Ip Address Which Can Be Used As An Account Restriction Mechanism.
The Geographical Location Of A User Or Device Can Be Calculated Using A Geographical
Mechanism.
Geofencing Refers To Accepting Or Rejecting Access Requests Based On Location.
Time-Based Restrictions - There Are Three Main Types Of Time-Based Policies.
 A Time Of Day Policy Established Authorized Logon Hours For An Account
 A Time-Based Login Policy Established The Maximum Amount Of Time An Account May
  Be Logged In For
 An Impossible Travel Time/Risky Login Policy Tracks The Location Of Logon Events Over
  Time.
Account & Usage audits - accounting and auditing processes are used to detect whether
an account has been compromised or is being misused. Usage auditing means
configuring the security log to record key indicators and then reviewing the logs for
suspicious activity.

Account lockout & Disablement - if account misuse is detected or suspected, the account
can be manually disabled by setting an account property. an account lockout means that
login is prevented for a period




                                                                                            40
  4.8 Privileged Access Management

A privileged account is one that can make significant configuration changes to a host, such
as installing software or disabling a firewall or other security system. Privileged accounts
also have the right to manage network appliances, application servers, and databases.
Privileged Access Management (PAM) refers to policies, procedures and technical controls
to prevent compromise of privileged accounts.
It is a good idea to restrict the number of administrative accounts as much as possible. The
more accounts there are, the more likely it is that one of them will be compromised. On the
other hand, you do not want administrators to share accounts or to use default accounts, as
that compromises accountability.
To protect privileged account credentials, it is important not to sign in on untrusted
workstations. A secure administrative workstation (SAW) is a computer with a very low
attack surface running the minimum possible apps.
Traditional administrator accounts have standing permissions. Just-in-time (JIT) permissions
means that an account’s elevated privileges are not assigned at log-in. Instead, the
permissions must be explicitly requested and are only granted for a limited period. This is
referred to as zero standing privileges (ZSP).
There are three main models for implementing this
 Temporary Elevation - Means that the account gains administrative rights for a limited
  period. The User Account Control (UAC) feature of Windows and the sudo command in
  Linux use this concept.
 Password Vaulting/Brokering - The privileged account must be “checked out” from a
  repository and is made available for a limited amount of time. The administrator must log
  a justification for using the privileges.
 Ephemeral Credentials - Means the system generates or enables an account to use to
  perform the administrative task and then destroys or disables it once the task has been
  performed. Temporary or ephemeral membership of security groups or roles can serve a
  similar purpose.




                                                                                               41
  4.9 Local, Network & Remote Authentication

This involves a complex architecture of components but the following three scenarios are
typical:


Windows Authentication
 Windows local sign-in -- the Local Security Authority (LSA) compares the submitted
  credential to a hash stored in the Security Accounts Manager (SAM) database.
 Windows network sign-in -- the LSA can pass the credentials for authentication to a
  network service either Kerberos or NT LAN Manager (NTLM) authentication.
 Remote sign-in -- if the user’s device is not connected to the local network,
  authentication can take place over some type of virtual private network (VPN) or web
  portal.
Linux Authentication -Local user account names are stored in /etc/passwd. When a user
logs in to a local interactive shell, the password is checked against a hash stored in /etc/
shadow.
A pluggable authentication module (PAM) is a package for enabling different authentication
providers.
Single Sign-On (SSO) - This system allows the user to authenticate once to a local device
and be authenticated to compatible application servers without having to enter credentials
again.
In Windows, SSO is provided by the Kerberos framework.




  4.10 Kerberos Authentication & Authorization

Kerberos is a single sign-on network authentication and authorization protocol
used on many networks notably as implemented by Microsoft’s Active Directory
(AD) service.
Kerberos Authentication - This protocol is made up of 3 parts
 KDC (Authentication Service)
 Principal
 Application Server




                                                                                               42
```
