# Section 16: Summarize Data Protection and Compliance Concepts

_Domain D5 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 16.1 Privacy & Sensitive Data Concepts
- 16.2 Data Sovereignty, Privacy Breaches & Data Sharing
- 16.3 Privacy And Data Controls
- 16.4 Privacy Principles
- 16.5 Compliance Monitoring
- 16.6 Education, Training & Awareness
- 16.7 Personnel Policies

## Content

```
SECTION 16 -
SUMMARIZE DATA
PROTECTION AND
COMPLIANCE CONCEPTS
  16.1 Privacy & Sensitive Data Concepts

The value of an information asset can be determined by how much damage its
compromise would cause the company.
It is important to consider how sensitive data must be secured not just at rest but also
in transit.

Information life cycle management
 Creation/collection
 Distribution/use
 Retention
 Disposal

Data roles & responsibilities - A data governance policy describes the security controls that
will be applied to protect data at each stage of its life cycle.
Data owner - A senior executive role with ultimate responsibility for maintaining the cia of
the information asset. The owner also typically chooses a steward and custodian and directs
their actions and sets the budget and resource allocation for controls.
Data steward - Primarily responsible for data quality. Ensuring data is labeled and identified
with appropriate metadata and that it is stored in a secure format
Data custodian - This role handles managing the system on which the data assets are
stored. This includes responsibility for enforcing access control, encryption and backup
measures.
Data privacy officer (dpo) - This role is responsible for oversight of any personally
identifiable information (pii) assets managed by the company.




                                                                                                 166
In the context of legislation and regulations protecting personal privacy, the following two
institutional roles are important
Data controller - The entity responsible for determining why and how data is stored,
collected and used for ensuring that these purposes and means are lawful. The controller
has ultimate responsibility for privacy breaches and is not permitted to transfer that
responsibility.
Data processor - An entity engaged by the data controller to assist with technical collection,
storage or analysis tasks. A data processor follows the instructions of a data controller with
regard to collection or processing.
Data classifications - Data can be classified based on the degree of confidentiality required.
 Public (unclassified) - no restrictions and can be viewed by the public. Poses no real risk
  to the company.
 Confidential (secret) - Highly sensitive information to be viewed only by authorized
  people and possibly by trusted parties under an nda.
 Critical (top secret) - Extremely valuable information and viewing is severely restricted.
Data can also be classified based on the kind of information asset.
 Proprietary/intellectual property (ip) - Information created and owned by the company
  typically about the products they make.
 Private/personal data - Information that relates to an individual identity.
 Sensitive - Refers to company data that could cause serious harm or embarrassment
  if it is leaked to the public. Sensitive personal data includes political opinions, sexual
  orientation, health records , tax records etc.




                                                                                                 167
Data types
Personally identifiable information (PII) - This is data that can be used to identify, contact
or locate an individual such as a social security number.
An IP address can also be used to locate an individual and could be considered to be a type
of pii.
Customer data -This can be institutional information but also personal information about the
customer’s employees such as sales and technical support contacts.
Financial information -This refers to data held about bank and investment accounts plus tax
returns and even credit/debit cards. The payment card industry data security standard (pci
dss) defines the safe handling and storage of this information.
Government data - Government agencies have complex data collection and processing
requirements. The data may sometimes be shared with companies for analysis under very
strict agreements to preserve security and privacy.
Data retention -This refers to backing up and archiving information assets in order to
comply with business policies and applicable laws and regulations.




  16.2 Data Sovereignty, Privacy Breaches & Data Sharing

Data sovereignty & geographical considerations - Some states and nations may respect
data more or less than others and likewise some nations may disapprove of the nature and
content of certain data.
Data sovereignty refers to a jurisdiction preventing or restricting processing and storage
from taking place on systems that do not physically reside within that jurisdiction. For
example gdpr protections are extended to any eu citizen while they are within the eu
borders.
Geographic access requirements fall into two different scenarios
 Storage locations might have to be carefully selected to mitigate data sovereignty issues.
  Most cloud providers allow choice of data centers for processing and storage, ensuring
  that information is not illegally transferred from a particular privacy jurisdiction without
  consent.
 Employees needing access from multiple geographic locations. Cloud-based file and
  database services can apply constraint-based access controls to validate the user’s
  geographic location before authorizing access.
A data breach occurs when information is read, modified or deleted without authorization.


                                                                                                 168
Notification & escalation - Responses to
a data breach must be configured so the
appropriate personnel are notified immediately
of the breach.
The first responders might be able to handle
the incident if its a minor issue however in
more serious cases, the case may need to be
escalated to a more senior manager.
In certain cases, a timescale might also be
applied. For example with gdpr, all affected
individuals must be informed of the breach
within 72 hours after the breach occurred.


Data sharing & privacy terms of
agreement
 Service level agreement (SLA) - A
  contractual agreement setting out the
  detailed terms under which a service is
  provided.
 Interconnection security agreement (ISA)
  - ISAS set out a security risk awareness
  process and commits the agency and
  supplier to implementing security controls.
 Nondisclosure agreement (NDA) - This is a
  legal basis for protecting information assets.
 Data sharing and use agreement - Personal
  data can only be collected for a specific
  purpose but data sets can be subject to
  deidentification to remove personal data.
  However there are risks of re identification if
  combined with other data sources. A data
  sharing and use agreement is a legal means
  of preventing this risk. It can specify terms for
  the way a data set can be analyzed
  and proscribe the use of re identification
  techniques.




                                                      169
  16.3 Privacy And Data Controls

Data can be described as being in one of three states:

 Data at rest - Data is in some sort of persistent storage media. This data can be
  encrypted and acls can also be applied to it
 Data in transit - This is the state when data is transmitted over a network. In this state it
  can be protected by a transport encryption protocol such as tls or ipsec.
 Data in use/processing - This is the state when data is present in volatile memory such
  as the ram cache. Trusted execution environment (tee) mechanisms e.G intel software
  guard extensions are able to encrypt the data as it exists in memory.


Data exfiltration - Data exfiltration can take
place via a wide variety of mechanisms:
 Copying the data to removable media
  such as usb drive or smartphone
 Using a network protocol such as ftp,
  http or email
 Communicating it orally over a phone or
  even with the use of text messaging.




Data protection against exfiltration
 All sensitive data is encrypted at rest
 Create and maintain offsite backups of
  data
 Ensure that systems storing or
  transmitting sensitive data are
  implementing access controls.
 Restrict the types of network channels
  that attackers can use to transfer data
  from the network to the outside.
 Train users about document
  confidentiality and the use of encryption
  to store and transmit data securely.




                                                                                                  170
Data loss prevention
Dlp products automate the discovery
and classification of data types and
enforce rules so that data is not viewed or
transferred without proper authorization.
 Policy server - to configure
  classification, confidentiality and privacy
  rules and policies, log incidents and
  compile reports
 Endpoint agents - to enforce policy on
  client computers even when they are not
  connected to the network
 Network agents - to scan
  communications at network borders
  and interface with web and messaging
  servers to enforce policy.




Remediation is the action the dlp software takes when it detects a policy violation.

 Alert only
 Block - The user is prevented from copying the original file but retains access to it.
  User may not alerted to the policy violation but it will be logged as an incident by the
  management engine.
 Quarantine - Access to the original file is denied to the user.
 Tombstone - The original file is quarantined and replaced with one describing the policy
  violation and how the user can release it again.

Privacy enhancing technologies - data minimization is the principle that data should only be
processed and stored if that is necessary to perform the purpose for which it is collected.
Data minimization affects the data retention policy and its necessary to track how long a
data point has been stored for and whether continued retention is necessary for a legitimate
processing function.
Pseudo-anonymization modifies identifying information so that reidentification depends on
an alternate data source which must be kept separate. With access to the alternated data,
pseudo-anonymization methods are reversible.




                                                                                               171
Database identification methods
Data masking - Can mean that all or part of the contents of a field are redacted by
substituting all character strings with “x”.
Tokenization - Means that all or part of data in a field is replaced with a randomly generated
token. The token is stored with the original value on a token server or vault separate to the
production database. It’s often used as a substitute for encryption.
Aggregation/binding - Another identification technique is to generalize the data such as
substituting a specific age with a broader age band.
Hashing & salting - A cryptographic hash produces a fixed-length string from arbitrary-
length plaintext data using an algorithm such as sha. If the function is secure, it should not
be possible to match the hash back to a plaintext. A salt is an additional value stored with
the hashed data field. The purpose of salt is to frustrate attempts to crack the hashes.




  16.4 Privacy Principles

Privacy - This is the right of an individual to control the use of their personal information.
Data minimization approach limits data collection to only what is required to fulfill a specific
purpose.
Privacy Statement - This describes how an organization collects, uses, shares and protects
personal information collected from individuals.
Right to be Forgotten - This pertains to an individual’s right to have their personal
information removed or deleted from online platforms, search engine results or other
publicly accessible sources.
It is not an absolute right and needs to be balanced against other rights such as freedom of
expression, public interest or legal obligations.




                                                                                                   172
Privacy Enhancing Technologies
 Data Masking - A technique used to protect sensitive data by replacing it with fictional or
  deidentified data
 Tokenization - A technique used to desensitize data by replacing the original data with
  an unrelated value of the same length and format.
 Anonymization - Is the process in which individually identifiable data is altered in a way it
  can no longer be traced back to the original owner
 Pseudo-Anonymization - Is a method to substitute identifiable data with a reversible
  consistent value


Privacy Management Components
 Privacy Program - Privacy statement, tools for data mapping, executive sponsorship and
  privacy impact assessment
 Operations - Cookie compliance, privacy enhancing technologies, reporting and
  assessment and consent mechanisms
 Incident and Breach Response - Incident prevention, detection, management,
  notification triggers and reporting obligations.




                                                                                                  173
  16.5 Compliance Monitoring

Compliance - This means acting in accordance with applicable rules, laws, policies and
obligations.
Organizations are responsible for complying with all local, state, federal and union laws and
regulations, international treaties as well as contractual obligations.
Jurisdiction - This is the power or right of a legal or political body to exercise their authority
over a person, subject or territory.

Consequences of Non-Compliance

 Fines & Sanctions
 Loss of License
 Reputational Damage
 Contractual Impact
 Resource Utilization


Compliance Monitoring - This is the active process of evaluating activities and behaviors to
verify compliance and identify any deviations or non-compliant actions.

Monitoring activities include:
 Manual Inspections
 Audits
 Data Analysis
 Automated Systems
 Specialized Tools


Automated Compliance Monitoring - This utilizes automated tools to monitor and assess
compliance.
Automated systems can analyze large volumes of data in real time to identify compliance
breaches and also generate alerts when specific conditions or thresholds are met.




                                                                                                     174
16.6 Education, Training & Awareness



  Security        Education               Training                 Awareness


   Attribute          Why                    How                       What



    Level            Insight              Knowledge                 Information



    Object       Understanding               Skill                   Behavior


               Discussion, Seminar,   Lecture, case study,       Interactive vedio,
   Method
                     Reading               hands-on               posters, games


   Measure            Essay            Problem solving       True/false,multiple choice



    Impact         Long-term             Intermediate              Shorts-terms




                                                                                          175
  16.7 Personnel Policies

 Acceptable use policy (aup)
 Code of conduct and social media
  analysis
 Use of personally owned devices in the
  workplace
 Clean desk policy


User and role-based training - Appropriate security awareness training needs to be
delivered to employees at all levels including end users, technical staff and executives.
 Overview of the organization’s security policies
 Data handling
 Password & account management
 Awareness of social engineering and phishing


Diversity of training techniques - Using a diversity of training techniques helps to improve
engagement and retention.
 Phishing campaigns
 Capture the flag - Usually used in ethical hacker training programs and gamified
  competitions.
 Computer-based training and gamification




                                                                                               176
```
