# Section 6: Secure Cloud Network Architecture

_Domain D3 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 6.1 Cloud Deployment Models
- 6.2 Responsibility Matrix
- 6.3 Cloud Security Solutions
- 6.4 Infrastructure As Code Concepts
- 6.5 Zero Trust
- 6.6 Embedded Systems
- 6.7 Industrial Control Systems & Internet Of Things

## Content

```
SECTION 6 -
   SECURE CLOUD NETWORK
   ARCHITECTURE


  6.1 Cloud Deployment Models

Public (multi-tenant) - A service offered over the internet by cloud service providers (csps) to
cloud consumers
Hosted Private - Hosted by a third party for the exclusive use of an organization. Better
performance but more expensive than public.
Private - Cloud infrastructure that is completely private and owned by the organization.
Geared more towards banks and governmental services where security and privacy is of
utmost importance.
Community - Several organizations share the costs of either a hosted private or fully private
cloud.
Cloud Service Models - Cloud services can also be differentiated on the level of complexity
and pre-configuration provided (sometimes referred to as anything as a service xaas)
Most common implementations are infrastructure, software and platform.
Infrastructure As A Service (IAAS) - It resources (servers, load balancers and san) are
provided here. Examples include amazon elastic compute cloud, oracle cloud and microsoft
azure virtual machines.
Software As A Service (SAAS) - Provisioning of software applications and can be purchased
on a pay-as-you-go or lease arrangement. Examples are microsoft 365, salesforce and adobe
creative cloud.
Platform As A Service (PAAS) - Provides resources somewhere between saas and iaas. A
typical paas solution would provide servers and storage network infrastructure and also a
web-application or database platform on top.
Examples include oracle database, microsoft azure sql database and google app engine.



                                                                                                   61
Security As A Service
 Consultants - can be used for framework analysis or for more specific projects.
 Managed Security Services Provider (MSSP) - fully outsourcing responsibility for
  information assurance to a third party. can be expensive but a good fit for an SME that
  has no in-house security capability.
 Security As A Service (SECAAS) - can mean a lot of things but typically means
  implementing a particular security control such as malware scanning in the cloud.
  examples include CloudFlare, Mandiant/fireeye and SonicWall.




   6.2 Responsibility Matrix

The shared responsibility model describes the balance of responsibility between a customer
and a cloud service provider (CSP) for implementing security in a cloud platform.
The division of responsibility becomes more or less complicated based on whether the
service model is SaaS, PaaS, or IaaS. For example, in a SaaS model, the CSP performs the
operating system configuration and control as part of the service offering.
In contrast, operating system security is shared between the CSP and the customer in an
IaaS model.
A responsibility matrix sets out these duties in a clear table.




                                                                        CIS Controls Cloud   CIS Foundations
 Responsibility               On-premises   laaS   PaaS   SaaS   FaaS
                                                                        Companion Guide        Benchmarks

 Data classification and
 Accountability

 Client and end-point
 Protection                   w
 Identity and access
 Management


 Application-level Controls


 Network Controls


 Host Infrastructure


 Physical Security



                                       Cloud customer            Cloud provider
                                                                                                               62
  6.3 Cloud Security Solutions

Cloud computing is also a means of transferring risk and as such it is important to identify
which risks are being transferred and what responsibilities both the company and service
provider will undertake.
A company will always still be held liable for legal and regulatory consequences in case of a
security breach though the service provider could be sued for the breach.
The company will also need to consider the legal implications of using a csp if its servers are
located in a different country.
Application security in the cloud refers both to the software development process and to
the identify and access management (iam) features designed to ensure authorized use of
applications.
Cloud provides resources abstracted from physical hardware via one or more layers of
virtualization and the compute component provides process and system memory (ram)
resources as required for a particular workload.
High availability - one of the benefits of using the cloud is the potential for providing services
that are resilient to failures at different levels.
In terms of storage performance, high availability (ha) refers to storage provisioned with a
guarantee of 99.99% Uptime or better and the csp typically uses redundancy to make multiple
disk controllers and storage devices available to a pool of storage resources.
Replication - data replication allows businesses to copy data to where it can be utilized most
effectively and the cloud may be used as a central storage area.




                                                                                                     63
The terms hot and cold storage refer to how quickly data is retrieved and hot storage is quicker
but also more expensive to manage.
 Local replication - Replicates data within a single data center in the region where the
  storage account was created.
 Regional replication - Replicates data across multiple data centers within one or two
  regions.
 Geo-redundant storage (grs) - Replicates data to a secondary region that is distant from the
  primary region. This safeguards data in the event of a regional outage or a disaster.




Virtual private clouds (VPCs) - each customer can create one or more VPCs attached to their
account. By default, a vpc is isolated from other csp accounts and from other VPCs operating
in the same account.
Each subnet within a vpc can either be private or public. For external connectivity that isn’t
appropriate for public.
Routing can be configured between subnets in a vpc and between VPCs in the same account
or with VPCs belonging to different accounts.
Configuring additional VPCs rather than subnets within a vpc allows for a greater degree of
segmentation between instances.
A VPC endpoint is a means of publishing a service that is accessible by instances in other
VPCs using only the aws internal network and private ip addresses. There are two types -
gateway and interface


                                                                                                 64
 Cloud firewall security - Filtering decisions can be made based on packet headers and
  payload contents at various layers
 Network layer 3 - The firewall accepts/denies connections based on the ip addresses
  or address ranges and tcp/udp port numbers (actually contained in layer 4 headers but
  the functionality is still always described as layer 3 filtering).
 Transport layer 4 - The firewall can store connection states and use rules to allow
  established traffic.
 Application layer 7 - The firewall can parse application protocol headers and payloads
  and make decisions based on their contents.




Firewalls in the cloud can be implemented in several ways to suit different purposes.
 As software running on an instance
 As a service at the virtualization layer to filter traffic between vpc subnets and
  instances. This equates to an on-premises network firewall.

Cloud access security brokers (CASB) -CASBs provide you with visibility into how clients
and other network nodes are using cloud services.
 Enable single sign-on authentication and enforces access controls and authorizations
  from the enterprise network to the cloud provider
 Scan for malware and rouge devices
 Monitor and audit user and resource activity
 Mitigate data exfiltration


Casbs are implemented in one of three
ways:
 Forward proxy - positioned at the
  client network edge that forwards user
  traffic to the cloud network
 Reverse proxy - positioned at the
  cloud network edge and directs traffic
  to cloud services
 api




                                                                                           65
  6.4 - Infrastructure As Code Concepts

Service-Oriented Architecture (SOA) - this conceives of atomic services closely mapped to
business workflows. each service takes defined inputs and produces defined outputs.

Service functions are self-contained, do not rely on the state of other services and expose
clear input/output (i/o) interfaces.

Micro-services - micro service-based development shares many similarities with agile
software project management and the processes of continuous delivery and deployment.

The main difference from SOA is that while SOA allows a service to be built from other
services, each micro-service should be capable of being developed, tested and deployed
independently (highly decoupled).

Services Integration - service integration refers to ways of making these decoupled services
work together to perform a workflow. Where SOA used the concept of an enterprise service
bus, micro-services integration and cloud services/virtualization, integration generally is very
often implemented using orchestration tools.

Automation focuses on making a single discrete task easily repeatable while orchestration
performs a sequence of automated tasks.

Cloud orchestration platforms connect to and provide administration, management and
orchestration for many popular cloud platforms and services.




                                                                                                   66
Application Programming Interfaces
(Api) - Soa, Microservices, Service
Integration, Automation And
Orchestration All Depend On Apis
 Simple Object Access Protocol
  (SOAP) - uses XML format
  messaging and has a number of
  extensions in the form of web
  services standards that support
  common features such as
  authentication, transport security
  and asynchronous messaging.
 Representational State Transfer
  (REST) - a much looser
  architectural framework also
  referred to as restful API. soap
  requests must be sent in correctly
  formatted XML document while
  rest requests can be submitted as
  an http operation.





Serverless architecture - This is a modern design pattern for service delivery and is strongly
associated with modern web applications - netflix.
billing is based on execution time rather than hourly charges and this type of service provision
is also called function as a service (FAAS).
Serverless architecture eliminates the need to manage physical or virtual server instances so
there is no need for software and patches or file system security monitoring.
Infrastructure as code - An approach to infrastructure management where automation and
orchestration fully replace manual configuration is referred to as infrastructure as code (IAC)
The main objective of iac is to eliminate snowflake systems which are basically systems that
are different from others and this can happen when there is a lack of consistency in terms of
patch updates and stability issues.
By rejecting manual configuration of any kind, iac ensures idempotence which means making
the same call with the same parameters will always produce the same result.
Iac means using carefully developed and tested scripts and orchestration runbooks to
generate consistent builds.



                                                                                                   67
Fog & Edge Computing - Traditional data center architecture sensors are quite likely to have
low bandwidth and higher latency WAN links to data networks.
Fog computing developed by cisco addresses this by placing fog node processing resources
close to the physical location for the iot sensors. The sensors communicate with the fog node
using wi-fi or 4g/5g and the fog node prioritizes traffic, analyzes and remediates alertable
conditions.




Edge Computing Is A Broader Concept Partially Developed From Fog Computing.
 Edge Devices Collect and Depend Upon Data for Their Operation.
 Edge Gateways Perform Some Pre-Processing of Data to And From Edge Devices to
  Enable Prioritization.
 Fog Nodes can be Incorporated as a Data Processing Layer Positioned Closed To The
  Edge Gateways.
 The Cloud Or Data Center Layer Provides the Main Storage and Processing Resources
  Plus Distribution and Aggregation of Data Between Sites.
Instead of depending on a cluster of clouds for computing and data storage, edge
computing leverages local computing (routers, PCs, smartphones) to produce shorter
response time as the data is processed locally.




   6.5 Zero Trust
This is a security framework requiring
all subjects, assets and workflows to be
authenticated, authorized and continuously
validated before being granted or keeping
access to the data or application.

Zero Trust View
 No Implicit Zone Trust - Assets should
  always act as though an attacker was
  present in the enterprise network
 Devices on the network cannot be
  owned or configured by users
 Assume all network connections are
  insecure


                                                                                                68
  Zero Trust Core Principles (NIST SP800-207)
   Continuous Verification - Always verify access all the time
   Access Limitation - Access to resources are granted strictly on a per-
    session basis
   Limit the “Blast Radius” - Minimize the impact of a breach
   Automate - Automate context, collection and response for credentials,
    workloads, threat intelligence and endpoints




Control & Data Planes
 Control Plane - Used by infrastructure components to maintain and configure assets,
  access control and communication security.
 Data Plane - Used for communication between software components.




                            Zero Trust Architecture
                                                                                        69
Zero Trust Logical Components
 Policy Decision Point (PDP) - The gatekeeper and is made up of the policy engine and
  policy administrator.
 Policy Engine (PE) - is responsible for granting access to a resource
 Policy Administrator (PA) - generates any session-specific authentication token or
  credential used to access an enterprise resource.
 Policy Enforcement Point (PEP) - is responsible for enabling, monitoring and terminating
  connections between a subject and an enterprise resource.


Zero Trust Disadvantages
 Can be complex and expensive
 Slows down application performance
 Hampers employee productivity




  6.6 Embedded Systems

This is a complete system designed to perform a specific dedicated function.
These systems can be a micro-controller in a small device or could be as large and
complex as the network of control devices managing a water treatment plant.
Embedded systems are characterized as static environments while a PC is a dynamic
environment because both software and hardware changes can be made by the user.
Embedded Systems are Usually Constrained by:

 Processor Capability                            Power (Battery)
 System Memory                                   Authentication Technologies
 Persistent Storage                              Cryptographic Identification
 Cost                                            Network And Range Constraints

System On Chip - this is a system where all processors, controllers and devices are
provided on a single processor die or chip. this is often very power efficient and is
commonly used with embedded systems.


                                                                                             70
RaspberryPI and Arduino are examples of soc boards initially devised as educational tools
but now widely used for industrial applications and hacking.

Field Programmable Gate Array (FPGA) - as many embedded systems perform simple and
repetitive operations, it is more efficient to design the hardware controller to perform only the
instructions needed. An example of this is the application-specific integrated circuits (ASICs)
used in ethernet switches but they can be quite expensive and work only for a single
application.

An FPGA solves the problem because the structure is not fully set at the time of manufacture
giving the end customer the ability to configure the programming logic of the device to run a
specific application.

Operational Technology (OT) Networks - these are cabled networks for industrial applications
and typically use either serial data protocols or industrial Ethernet. Industrial ethernet is
optimized for real-time and deterministic transfers.

Cellular Networks - a cellular network enables long-distance communication over the same
system that supports mobile and smartphones.




           Also known as Baseband Radio and there are Two Main
           Radio Technologies:
            Narrowband-Iot (Nb-Iot) - This Refers to Low-Power Version Of
             The Long Term Evolution (Lte) Or 4g Cellular Standard.
            Lte Machine Type Communication (Lte-M) - This is Another
             Low-Power System But Supports Higher Bandwidth (Up To About
             1 Mbps)
           Any LTE-based cellular radio uses a subscriber identity module (SIM)
           card as an identifier. the sim is issued by a cellular provider with
           roaming to allow the use of other supplier's tower relays.




                                                                                                    71
  6.7 Industrial Control Systems & Internet Of Things

Industrial systems have different priorities to it systems and tend to prioritize availability
and integrity over confidentiality (reversing the CIA triad as the AIC triad).

Workflow and Process Automation Systems - industrial control systems (ICs) provide
mechanisms for workflow and process automation and these systems control machinery
used in critical infrastructure like power and water suppliers and health services. An ICS
comprises plant devices and equipment with embedded PLCs.

Supervisory Control and Data Acquisition (SCADA) - A SCADA system takes the place of a
server in large scale multiple-site ICSS. SCADA typically run as software on ordinary
computers, gathering data from and managing plant devices and equipment with
embedded PLCs referred to as field devices.

ICS/SCADA Applications - these types of systems are used within many sectors of industry

 Power Generation And Distribution
 Mining And Refining Raw Materials
 Fabrication And Manufacturing
 Logistics
 Site And Building Management Systems

Internet Of Things (IoT) - This is Used to describe a Global Network of Appliances and
Personal Devices that have Been Equipped with Sensors, Software and Network
Connectivity.



                                                                                                 72
```
