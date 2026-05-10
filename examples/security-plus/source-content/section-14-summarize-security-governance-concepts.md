# Section 14: Summarize Security Governance Concepts

_Domain D5 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 14.1 Regulations, Standards & Legislation
- 14.2 ISO and Cloud Frameworks
- 14.3 Governance Structure
- 14.4 Governance Documents
- 14.5 Change Management
- 14.6 Configuration Management
- 14.7 Scripting, Automation & Orchestration

## Content

```
SECTION 14 -
SUMMARIZE SECURITY
GOVERNANCE CONCEPTS

  14.1 Regulations, Standards & Legislation

Key Frameworks, Benchmarks And Configuration Guides May be Used to Demonstrate
Compliance With A Country’s Legal Requirements.
Due Diligence Is a Legal Term meaning that Responsible Persons have not been negligent
in Discharging their Duties.
 Sarbanes-Oxley Act (Sox) Mandates The Implementation Of Risk Assessments, Internal
  Controls And Audit Procedures.
 The Computer Security Act (1987) Requires Federal Agencies To Develop Security
  Policies For Computer Systems That Process Confidential Information.
 In 2002, The Federal Information Security Management Act (Fisma) Was Introduced To
  Govern The Security Of Data Processed By Federal Government Agencies.
Some Regulations Have Specific Cybersecurity Control Requirements While Others
Simply Mandate “Best Practice” As Represented By A Particular Industry Or International
Framework.
Personal Data And General Data Protection Regulation (GDPR)
This legislation focuses on information security as it affects privacy or personal data.
GDPR means that personal data cannot be collected, processed or retained without the
individual’s informed consent.
Compliance issues are complicated by the fact that laws derive from different sources e.g
gdpr does not apply to american data subjects but it does apply to american companies that
collect or process the personal data of people in eu countries.
National, Territory Or State Laws
In the US there are federal laws such as the gramm-leach-bliley act (GLBA) for financial
services and the health insurance portability and accountability act (HIPAA).



                                                                                             147
  14.2 ISO and Cloud Frameworks

ISO 27k - The International Organization For Standardization (ISO) Has Produced A
Cybersecurity Framework In Conjunction With The International Electro Technical
Commission (IEC).
Unlike The NIST Framework, The ISO 27001 Must be Purchased. The ISO 27001 Is part of
an Overall 27000 Series Of Information Security Standards Also Known As 27k.
There Are 3 Main Versions Of The ISO 27k
 27002 - Security Controls
 27017 & 27018 - Cloud Security
 27701 - Personal Data & Privacy




                                                                                       148
ISO 31k - This Is An Overall Framework For Enterprise Risk Management
(ERM). Erm Considers Risks And Opportunities Beyond Cybersecurity By
Including Financial, Customer Service And Legal Liability Factors.
Cloud Security Alliance (CSA) - The Not-For-Profit Organization
Produces Various Resources To Assist Cloud Service Providers (CSP) In
Setting Up And Delivering Secure Cloud Platforms.
Security Guidance - A Best Practice Summary Analyzing The Unique
Challenges Of Cloud Environments And How On-Premises Controls Can
Be Adapted To Them.
Enterprise Reference Architecture - Best Practice Methodology And
Tools For CSPs To Use In Architecting Cloud Solutions.
Cloud Controls Matrix - Lists Specific Controls And Assessment
Guidelines That Should Be Implemented By CSPs.
Statements On Standards For Attestation Engagements (SSAE) - the
SSAE are audit specifications developed by the American institute
of certified public accountants (AICPA). These audits are designed to
assure consumers that service providers (notably cloud providers) meet
professional standards.
Within SSAE No. 18, There Are Several Levels Of Reporting:
Service Organization Control (Soc2) - Soc2 Evaluates The Internal
Controls Implemented By The Service Provider To Ensure Compliance
With Trust Services Criteria (TSC) When Storing And Processing
Customer Data.
An Soc Type 1 Report Assesses The System Design, While A Type 2
Report Assesses The Ongoing Effectiveness Of The Security Architecture
Over A Period Of 6-12 Months.
Soc2 Reports Are Highly Detailed And Designed To Be Restricted.
Soc 3 - A Less Detailed Report Certifying Compliance With Soc2. They
Can Be Freely Distributed.




                                                                         149
  14.3 Governance Structure

Enterprise Governance - This is a system that holds to account, directs and controls all
entities involved in an organization.
Governance is useful in identifying roles and responsibilities.
A role is a specific position or job title that an individual occupies within an organization.
Stewardship is the responsible oversight and protection of something entrusted to one’s
care. Responsibility refers to the specific duties or tasks that an individual is expected to
fulfill within a given role.

Board of Directors
 Determine the desired future state of information/cyber security and provide funding.
 Exercise Due Care (providing the standard of care that a prudent person would have
  provided under the same conditions.)
 A fiduciary is a person or organization who holds a position of trust
 They also provide oversight and authorization of organizational activities.

Executive Management Duties
 Make decisions to achieve strategic goals and objectives
 Manage risks to an acceptable risk and also comply with applicable laws and regulations.
 Manage resources and the budget efficiently
 Evaluate performance measures
 Implement oversight process

Information Security Steering Committee
 Make decisions to achieve information security strategic goals and objectives
 Set a cybersecurity budget, authorize risk decisions and report to the board of
  committee.
 They provide an effective communication channel for ensuring the alignment of the
  security program and business objectives.




                                                                                                 150
Chief Information Security Officer (CISO) - Interprets strategic decisions and is ultimately
responsible for the success or failure of the information security program.
Supporting roles include Information Assurance Officer/Manager (IAO/IAM), Information
Security Officer (ISO)

Complimentary Organization Roles
 Privacy Officer - Responsible for developing and implementing all aspects of the privacy
  program.
 Compliance Officer - Responsible for identifying all applicable regulatory and contractual
  requirements.
 Physical Security Officer - Responsible for ensuring that appropriate physical security
  procedures are implemented
 Internal Audit - Responsible for providing independent and objective assurance services.

Functional Roles
 Owners - Responsible for oversight and decisions related to access control and
  protection.
 Custodians - Responsible for advising, managing and monitoring data protection
  controls.
 Users - Responsible for treating data in accordance with security policies and objectives.




                                                                                               151
  14.4 Governance Documents

These are used to communicate direction, expectations and rules.
They are typically derived from the information security strategy which is also derived from
the desired future state.

Policies
 These codify the high-level requirements for securing information assets and ensure CIA
 They should be approved and authorized by the organization’s highest governing body
 Modifications should be minor over extended periods of time

Standards, Baselines & Guidelines
 Standards serve as precise specifications for the implementation of policy and dictate
  mandatory requirements.
 Baselines are the aggregate of standards for a specific category or grouping such as a
  platform, device type or location
 Guidelines assist in helping to understand and conform to a standard. Guidelines are not
  mandatory.

Procedures - Procedures are instructions for how to carry out an action. They focus on
discrete actions or steps with a specific starting and ending point.
 Simple Step - Lists sequential actions. There is no decision making
 Hierarchical - Organizes the instructions in a hierarchical structure where each level is
  nested within the one above it.
 Graphic - Presents in pictorial or symbol form.
 Flowchart - Is used to communicate a process and when decision making is required.

Plan - This is a detailed strategy or tactic for doing or achieving something.
The function of the plan is to provide instructions and guidance on how to execute or
respond to a situation within a certain timeframe usually with defined stages and with
designated resources.

Acceptable Use Policy (AUP) - This details user community obligations pertaining to




                                                                                               152
Information and information systems. It contains rules that specifically pertain to acceptable
behavior and actions that are prohibited.
It’s a teaching document that develops security awareness and must be written in a way that
is easy to understand.

Non-disclosure Agreement (NDA) - Establishes data ownership and the reason why the data
is being provided.
It’s primarily used to prevent data disclosure and prevents forfeiture of patent rights.

Acceptable Use Policy Agreement - When a user signs it, they acknowledge that they
understand and agree to abide by the AUP including violation sanctions up to and including
termination.

Agreement should be executed prior to being granted access to information and information
systems.




                                                                                                 153
  14.5 Change Management

The objective is to drastically minimize the risk and impact a change can have on business
operations.

Types of Changes
 Standard - Occurs frequently, is low risk and has a pre-established procedure with
  documented tasks for completion (updates, patch management)
 Normal - Not standard but also not an emergency. Can be approved by the change
  control board (change of anti-malware product)
 Major - May have significant financial implications and could be high risk. May require
  multiple levels of management approval (change to new Operating system)
 Emergency - This is one that must be assessed and implemented without prior
  authorization to quickly resolve a major incident (switch to a backup server)

Configuration Management KPIs - Key Performance Indicators (KPIs) are business metrics
used to measure performance in relation to strategic goals and objectives.
 Successful Changes - The higher the better
 Backlog of Changes - Changes not yet completed and should not grow over time
 Emergency Changes - It should not trend upward




                                                                                             154
  14.6 Configuration Management

This is a set of practices designed to ensure that
Configuration Items (CI) are deployed in a consistent state
and stay that way through their frame. The primary goal is
to minimize risk and ensure the configuration of services
are known, good and trusted.

Configuration Management Elements
 Configuration Item (CI) -This is an aggregation of
  information system components and treated as a
  single entity throughout the configuration management
  process.
 Baseline Configuration (BC) - A set of specifications for
  a CI that has been reviewed and agreed upon and can
  be changed only through change control procedures.

Automated Provisioning - This is the ability to deploy
information technology (IT) or operational technology
(OT) systems and services using predefined automated
procedures without requiring human intervention.
The primary goal is to reduce or eliminate manual
dependencies and human error.

Provisioning Processes
 Demand - Generated Resource Allocation - is the
  automatic provisioning and deprovisioning of resources
  based upon demand.
 Idempotence - Is a principle that every time an
  automated configuration script is run, the same exact
  result is produced.
 Immutable System - Immutability is the principle that
  resources should not be changed, only created and
  destroyed (replace not fix).
 Infrastructure as Code - Is using code to manage
  configurations and automate provisioning of
  infrastructure. Supports Idempotence.




                                                              155
  14.7 Scripting, Automation & Orchestration

Scripting - This is a set of instructions (interactive/non-interactive) used to automate a
sequence of repetitive tasks.
Usually written in a scripting language which means they are interpreted and not compiled
(the scripts are read and executed line-by-line by the processor at runtime).

Scripting Tools
 Python - Interpreted, open-source programming language with an extensive available
  library.
 PowerShell - Microsoft automation and configuration management framework
 Bash - Linux | Unix shell command line interface (CLI) and scripting language.
 Macro - An automated input sequence that imitates keystrokes or mouse actions.

Adversarial Scripting
 Python - Very easy to learn and is used for writing attack code and tools
 PowerShell - Can be used to direct the execution of a local script, retrieve and execute
  remote resources using various network protocols and encode payloads.
 Bash - Can be used to direct the execution of a local script, retrieve and execute remote
  resources using various network protocols and automate tasks on a LINUX/UNIX
  platform
 Macro - A macro virus can infect a software program and trigger a set of actions when
  the program is opened or run.

Automation - This is the execution of tasks without human intervention.
The goals are to eliminate manual dependencies and human error, improve quality of
service, increase agility and reduce risk. Typically requires significant investment.

Orchestration - Orchestration is the coordination and management of multiple computer
systems, applications and/or services, stringing together multiple tasks in order to execute a
larger workflow or process.




                                                                                                 156
```
