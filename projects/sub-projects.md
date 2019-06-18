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

Potential extension bonus tasks:
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

## End of Run monitor rewrite
The end of run monitor is one of the core parts of the autoreduction system used to discover when new runs are created (and therefore should be processed). The current end of run monitor is considered to be fragile and over complex leading to an unstable solution. A new design has been produced to implement a much more straight forward system that sacrifices real-time run discovery for close to real time run discovery but much higher stability. 
This project would involve the following tasks:
* Learning the old and new designs for the end of run monitor
* Creating an improved testing framework to create a “fake” ISIS data archive
* Implementation of the new end of run monitor design
* Fully testing of the new monitor
* Rigorous manual testing
* Deployment onto development environment

## Autoreduction to be cloud compatible
The autoreduction system currently run on non-cloud enabled hardware, which by end of 2019-ish will not be able to provide enough compute resources to satisfy demand. As such, we want to expand the system to be able to run on an expandable system to deal with increased system load. We have started to make progress towards, including creating ansible scripts for automated creation of VMs on STFC/SCD cloud.
This project would involve the following tasks:
* Familiarisation yourself with the existing work done towards achieve this goal
* Exploring options for managing VMs with regards to expanding and contracting services based on load requirements
* As needed update software architecture documentation and views and agree on solution with relevant stakeholder  
* Implementing a system for doing this
* Testing and deployment of new system

## Queue Processor rewrite
The Queue Processor handles the flow control of the Autoreduction system. It consumes and sends messages to the ActiveMQ messaging service to update the status of reduction jobs appropriately. Due to the system evolving, it has been identified that this part of code code is in need of re-structuing and improvements.
This project would involve the following tasks:
* Familiarising yourself with the current Queue Processor system
* Designing a new and cleaner implementation for the queue processor
* Implementing your design for the queue processor
* Fully testing the system with a combination of unit and system tests.

