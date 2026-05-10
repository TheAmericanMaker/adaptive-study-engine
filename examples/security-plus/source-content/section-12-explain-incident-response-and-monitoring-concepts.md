# Section 12: Explain Incident Response and Monitoring Concepts

_Domain D4 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 12.1 Incident Response Process
- 12.2 Cyber Incident Response Team
- 12.3 Incident Response Plan
- 12.4 Incident Response Exercises, Recovery And Retention Policy
- 12.5 Incident Identification
- 12.6 Digital Forensics Documentation
- 12.7 Digital Forensics Evidence Acquisition
- 12.8 Data Sources

## Content

```
SECTION 12 -
EXPLAIN INCIDENT
RESPONSE AND
MONITORING CONCEPTS
12.1 - Incident Response Process


   This is a set of policies and procedures that are used to identify, contain, and
   eliminate cyberattacks. The goal is to allow an organization to quickly detect
   and stop attacks, minimize damage and prevent future attacks of the same
   type.
   Principal stages in incident response life cycle
    Preparation - Makes the system resilient to attack. this includes:
     hardening systems, writing policies and procedures,and creating incident
     response resources and procedures
    Identification - Determine whether an incident has taken place, assess
     how severe it might be and then notify the appropriate personnel.
    Containment - Limits the scope and magnitude of the incident. The main
     aim of incident response is to secure data while limiting the immediate
     impact on customers and business partners.
    Eradication - Once the incident is contained, the vulnerability/issue is
     removed and the affected systems are restored to a secure state.
    Recovery - The restored system is then reintegrated back into the
     business process that it supports
    Lessons learned - Analyze the incident and responses to identify
     whether procedures or systems could be improved. It is also imperative
     to document the incident.




                                                                                      119
  12.2 Cyber Incident Response Team

Preparing for incident response means establishing the policies and procedures for dealing
with security breaches and the personnel and resources to implement those policies.
First task is to define and categorize types of incidents. in order to identify and manage
incidents, you should develop some method of reporting, categorizing and prioritizing them.
An incident response team can be referred to as a cyber incident response team (CIRT),
computer security incident response team (CSIRT) or computer emergency response team
(cert).
For Major Incidents, Expertise from Other Business Divisions might be needed



 Legal - The Incident Can Be Evaluated From The Perspective Of Compliance With Laws
  And Industry Regulations.
 Human Resources (Hr) - Incident Prevention And Remediation Actions May Affect
  Employee Contracts, Employment Law And So On.
 Marketing - The Team Is Likely To Require Marketing Or Public Relations Input So Any
  Negative Publicity From A Serious Incident Can Be Managed.
Incident response policies should establish clear lines of communication both for reporting
incidents and for notifying affected parties.

Status and event details should be circulated on a need-to-know basis and only to trusted
parties identified on a call list. Trusted parties might include both internal and external
stakeholders.

Obligations to report the attack must be carefully considered and it may be necessary to
inform affected parties during or immediately after the incident so that they can perform
their own remediation e.g "change your passwords immediately"




  12.3 Incident Response Plan

This lists the Procedures, Contacts and Resources Available to Responders for Various
Incident Categories.
A Playbook Is a Data-Driven Standard Operating Procedure (SOP) to assist Junior Analysts
in Detecting and Responding to Specific Cyber threat Scenarios.



                                                                                              120
One Challenge In Incident Management is to allocate Resources Efficiently and there are
several factors that can affect this Process.
 Data Integrity - The Most important factor In Prioritizing Incidents
 Downtime - An Incident can Either Degrade or Interrupt the Availability Of an asset Or
  system.
 Economic/Publicity - both data integrity and downtime will have important economic
  effects. short-term might involve lost business opportunity while long-term may involve
  damage to reputation and marketing standing.
 Scope - Refers To the number of affected Systems In an Incident
 Detection Time - research has shown that more than half of data breaches are not
  detected for weeks or months. this demonstrates that systems used to search for
  intrusions must be thorough.
 Recovery Time - Some Incidents require Lengthy Remediation as the system Changes
  Required are Complex to Implement.
A key tool for threat research is a framework to use to describe the stages of an
attack and these stages are referred to as a cyber kill chain.




                                                                                            121
MITRE att&ck - an alternative to the kill chain is the MITRE corporation's adversarial tactics,
techniques and common knowledge.

It provides access to a database of known TTPS and tags each technique with a unique id
and places it in one or more tactic categories such as initial access , persistence or
command & control.

Diamond model of Intrusion Analysis - this suggests a framework to analyze an intrusion
event (e) by exploring the relationships between four core features: adversary, capability,
infrastructure and victim.

Each event may also be described by meta-features such as date/time, kill chain phase etc.




                                                                                                  122
    12.4 Incident Response Exercises, Recovery And
    Retention Policy

Identi ication - This is the Process of Collating Events and Determining whether any of
them should be Managed as Incidents or as Possible Precursors to an Incident.
 Tabletop - least costly where the facilitator presents a scenario and the responders
  explain what action they would take to identify, contain and eradicate the threat.
  flashcards are used in place of computer systems.
 Walkthroughs - similar to tabletop except here the responders demonstrate what
  actions they would take in response such as running scans and analyzing sample files.
 Simulations - a team based exercise where the red team attempts an intrusion, the blue
  team operates response and recovery controls and the white team moderates and
  evaluates the exercise.

Disaster recovery plan - Also called the emergency response plan. This is a document
meant to minimize the effects of a disaster or disruption. meant for short term events and
implemented during the event itself.
Business continuity plan - Identifies how business processes should deal with both minor
and disaster-level disruption. a continuity plan ensures that business processes can still
function during an incident even if at a limited scale.
Continuity of operation planning (COOP) - This terminology is used for government
facilities but is functionally similar to business continuity planning. In some definitions, coop
refers specifically to backup methods of performing mission functions without IT support.
Retention policy - a retention policy for historic logs and data captures sets the period of
which these are retained. indicators of a breach might be discovered only months after the
breach and this would not be possible without the retention policy to keep logs and other
digital evidence.

Training On Specific Incident Response Scenarios Can Use Three Forms
 Tabletop - Least Costly where the Facilitator presents a Scenario and The Responders
  explain what action they Would Take to Identify, Contain and Eradicate the Threat.
  Flashcards are used in place of Computer Systems.
 Walkthroughs - Similar to Tabletop Except here The Responders Demonstrate what
  actions they would Take In Response Such As Running Scans and Analyzing Sample
  Files.
 Simulations - A Team Based Exercise where the Red Team Attempts an Intrusion, the
  Blue Team Operates Response and Recovery Controls and the White Team moderates
  and Evaluates The Exercise.


                                                                                                    123
Disaster recovery plan - also called the emergency response plan. This is a document
meant to minimize the effects of a disaster or disruption. meant for short term events and
implemented during the event itself.
Business continuity plan - identifies how business processes should deal with both minor
and disaster-level disruption. a continuity plan ensures that business processes can still
function during an incident even if at a limited scale.
Continuity of operation planning (COOP) - this terminology is used for government facilities
but is functionally similar to business continuity planning. In some definitions, coop refers
specifically to backup methods of performing mission functions without IT support.
Retention policy - a retention policy for historic logs and data captures sets the period of
which these are retained. indicators of a breach might be discovered only months after the
breach and this would not be possible without the retention policy to keep logs and other
digital evidence.




  12.5 Incident Identification

Training On Specific Incident Response Scenarios Can Use Three Forms
 Using Logs, Error Messages And Ids/Firewall Alerts
 Comparing Deviations To Established Metrics To Recognize Incidents And Their Scopes
 Manual Or Physical Inspections Of Site, Premises, Networks And Hosts
 Notification By An Employee, Customer Or Supplier
 Public Reporting Of New Vulnerabilities
Correlation - This Means Interpreting The Relationship Between Individual Data Points To
Diagnose Incidents Of Significance to The Security Team.
A SIEM (Security Information and Event Management System) Correlation Rule Is a
Statement That Matches Certain Conditions.
These Rules Use Logical Expressions such as And And or And Operators (==, <,>, In)
A Single-User Logon Failure Might Not Raise an Alert However Multiple Failed Logins For
The Same Account Over A Short Period Of Time Should Raise One.
Error.Logonfailure > 3 And Logonfailure.Alice And Duration < 10 Minutes
One of the biggest challenges in operating a SIEM is tuning the system sensitivity to reduce
false positive indicators being reported as an event.




                                                                                                124
The correlation rules are likely to assign a criticality level to each match.
Trend analysis - This is the process of detecting patterns or indicators within a data set over
a time series and using those patterns to make predictions about future events.
 Frequency-based trend analysis establishes a baseline for a metric such as number of
  errors per hour of the day. if the frequency exceeds the threshold for the baseline, then
  an alert is raised.
 Volume-based trend analysis - this can be based on logs growing much faster than
  usual. This analysis can also be based on network traffic and endpoint disk usage.
 Statistical deviation analysis can show when a data point should be treated as suspicious.
  For example, a data point that appears outside the two clusters for standard and admin
  users might indicate some suspicious activity by that account.
Logging platforms - Log data from network appliances and hosts can be aggregated by a
siem either by installing a local agent to collect the data or by using a forwarding system to
transmit logs directly to the siem server.
Syslog - Provides an open format, protocol and server software for logging event messages
and it’s used by a very wide range of host types.
A syslog message comprises a pri code, a header containing a timestamp and host name
and a message part. usually uses UDP port 514
 Rsyslog uses the same configuration file syntax but can work over tcp and use a secure
  connection.
 Syslog-ng uses a different configuration file syntax but can also use tcp/secure
  communications and more advanced options for message filtering.
In linux, rather than writing events to syslog-format text files, logs from processes are written
to a binary-format called journald.
Events captured by journald can be forwarded to syslog and to view events in journald
directly, you can use journalct command to print the entire journal log.




System & security logs - The five main categories of windows event logs are:

 Application - Events generated by applications and services
 Security - Audit events such as a failed logon or denied access to a file
 System - Events generated by the os and its services such as storage volume health
  checks
 Setup - Events generated during the windows installation
 Forwarded Events - Events that are sent to the local log from other hosts.


                                                                                                    125
Network logs can be generated from routers, firewalls, switches and access points.
Authentication attempts for each host are likely to be written to the security log.
DNS event logs may be logged by a dns server while web servers are typically configured to
log http traffic that encounters an error or traffic that matches some predefined rule set.
The status code of a response can reveal something about both the request and the server’s
behavior.
 Codes in the 400 range indicate client-based errors
 Codes in the 500 range indicate server-based errors
 “403” may indicate that the server is rejecting a client’s attempts to access resources
  they are not authorized to.
 “502” (bad gateway) response could indicate that communications between the target
  server and its upstream server are being blocked or the upstream server is down.




Dump files - A system memory dump creates
an image file that can be analyzed to identify
the processes that are running, the contents of
temporary file systems, registry data, network
connections and more.
It can also be a means of accessing data that
is encrypted when stored on a mass storage
device.
Metadata - This the properties of data as it is
created by an application stored on media or
transmitted over a network. Metadata sources
are useful during an investigation as they
can establish timeline questions as well as
containing other types of evidence.
File - File metadata is stored as attributes. The
file system tracks when a file was created,
accessed and modified. The acl attached to
a file showing its permissions also represents
another type of attribute.
Web - when a client requests a resource from
a web server, the server returns the resource
plus headers setting or describing its properties.
headers describe the type of data returned.



                                                                                              126
Email - An email’s internet header contains address information for the recipient and sender
plus details of the servers handling transmission of the message between them.
Mobile - Phone metadata comprises call detail records (CDRs) of incoming, outgoing and
attempted calls and sms text time, duration and the opposite party’s number. meta data will
also record data transfer volumes and the location history of the device can be tracked by
the list of cell towers it has used to connect to the network.
Netflow/ipfix - A flow collector is a means of recording metadata and statistics about
network traffic rather than recording each frame.

Flow analysis tools can provide features such as:
 Highlighting trends and patterns in traffic generated by particular applications, hosts and
  ports.
 Alerting based on detection of anomalies or custom triggers
 Identification of traffic patterns revealing rouge user behavior or malware in transit




  12.6 Digital Forensics Documentation

Digital forensics is the practice of collecting evidence from computer systems to a standard
that will be accepted in a court of law.

Prosecuting external threat sources can be difficult as the threat actor may be in a different
country or have taken effective steps to disguise their location. Like dna or fingerprints,
digital evidence is latent meaning that the evidence cannot be seen with the naked eye;
rather it must be interpreted using a machine or process.

Due Process - term used in us and uk common law that requires that people only be
convicted of crimes following the fair application of the laws of the land. The first response
period following detection and notification is often critical. to gather evidence successfully,
it‘s vital that staff do not panic or act in a way that would compromise the investigation.

Legal Hold - this refers to the fact that information that may be relevant to a court case must
be preserved. This means that computer systems may be taken as evidence with all the
obvious disruption to a network that entails.

Chain of Custody - this documentation reinforces the integrity and proper handling of
evidence from collection, to analysis, to storage and finally to presentation. It is meant to
protect an organization against accusations that evidence has been tampered with during a
trial.


                                                                                                  127
Digital Forensics Reports - a report summarizes the significant contents of the digital
data and the conclusions from the investigator‘s analysis.
 Analysis must be performed without bias. conclusions and opinions should be formed
  only from the direct evidence under analysis.
 Analysis methods must be repeatable by third parties with access to the same evidence
 Ideally, the evidence must not be changed or manipulated.

E-Discovery - this is a means of filtering the relevant evidence produced from all the data
gathered by a forensic examination and storing it in a database in a format such that it
can be used as evidence in a trial.

Some Of The Functions Of E-Discovery Suites Are:
 Identify And De - Duplicate Files and Metadata
 Search - Allows Investigators to Locate Files of Interest to the Case.
 Tags - Apply standardized Keywords or labels to Files and Metadata to Help Organize
  The Evidence.
 Security - At all Points Evidence must be Shown to have Stored, Transmitted and
  analyzed without Tampering.
 Disclosure - An Important part of the Trial Procedure is that Evidence Is made available
  to Both Plaintiff And Defendant.




                                                                                              128
Video and witness interviews - The first phase of a forensics investigation is to document
the scene by taking photographs and ideally audio and video.
As well as digital evidence, an investigator should interview witnesses to establish what they
were doing at the scene and whether they observed any suspicious behavior or activity.
Timelines - A very important part of a forensic investigation will involve tying events to
specific times to establish a consistent and verifiable narrative. This visual representation of
events in a chronological order is called a timeline.
Operating systems and files use a variety of methods to identify the time at which something
occurred but the benchmark time is coordinated universal time (UTC).
Local time will be offset from UTC by several hours and this local time offset may also vary if
a seasonal daylight saving time is in place.
NTFS uses UTC “internally“ but many OS and file systems record timestamps as the local
system time and when collecting evidence, it is vital to establish how a timestamp is
calculated and note the offset between the local system time and utc.
Event logs and network traffic - An investigation may also obtain the event logs for one
or more network appliances and/or server hosts. network captures might provide valuable
evidence.
For forensics, data records that are not supported by physical evidence (data drive) must
meet many tests to be admissible in court. if the records were captured by a SIEM, it must
demonstrate accuracy and integrity.

The intelligence gathered from a digital forensic activity can be used in two
different ways:
 Counterintelligence - Identification and analysis of specific adversary tactics, techniques
  and procedures (TTPS) provides information on how to configure and audit systems so
  they are better able to capture evidence of attempted and successful intrusions.
 Strategic Intelligence - Data that has been analyzed to produce actionable insights.
  These insights are used to inform risk management and security control provisioning to
  build mature cybersecurity capabilities.




                                                                                                   129
  12.7 Digital Forensics Evidence Acquisition

Acquisition is the process of obtaining a forensically clean copy of data from a device held
as evidence. if the system is not owned by the organization then the seizure could be
challenged legally (BYOD)
Data acquisition is also more complicated when capturing evidence from a digital scene
compared to a physical one (evidence may be lost due to system glitches or loss of power).
Data acquisition usually proceeds by using a tool to make an image from the data held on
the target device. the image can be acquired from either volatile or nonvolatile storage.
Digital acquisition and order of volatility - the general principle is to capture evidence in the
order of volatility from more volatile to less volatile.


According to the ISOC, the order is as follows
 Cpu registers and cache memory
 Contents of ram including routing table, arp cache, kernel statistics
 Data on persistent mass storage devices like hard drives, usbs
 Remote logging and monitoring data
 Physical configuration and network topology
 Archival media and printed documents


Digital forensics software include:
 Encase forensic is a digital forensics case management product. contains workflow
  templates showing the key steps in diverse types of investigation.
 The forensic toolkit (ftk) from accessdata. a commercial investigation suite designed to
  run on windows server.
 The sleuth kit - an open source collection of command line tools and programming
  libraries for disk imaging and file analysis. autopsy is the gui that sits on top of the kit and
  is accessed through a web browser.
 Winhex - a commercial tool for forensic recovery and analysis of binary data, with
  support for a range of file systems and memory dump types.
 The volatility framework which is widely used for system memory analysis.




                                                                                                     130
Disk image acquisition refers to acquiring data from
non-volatile storage. it could also be referred to as
device acquisition meaning the ssd storage in a
smartphone or media player.
There are three device states for persistent storage
acquisition
Live acquisition - Means copying the data while the
host is still running. this may capture more evidence
or more data for analysis and reduce the impact on
overall services. however the data on the actual disks
will have changed so this method may not produce
legally acceptable evidence.
Static acquisition by shutting down the host - runs
the risk that the malware will detect the shut-down
process and perform anti-forensics to try and remove
traces of itself.
Static acquisition by pulling the plug - This means
disconnecting the power at the wall socket. This will
likely preserve the storage device in a forensically
clean state but there is the risk of corrupting data.
Whichever method is chosen, it is important to
document the steps taken and supply a timeline of all
actions.
Preservation and integrity of evidence - It is vital that
the evidence collected at the crime scene conform
to a valid timeline. recording the whole process
establishes provenance of the evidence as deriving
directly from the crime scene.
To obtain a clean forensic image from a non-volatile
storage, you need to ensure nothing you do alters the
data or metadata on the source disk or file system. A
write blocker can ensure this by preventing any data
from being changed by filtering write commands.
The host devices and media taken from the crime
scene should be labeled, bagged and sealed using
tamper-evident bags. bags should have anti-static
shielding to reduce the possibility that data will be
damaged or corrupted on the electronic media by
electrostatic discharge.
The evidence should be stored in a secure facility.




                                                            131
Acquisition of other data types includes:
 Network - Packet captures and traffic flows can contain evidence. most networks will
  come from a SIEM.
 Cache - Software cache can be acquired as part of a disk image. the contents of
  hardware cache are generally not recoverable.
 Artifacts and data recovery - Artifact refers to any type of data that is not part of the
  mainstream data structures of an os. Data recovery refers to analyzing a disk for file
  fragments that might represent deleted or overwritten files. The process of recovering
  them is referred to as carving.
 Snapshot - Is a live acquisition image of a persistent disk and may be the only means of
  acquiring data from a virtual machine or cloud process.
 Firmware - Is usually implemented as flash memory. Some types like the pc firmware can
  potentially be extracted from the device or from the system memory using an imaging
  utility.




  12.8 Data Sources

Incident investigation often requires analysis of several data sources in order to draw a
defensible conclusion.
 Vulnerability Scans
 Log files
 SIME dashboards
 Metadata
 Packet capture

Log Analysis and Response Tools
 Security Information Event Management (SIEM) is an automation tool for real-time data
  capture, event correlation, analysis and reporting
 Threat Intelligence Platform (TIP) is an automation tool that combines multiple threat
  intelligence feeds and integrates with existing SIEM solutions
 User & Entity Behavior Analytics (UEBA) - is an automation tool that models human and
  machine behavior to identify normal and abnormal behavior.
 Security Orchestration, Automation and Response (SOAR) is an automation tool that
  responds to alerts and takes remediation steps.




                                                                                              132
Packet Capture - This is the process of intercepting and logging traffic for
analysis.
 A protocol analyzer (sniffer) is a tool used to capture and analyze network packets
 A port mirror captures network traffic from one or several ports of a switch and forwards
  a copy of the traffic to an analysis device
 A network TAP is a dedicated hardware device that is inserted between network devices
  and makes copies of the traffic and forwards to an analysis device.

Packet Capture Modes
 Normal - The network interface card (NIC) only captures frames intended for the interface
  (filtering by MAC address)
 Promiscuous - The NIC accepts any frame it captures even if it was not the intended
  recipient
 Unfiltered - Packet capture regardless of data elements
 Filtered - Packet capture limited to specific data elements




                                                                                              133
```
