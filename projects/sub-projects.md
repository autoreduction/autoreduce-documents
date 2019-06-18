# Autoreduction projects
## Web application graphical output
The web application is currently only being used in the as a high level overview for the status of reduction jobs. A request from instrument scientists has been to instead show a graphical representation of their reduced data.
This project would involve the following tasks:
* Agreeing the format which instrument scientists would like to see their data
* Producing a plot from the output reduced file
* Storing the plot in the database
* Adding that plot to the web application

Extension task:
* Be able to create a graph based on snapshots of the data taken during acquisition
* Talk to the IBEX team about adding this to their interface

## Web application testing
The web application is the main way in which users interact with autoreduction. As such we should look to ensure that this is well tested. With a combination of unit and system tests incorporating the test automation tool selenium, we hope to add testing to the web application. For the more complex use cases, we would want to have a separate machine to run these test once per day as to not interfere with the travis pipeline for testing. 
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
The autoreduction system currently runs on a single compute node, which is not a realistic long term solution. As such, we want to expand the system to be able to run on an expandable system to deal with increased system load. We have started to make progress towards this by creating an ansible script for automated creation of VMs that are setup to run autoreduction.
This project would involve the following tasks:
* Familiarisation with the ansible scripts
* Adding the ability to incorporate reduction software (such as MANTID) into ansible scripts
* Exploring options for managing VMs with regards to expanding and contracting services based on load requirements
* Implementing a system for doing this
* Testing and deployment of new system

## Queue Processors rewrite
The Queue Processor handles the flow control of the autoreduction system. It consumes and sends messages to the ActiveMQ messaging service to update the status of reduction jobs appropriately. The original code for this is poorly structured and in desperate need of improvement.
This project would involve the following tasks:
* Familiarising yourself with the current Queue Processor system
* Designing a new (cleaner) implementation for the queue processor
* Implementing your design for the queue processor
* Fully testing the system with a combination of unit and system tests.

