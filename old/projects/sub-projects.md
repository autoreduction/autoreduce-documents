This page lists upcoming Autoreduction sub-projects, which are estimated to take anything between a month and a year to complete depending on skill level and the specific sub-project.

There are opportunities to get involved with any of these. Note, this list may from time to time get out of date and please don't hesitate to contact us to discuss getting involved with any of these sub-projects.

# Autoreduction sub-projects
## Enrich the script API to automatically upload and delete reduce data
Currently all data created during a reduction run gets stored to CEPH. Enhance the API so that authors can tag some output files to be automatically uploaded to the ISIS Data Catalogoue. With input from customers, enable methods that users can specify in reduce.py scripts that allows script authors to tag output files; this will also serve to encourage script authors to think about which files they want for short and long term. The long term stored files enabled with automatic upload to the isis data catalogue; will include cross testing and buffer mechanism to accommodate the situation where the catalogue is not available. It will involve close interactions with the catalogue team to ensure the data are inserted in the right place etc.

## Towards easier longer term reduction reproducibility
Autoreduction can already reproduce reduction data within its environment and within a given ISIS cycle and even to some extend older cycle up to the point where the software on the underlying compute nodes have not changed. For edging towards reduction reproducibility beyond this, either using Autoreduction or some other service / software package later in time, this needs tracking of both variables *and* the environment used to produce a reduced file. At present we can only track the variables. This work is to also track / store information about the environment used during reduction jobs. The first part of this sub-project would be to gather requirements for what environment information needs to be tracked and the ease/difficulty of gather such information, combined with a search for ideas for approaches to implement this.

## Web application dynamical graphical output
The web application has been extending to allow static ploting. This project is to extend it allow dynamical plotting. A request from instrument scientists.
This project would involve the following tasks:
* Agreeing the presentation which instrument scientists
* Producing a dynamical plot from the output reduced file
* Storing the plot in the database
* Adding that plot to the web application

## Autoreduction to be cloud compatible
The autoreduction system currently run on non-cloud enabled hardware, which is not easy to extend and by its nature is not elastic. As such, we want to expand the system to be able to run on an expandable system and to deal with increased system load. We have started to make progress towards, including creating ansible scripts for automated creation of VMs on STFC/SCD cloud.
This project would involve the following tasks:
* Exploring options with regards to expanding and contracting services based on load requirements, and in particular also handle the requirements:
  * any data reduction must start within seconds of completing on ISIS beamline experiment and at most within a minute
  * handling in the region of 10000 jobs over a cycle (growing with more beamlines using the service) and where each job on a 48 core, 128GB RAM machine takes anything from 10 seconds to 10 minutes to complete
* Make software and deployment changes to enabled favoured solution, together with detailed documentation on this and how to monitor, maintain and bug fix during cycles
* Setting up of suitable development environment for this, and complete a period of testing this environment and with Autoreduction team and well as with selected customers
* Extensive period of next testing on production and before an ISIS cycle starts, with a wider range of customers



