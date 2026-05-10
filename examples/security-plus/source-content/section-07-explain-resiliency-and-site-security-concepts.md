# Section 7: Explain Resiliency and Site Security Concepts

_Domain D3 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 7.1 Backup Strategies & Storage
- 7.2 Implementing Redundancy Strategies
- 7.3 Cyber Security Resilient Strategies
- 7.4 Physical Security Controls
- 7.5 Physical Host Security Controls

## Content

```
SECTION 7 -
EXPLAIN RESILIENCY AND
SITE SECURITY CONCEPTS

  7.1 Backup Strategies & Storage

Backups & Retention Policies - as Backups take up Space, There is the Need for Storage
Management Routines while also Giving Adequate Coverage Of The Required Window.
The recovery Window is determined by the Recovery Point Objective (RPO) which is
determined through Business Continuity Planning.


Backup Types
 Full includes all files and directories while incremental and differential check the status of
  the archive attribute before including a file. The archive attribute is set whenever the file
  is modified so the backup software knows which files have been changed and need to
  be copied.
 Incremental makes a backup of all new files as well as files modified since the last
  backup while differential makes a backup of all new and modified files since the last full
  backup. Incremental backups save backup time but can be more time-consuming when
  the system must be restored. The system is restored first from the last full backup set and
  then from each incremental backup that has subsequently occurred.




Snapshots and images - snapshots are used for open files that are being used all the time
because copy-based mechanisms are not able to backup open files.

In windows, snapshots are provided for on NTFS by the volume shadow copy service (VSS).

Backup Storage Issues - backups require CIA as well and must be secured at all times.
Natural disasters such as fires and earthquakes must also be accounted for.


                                                                                                   73
Distance Consideration Is a calculation of how far offsite Backups need to be Kept Given
different disaster scenarios However they mustn’t be too far to slow down a Recovery
Operation.
The 3-2-1 Rule States that You Should Have 4 Copies of Your Data Across Two Media Types
with one copy held Offline and Offsite.


Backup Media Types
 Disk
 Network attached storage (nas) - An appliance that is a specially configured type of
  server that makes raid storage available over common network protocols
 Tape - Very cost effective and can be transported offsite but slow compared to disk-based
  solutions especially for restore operations
 San & cloud
Restoration order - If a site suffers an uncontrolled outage, ideally processing should be
switched to an alternate site. However, if an alternate processing site is not available, then the
main site must be brought back online as quickly as possible to minimize service disruption.




A complex facility such as a data center or campus network must be reconstituted according
to a carefully designed order of restoration.
 Enable and test power delivery systems (grid power, ups, secondary generators and so
  on)
 Enable and test switch infrastructure then routing appliances and systems
 Enable and test network security appliances (firewalls, ids)
 Enable and test critical network servers (dhcp. DNS, ntp and directory services)
 Enable and test back-end and middleware (databases). verify data integrity
 Enable and test front-end applications
 Enable client workstations and devices and client browser access.




                                                                                                     74
Non-persistence
 Snapshot/revert to known state - A saved system state that can be reapplied to the
  instance.
 Rollback to known configuration
 Live boot media - An instance that boots from read-only storage to memory rather
  than being installed on a local read/write hard disk.
When provisioning a new or replacement instance automatically, the automation system
may use one of two types of mastering instructions.
 Master image - the “gold copy” of a server instance with the os applications and
  patches all installed and configured.
 Automated build from a template - similar to a master image and is the build
  instructions for an instance. rather than storing a master image, the software may build
  and provision an instance according to the template instructions.



  7.2 Implementing Redundancy Strategies

High Availability - a key property of any resilient system and is typically measured over a
period of one year.
The Maximum Tolerable Downtime (MTD) metric expresses the availability requirement for a
particular business function.
High availability also means that a system is able to cope with rapid growth in demand.
Scalability is the capacity to increase resources to meet demands with similar cost ratios
 To Scale Out is to Add More Resources In Parallel with Existing Resources
 To Scale Up is to Increase the Power of Existing Resources.
Elasticity refers to the system’s ability to handle these changes on demand in real time.
Fault Tolerance & Redundancy - a system that can experience failures and continue to
provide the same or nearly the same level of service is said to be fault tolerant.
Fault tolerance is often achieved by provisioning redundancy for critical components and
single points of failure.



                        Dual Power Supplies          Battery Backups And
Power                                                  Upss
Redundancy              Managed Power
                         Distribution Units (Pdus)    Generators



                                                                                              75
A Ups Is Always Required To Protect Against Any Interruption As A Backup Generator Cannot
Be Brought Online Fast Enough To Respond To A Power Failure.
Network Redundancy - Network Interface Card (Nic) Teaming Means The Server Is Installed
With Multiple Nics Or Nics With Multiple Ports Or Both. Each Port Is Connected To Separate
Network Cabling.
For Example Four 1gb Ports Gives An Overall Bandwidth Of 4gb So If One Port Goes Down,
3gb Of Bandwidth Will Still Be Provided.
Switching & Routing - Network Cabling Should Be Designed To Allow For Multiple Paths
Between The Various Switches And Routers So That During A Failure Of One Part Of The
Network, The Rest Remains Operational.
Load Balancers - Nic Teaming Provides Load Balancing At The Adapter Level, Load Balancing
And Clustering Can Also Be Provisioned At A Service Level.
 A Load Balancing Switch Distributes Workloads Between Available Servers.
 A Load Balancing Cluster Enables Multiple Redundant Servers To Share Data And Session
  Information To Maintain A Consistent Service If There Is Failover From One Server To
  Another.
Disk Redundancy - Redundant Array Of Independent Disks (Raid) - Here Many Disks Can Act
As Backups For Each Other To Increase Reliability And Fault Tolerance.
There Are Several Raid Levels Numbered 0 To 6




   RAID Level                   Fault Tolerance

                               Mirroring means that data is written to two disks simultaneously, providing
   Level 1                     redundancy (if one disk fails, there is a copy of data on the other). The
                               main drawback is that storage efficiency is only 50%.

                               Striping with parity means that data is written across three or more disks,
                               but additional information (parity) is calculated. This allows the volume to
   Level 5
                               continue if one disk is lost. This solution has better storage efficiency than
                               RAID 1.

                               Double parity, or level 5 with an additional parity stripe, allows the volume
   Level 6
                               to continue when two devices have been lost.

                               Nesting RAID sets generally improves performance or redundancy.For
   Nested (0+1, 1+0, or 5+0)   example, some nested RAID solutions can support the failure ofmore than
                               one disk.




                                                                                                                76
Geographical Redundancy & Replication - Data Replication can be applied In Many
Contexts:
 Storage Area Networks - Redundancy can be Provided Within the SAN and Replication
  can also Take Place Between SANs using WAN Links.
 Database
 Virtual Machine - The Same VM Instance Can Be Deployed In Multiple Locations. This
  Can Be Achieved By Replicating The Vm’s Disk Image And Configuration Settings.
Geographical Dispersal Refers to Data Replicating Hot And Warm Sites that are Physically
Distant from One Another. This Means that Data is Protected Against a Natural Disaster
Wiping Out Storage at one of the Sites.


Asynchronous & Synchronous Replication
 Synchronous Replication is designed to write data to all replicas simultaneously
  therefore all replicas should always have the same data all the time.
 Asynchronous Replication writes data to the primary storage first and then copies
  data to the replicas scheduled intervals. it isn't a good choice for a solution that
  requires data in multiple locations to be consistent




  7.3 Cyber Security Resilient Strategies

Configuration management - Configuration management ensures that each component of
ict infrastructure is in a trusted state that has not diverged from its documented properties.
Change control and change management reduce the risk that changes to these components
could cause service disruption.
Asset management - An asset management process tracks all the organization’s critical
systems, components, devices and other objects of value in an inventory.
An asset management database can be configured to store as much or as little information
as it deemed necessary though typical data would be type, model, serial number, asset id,
location, user(s), value and service information.




                                                                                                 77
Asset identification & standard naming conventions - Tangible assets can be identified
using a barcode label or frequency id (rfid) tag attached to the device. the rfid tag is a chip
programmed with asset data and can help to also track the location of the device making theft
more difficult.
A standard naming convention for hardware and digital assets such as accounts and virtual
machines makes the environment more consistent. This means errors are easier to spot and
it’s easier to automate through scripting.
The naming strategy should allow admins to identify the type and function of any particular
resource or location at any point in the network directory.
Change control & change management - A change control process can be used to request
and approve changes in a planned and controlled way. change requests are usually
generated when
 Something needs to be corrected
 When something changes
 Where there is room for improvement in a process or system currently in place.
In a formal change management process, the need or reasons for change and the procedure
for implementing the change is captured in a request for change (rfc) document and
submitted for approval.




The implementation of changes should be carefully planned, with consideration for how the
change will affect dependent components.
For major changes, a trial change should be attempted first and every change should be
accompanied by a rollback plan so the change can be reversed if it has a negative impact.
Site resiliency - An alternate processing site might always be available and in use while a
recovery site might take longer to set up or only be used in an emergency.
 A hot site can failover almost immediately.
 A warm site could be similar but with the requirement that the latest data set will need to
  be loaded.
 A cold site takes longer to set up and could be an empty building waiting to have
  whatever equipment that is needed to be installed in it.
Diversity and defense in depth - layered security is typically seen as improving cybersecurity
resiliency because it provides defense in depth (multiple security controls).




                                                                                                  78
Allied with defense in depth is the concept of security through diversity. Technology diversity
refers to a mix of oss, applications, coding languages and so on while control diversity means
that the layers of controls should combine different classes of technical and administrative
controls with the range of control functions to prevent, detect, correct and deter.
Vendor diversity - As well as deploying multiple types of controls, there are also advantages
in leveraging vendor diversity.
While single vendor solutions provide interoperability and can reduce training and support
costs, it does have several disadvantages.
 Not obtaining best-in-class performance
 Less complex attack surface.
 Less innovation


Deception and disruption strategies
Active defense means an engagement with the adversary and can mean the deployment of
decoy assets to act as lures or bait.
A honey pot is a system set up to attract threat actors, with the intention of analyzing attack
strategies and tools to provide early warnings of attack attempts. it could also be used to
detect internal fraud, snooping and malpractice.
A honeynet is an entire decoy network.
On a production network, a honeypot is more likely to be located in a dmz, or on an isolated
segment on the private network if the honeypot is seeking to draw out insider threats.




                                                                                                  79
A honeypot or honeynet can be combined with the concept of a honeyfile which is
convincingly useful but actually fake data.
Some examples of disruption strategies include:
 Using bogus DNS entries to list multiple non-existent hosts
 Configuring a web server with multiple decoy directories
 Using port triggering or spoofing to return fake telemetry data when a host detects port
  scanning activity. This will result in multiple ports being falsely reported as open.
 Using a DNS sinkhole to route suspect traffic to a different network such as a honeynet.




  7.4 - Physical Security Controls

Physical access controls - These are security measures that restrict and monitor access to
specific physical areas or assets. They can control access to buildings, server rooms, data
centers, finance or legal areas and so on.
Physical access controls depend on the same access control fundamentals as network or os
security:
 Authentication - Create lists of approved people
 Authorization - Create barriers around a resource so access to it is controlled through
  defined entry and exit points
 Accounting - Keep a record of when entry/exit points are used and detect security
  breaches.

                                                                                              80
Site layout, fencing & lighting - Given constraints of cost and existing infrastructure, try to
plan the site using the following principles
 Locate secure zones
 Use a demilitarized zone design for the physical space and position public access areas
  so that guests do not pass near secure zones.
 Use signage and warnings to enforce the idea that security is tightly controlled.
 Entry points to secure zones should be discreet. Do not allow an intruder the opportunity
  to inspect security mechanisms.
 Try to minimize traffic having to pass between zones. The flow should be “in and out”
  rather than “across and between”
 Give high traffic public areas high visibility
 In secure zones, do not display screens facing toward pathways or windows. Alternatively
  use one-way glass so that no one can look in through windows.




Gateways and locks - in order to secure a gateway, it must be fitted with a lock. Lock types
can be categorized as follows:
 Physical - A conventional lock that prevents the door handle from being operated
  without the use of a key.
 Electronic - Rather than a key, the lock is operated by entering a pin on an electronic
  keypad. This type of lock is also referred to as cipher, combination or keyless.
 Biometric - A lock may be integrated with biometric scanner




Physical attacks against smart cards and usb - smart cards used to bypass electronic locks
can be vulnerable to cloning and skimming attacks.
 Card cloning - Making one or more copies of an existing card. A lost or stolen card with
  no cryptographic protections can be physically duplicated.
 Skimming - Refers to using a counterfeit card to capture card details which are then used
  to program a duplicate.




                                                                                                  81
Malicious usb charging cables and plugs are also a widespread problem. A usb data blocker
can provide mitigation against “juice-jacking” attacks by preventing any sort of data transfer
when the smartphone is connected to a charge point.


Alarm systems & sensors
there are five main types of alarms
 Circuit - A circuit-based alarm sounds when the circuit is opened or closed depending on
  the type of alarm. Could be caused by a door or window opening or by a fence being cut.
 Motion detection - A motion-based alarm is linked to a detector triggered by any
  movement within an area.
 Noise detection - An alarm triggered by sounds picked up by a microphone.
 Proximity - Rfid tags and readers can be used to track the movement of tagged objects
  within an area.
 Duress - This type of alarm is triggered manually by staff if they come under threat.




Security guards & cameras - Surveillance is typically a second layer of security designed to
improve the resilience of perimeter gateways.
Security guards can be placed in front of secure and important zones and can act as a very
effective intrusion detection and deterrence mechanism but can be expensive.
Cctv is a cheaper means of providing surveillance than using security guards.
The other big advantage is that movement and access can also be recorded but the main
drawback is that response times are longer and security may be compromised if not enough
staff are present to monitor the camera feeds.
Reception personnel & id badges - A very important aspect of surveillance is the challenge
policy and can be quite effective against social engineering attacks.
An access list can be held at the reception area for each secure area to determine who is
allowed to enter.
Reception areas for high-security zones might be staffed by at least two people at all times




                                                                                                 82
  7.5 - physical host security controls

Secure Areas - A secure area is designed to store critical assets with a higher level of access
protection than general office areas. The most vulnerable point of the network infrastructure
will be the communications or server room.
Air gap/ dmz - An air gapped host is one that is not physically connected to any network.
Such a host would normally have stringent physical access controls.
An air gap within a secure area serves the same function as a dmz. As well as being
disconnected from any network, the physical space around the host makes it easier to
detect unauthorized attempts to approach the asset.
Protected Distribution & Faraday Cages - A physically secure cabled network is referred
to as protected cable distribution or as a protected distribution system (pds). There are two
main risks:
 An attacker could eavesdrop using a tap
 An attacker could cut the cable (dos)
Heating, Ventilation & Air Conditioning - Environmental controls mitigate the loss of
availability through mechanical issues with equipment such as overheating.
For computer rooms and data centers, the environment is typically kept at a temperature of
about 20-22 degrees centigrade and relative humidity of 50%.
Hot and Cold Aisles - A server room or data center should be designed in such a way as to
maximize air flow across the server or racks.
The servers are placed back-to-back not front-to-back so that the warm exhaust from one
bank of servers is not forming the air intake for another bank. This is referred to as a hot/cold
aisle arrangement.




                                                                                                    83
Fire detection & suppression - Fire suppression systems work on the basis of the fire
triangle. This triangle works on the principle that a fire requires heat, oxygen and fuel to ignite
and burn so removing any one of them will suppress the fire.
Overhead sprinklers may also be installed but there is the risk of a burst pipe and accidental
triggering as well as the damage it could cause in the event of an actual fire.
Secure data destruction - Physical security controls also need to take account of the disposal
phase of the data life cycle. Media sanitization and remnant removal refer to erasing data
from hard drives, flash drives and tape media before they are disposed of.
There are several physical destruction options:
 Burning
 Shredding and pulping
 Pulverization
 Degaussing - Exposing a hard disk to a powerful electromagnet disrupts the magnetic
  pattern that stores the data.




Data Sanitization Tools - The standard method of sanitizing an HDD is called overwriting.
This can be performed using the driver’s firmware tools or a utility program.
The most basic type of overwriting is called zero filling which just sets each bit to zero. Single
pass zero filling can leave patterns that can be read with specialist tools.
Secure Erase (SE) - Since 2001, the SATA and serial attached SCSI (SAS) specifications have
included a secure erase (SE) command. This command can be invoked using a drive/array
utility or the hdparm Linux utility. On HDDs, this performs a single pass of zero-filling.
Instant Secure Erase (ISE) - Hdds and ssds that are self-encrypting drives (seds) support
another option invoking a sanitize command set in sata and SAS standards from 2012 to
perform a crypto ease. Drive vendors implement this as ISE. With an ISE, all data on the drive
is encrypted using media encryption key (MEK) and when the erase command is issued, the
MEK is erased rendering the data unrecoverable.




                                                                                                      84
```
