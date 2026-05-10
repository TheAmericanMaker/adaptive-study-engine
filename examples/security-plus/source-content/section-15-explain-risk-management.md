# Section 15: Explain Risk Management

_Domain D5 · Source: external/source-repo/SYO-701+Study+Guide.pdf_

## Subsections
- 15.1 Risk Management Process
- 15.2 Risk Controls
- 15.3 Business Impact Analysis
- 15.4 Third-Party Risk Management & Security Agreements
- 15.5 Audit & Assurance
- 15.6 PenTest Attack Life Cycle

## Content

```
SECTION 15 -
EXPLAIN RISK
MANAGEMENT

  15.1 Risk management process

Risk management involves all processes from assessing the risk to managing it.

 Identify Assets - Humans, data, emails, hardware (scoping)
 Identify Vulnerabilities - Weak passwords, unpatched systems
 Identify Exploits & Threats - Hackers, natural disasters
 Determine Safeguards & Countermeasures - Security policies, backups, patches,
  updates etc
 Determine which risks are acceptable or not

Enterprise risk management - Risk management is treated very differently in
companies of different sizes and compliance requirements. most companies will
institute enterprise risk management (erm) policies and procedures based on
frameworks such as nist’s rmf


Risk Types
 External
 Internal
 Multiparty (Supply Chain Attack)
 Intellectual Property (Ip) Theft
 Software Compliance/Licensing
 Legacy Systems




                                                                                  157
Quantitative risk assessment - This aims to assign concrete values to each risk factor:
 Single loss expectancy (sle) - The amount that would be lost in a single occurrence of
  the risk factor. it’s calculated by multiplying the value of the asset by an exposure factor
  (ef). ef is the percentage of the asset value that would be lost.
 Annualized loss expectancy (ale) - The amount that would be lost over the course of a
  year. done by multiplying the sle by the annualized rate of occurrence (aro)
It’s important to realize that the value of an asset isn’t just about its material value but also
the damage its compromise could cost the company (e.g a server is worth more than its
cost).
Qualitative risk assessment - Seeks out people’s opinions of which risk factors are
significant. assets and risks may be placed in categories such as high, medium or low value
and critical, high, medium or low probability respectively.




    Risk Factor            Impact             ARO          Cost Of Control         Overall Risk


   Legacy Windows
       Clients



    untrained Staff



     No Antivirus
      Software




                                                                                                    158
  15.2 Risk Controls

Risk Mitigation - This is the most common method of handling risk and typically involves the
use of countermeasure or safe guards. The likelihood of the risk occurring must be reduced
to the absolute minimum.
Risk Avoidance - The cost of the risk involved is too high and must be avoided. Mitigation
means the risk probabilities are reduced to the maximum while avoidance means the risk is
eliminated completely
Risk Transference - This involves assigning or transferring the risk to another entity or
organization. In other words, the risk is outsourced because the organization cannot mitigate
the risk on it’s own due to cost.
Risk Acceptance - The cost of mitigating the risk outweighs the cost of losing the asset. Risk
can also be accepted when there isn’t a better solution.
Risk Appetite & Residual Risk - Where risk acceptance has the scope of a single system,
risk appetite has a project or institution-wide scope and is typically constrained by regulation
and compliance. Where inherent risks are the risks before security controls have been
applied, residual risks are those carried over after the controls have been applied.
Control risk is a measure of how much less effective a security control has become over
time e.G antivirus.
Risk Register - A document showing the results of risk assessments in a comprehensible
format.




                                                                                                   159
  15.3 Business Impact Analysis

Business Impact Analysis (BIA) - This is the process of assessing what losses might occur
for a range of threat scenarios.
Where BIA identifies risks, the business continuity plan (BCP) identifies controls and
processes that enable an organization to maintain critical workflows in the face of an
incident.
Mission Essential Function (MEF) - This is one that cannot be deferred. the business must
be able to perform the function as close to continually as possible.
Maximum Tolerable Downtime (MTD) - The maximum amount of time a business can be
down before it can no longer recover in a reasonable time or manner.
Recovery Time Objective (RTO) - The targeted amount of time to recover business
operations after a disaster.
Work Recovery Time (WRT) - Following systems recovery, there may be additional work
to reintegrate different systems, test overall functionality and brief system users on any
changes.
Recovery Point Objective (RPO) - Refers to the maximum amount of data that can be lost
after recovery from a disaster before the loss exceeds what is tolerable to an organization.




                                                                                               160
Identification of critical systems - Asset types include:
 People
 Tangible assets
 Intangible assets (ideas, reputation, brand)
 Procedures (supply chains, critical procedures)
Single points of failure - A SPOF is an asset that causes the entire workflow to collapse if it
is damaged or unavailable. Can be mitigated by provisioning redundant components.
Mean time to failure (MTTF) and mean time between failures (MTBF) represent the
expected lifetime of a product. MTTF should be used for non-repairable assets for example,
a hard drive can be described with an MTTF while a server with MTBF.
 Calculation for mtbf is the total time divided by the number of failures. For example 10
  devices that run for 50 hours and two of them fail, the mtbf is 250.
 Calculation for mttf for the same test is the total time divided by number of devices so 50
  hours/failure.
Mean time to Repair (MTTR) is a measure of the time taken to correct a fault so that the
system is restored to full operation. This metric is important for determining the overall RTO.


Disasters
 Internal Vs External - Internal Could Be System Faults Or Malicious/Accidental Act By An
  Employee
 Person-Made - War, Terrorism, Pollution
 Environmental - Natural Disaster
A Site Risk Assessment Should Be Conducted To Identify Risks From These Factors.


Disaster Recovery Plans
 Identify Scenarios For Natural And Non-Natural Disasters And Options For Protecting
  Systems
 Identify Tasks, Resources And Responsibilities For Responding To A Disaster




                                                                                                  161
 Train Staff In The Disaster Planning Procedures And How To React Well To Change.

Functional Recovery Plans
 Walkthroughs, Workshops And Seminars
 Tabletop Exercises - Staff “Ghost” The Same Procedures As They Would In A Disaster
  Without Actually Creating Disaster Conditions.
 Functional Exercises - Action Based Sessions Where Employees Can Validate The Drp
  By Performing Scenario-Based Activities In A Simulated Environment
 Full-Scale Exercises - Action Based Sessions That Reflect Real Situations. Held On Site
  And Uses Real Equipment And Real Personnel.




  15.4 Third-Party Risk Management & Security Agreements

A root of trust is only trustworthy if the vendor has implemented it properly. Anyone with time
and resources to modify the computer’s firmware could create some sort of backdoor access.
For a tpm to be trustworthy, the supply chain of chip manufacturers, firmware authors and the
administrative staff responsible for providing the computing device to the user must all be
trustworthy.
When assessing suppliers for risk, it is helpful to distinguish two types of relationship
 Vendor - This means a supplier of commodity goods and services possibly with some
  level of customization and direct support.
 Business partner - This implies a closer relationship where two companies share quite
  closely aligned business goals.


End of life systems - When a manufacturer discontinues the sales of a product, it enters an
end of life (EOL) phase in which support and availability of spares and updates become
more limited.
An end of service life (EOSL) system is one that is no longer supported by its developer or
vendor.
Windows versions are given five years of mainstream support and five years of extended
support (during which only security updates are provided).
Organizational security agreements - It is important to remember that although one can
outsource virtually any service to a third party, one cannot outsource legal accountability for
these services.



                                                                                                  162
Issues of security risk awareness, shared duties and contractual responsibilities can be set
out in a formal legal agreement.
Memorandum of understanding (mou) - A preliminary agreement to express an intent to
work together. They are usually intended to be relatively informal and not contract binding.
Business partnership agreement (bpa) - The most common model of this in it are the
agreements between large companies and their resellers and solution providers.
Nondisclosure agreement (NDA) - Used between companies and employees/contractors/
other companies as a legal basis for protecting information assets.
Service level agreement (SLA) - A contractual agreement describing the terms under which
a service is provided.
Measurement systems analysis (MSA) - A means of evaluating the data collection and
statistical methods used by a quality management process to ensure they are robust.



  15.5 Audit & Assurance

Information security assessment - This is the process of determining how effectively the
entity being evaluated meets the specific security requirements.
 Examination - is the process of interviewing, reviewing, inspecting, studying and
  observing to facilitate understanding, comparing standards or to obtain evidence (audit)
 Testing - is the process of exercising objects under specified conditions to compare
  actual and expected behaviors (pen testing)
Assurance -This is the measure of confidence that intended controls, plans and processes
are effective in their application.
The objective of an audit is to provide independent assurance based on evidence.
Audit plan - This is a high-level description of audit work to be performed in a specific time
frame.
The plan may include objectives, resource requirements and reporting expectations. The
final audience for the audit results is either an executive or board audit committee.
Audit focus
 Compliance - Meeting laws, regulations and industry standards.
 Security & privacy - Attaining required levels of cia and privacy
 Internal controls - Evaluation of the design of the controls and assessment of the
  operational effectiveness and efficiency of the controls
 Alignment - Assure alignment with organizational and control objectives.




                                                                                                 163
Sampling - This is used to infer characteristics about a population based upon the
characteristics of a sample of that population.
Evidence sampling is applying a procedure to less than 100% of the population.
Audit examination opinions
 Unqualified - Rendered when the auditor does not have any significant reservations
  (clean report)
 Qualified - Rendered when there are minor deviations or scope limitations.
 Adverse - Rendered when the target is not in conformance with the control objectives or
  when the evidence is misleading or misstated.
 Disclaimer - This means the auditor was not able to render an opinion due to certain/
  named circumstances.
Audit framework - This is a structured and systematic approach used by auditors to plan,
execute and report on an audit engagement. They are typically developed by auditing
standards-setting bodies.
 Isaca cobit 5
 Aicpa (ssae18)
Ssae 18 soc versions
 Soc1 is a report of controls relevant to user entities financial statements
 Soc2 is based upon trust services principles (tsp) reports on controls intended to mitigate
  risk related to security, cia and privacy
 Soc 3 is similar to soc2 but does not detail testing performed and is designed for public
  distribution.




                                                                                                164
  15.6 PenTest Attack Life Cycle

 Reconnaissance - Is typically followed by an initial exploitation phase where a software
  tool is used to gain some sort of access to the target’s network.
 Persistence - this is the tester’s ability to reconnect to the compromised host and use it as
  a remote access tool (rat) or backdoor.
 Privilege escalation - The tester attempts to map out the internal network and discover
  the services running on it.
 Lateral movement - Gaining control over other hosts and usually involves executing the
  attack or scripting tools such as powershell.
 Pivoting - If a pen tester achieves a foothold on a perimeter server, a pivot allows them to
  bypass a network boundary and compromise servers on an inside network.
 Actions on objectives - For a threat actor, this means stealing data while for a tester it
  would be a matter of the scope definition.
 Cleanup - For an attacker, this means removing evidence of the attack while for a pen
  tester, this means removing any backdoors or tools and ensuring the system is not less
  secure than its pre-engagement state.




                                                                                                  165
```
