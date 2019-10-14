This page lists upcoming Autoreduction sub-projects, which are estimated to take anything between a month and a year to complete depending on skill level and the specific sub-project.

There are opportunities to get involved with any of these. Note, this list may from time to time get out of date and please don't hesitate to contact us to discuss getting involved with any of these sub-projects.

# Autoreduction sub-projects
## Web application graphical output
The web application is currently being used to view, in a textual manner, the status of reduction jobs. A request from instrument scientists has been to also show a graphical representation of their reduced data.
This project would involve the following tasks:
* Agreeing the format which instrument scientists would like to see their data
* Producing a plot from the output reduced file
* Storing the plot in the database
* Adding that plot to the web application

Potential extension tasks:
* Be able to create a graph based on snapshots of the data taken during acquisition
* Talk to the IBEX team about adding this to their interface

## Web application testing
The web application is a way in which users can monitor and interact with Autoreduction and it is used by support to monitor the system. A sub-project is to add automated testing to this part of the system also, with a combination of unit and system tests incorporating the test automation tool Selenium. For the more complex use cases, we would want to have a separate machine to run these test less frequently, once per day, as to not interfere with the travis testing pipeline. 
This project would involve the following tasks:
* Familiarising yourself with Selenium
* Creating test cases to perform common workflows on the web application
* Evaluating the best choice for automated testing
* Setting up an automated testing instance on an external machine to run these tests
*	Ensuring that the automated testing interfaces with git to get most up to date version of code base
* Making the tests run on the machine externally accessible

## Autoreduction to be cloud compatible
The autoreduction system currently run on non-cloud enabled hardware, which by end of 2019-ish will not be able to provide enough compute resources to satisfy demand. As such, we want to expand the system to be able to run on an expandable system to deal with increased system load. We have started to make progress towards, including creating ansible scripts for automated creation of VMs on STFC/SCD cloud.
This project would involve the following tasks:
* Familiarisation yourself with the existing work done towards achieve this goal
* Exploring options for managing VMs with regards to expanding and contracting services based on load requirements
* As needed update software architecture documentation and views and agree on solution with relevant stakeholder  
* Implementing a system for doing this
* Testing and deployment of new system

## Database optimisations (Pending)
* We may be moving to a new database maintained by SCD so this might not be in our scope. Will complete if required (14/10/2019)

## Reduction Configuration
For reproducabiity, it's important that we can trak the exact variables and environment used to produce a reduced file. At present we can only track the variables. It'll be important to also include the docker container used and a way to use it again. For the use of other projects, applications of autoreduction it is important to make this more generic. 
* Define a configuration file that states all the input / output parameters of a processing job
* Allow the QueueProcessors to operate with these configuration files.
* Ensure that ISIS data can construct these configuration files 
* Ensure all the relevant meta data is captured to allow for reproducability of processing

## Monitoring the Workflow
It would be great to have the ability to see the full state of the data pipeline from start to finish for ISIS data. 
Specifically this would include:
* Data acquisition (file in file system)
* Ingestion into ICAT (ICAT API call) 
* Autoreduction ingestion and status (Autoreduction DB call) 
* Autoreduction completion and available in CEPH (AR DB and inspect ceph)
