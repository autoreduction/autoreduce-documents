Elliot kick-off graduate rotation 
=================================

9:30-11:30
* Anders: autoreduce-documents repo
* Jamie: demo where the system is now and in some detail on the current CEPH/ICAT storage/directory solution 
* Elliot: final year project and Selenium
* where we are going and what remains to be done in terms of improving stability and reliability to our current system and using our current compute infrastructure
* Schedule for roling out service to scientists based on the planned ISIS cycles
  * For cycle starting 17th April: Polaris, GEM, HRPD using Joe's script. Also simple dummy scripts for Polref, Musr, and dummy for OSIRIS which runs ~5 mins
  * This cycle: 17th April to 18th May. The following is 5th June. 
* Our development environment and password files on isis sharepoint site
  * Move start-up check-list to the wiki
  * sharepoint for private info. autoreduce-documents for minutes etc and autoreduce for code user installation etc
* Anders: explain issues with current compute infrastructure and all discuss how to improve this shorter term
  * We only one compute node in production, but in dev enviroment we should test with multiple compute nodes
  * Move where scripts are stored (currently \\isis\inst$\NDXWISH\users...) to where calibration files are stored - thereby remove dependency. Create Issue for this
  * Nice to have: Create cron job for uploading script to github repository for users and us to see global history. Create seperate github user, which could be isisautoreduce, and seperate repository, which could be autoreduce-cron
  * Currently wipe MySQL manually before each cycle - automate this and how best? Probably could extend this to a longer period with current setup without seeing a significant reduction in how the WebApp performs and responds to user interactions
* Anders: Remaining smaller concerns with 3rd party software service dependencies and all discuss these
  * For end of run monitor script. Should we have a fallback to monitor ICAT also for new jobs. Create an issue for this
  * For webapp authentication (done through user-office) and authorisation (ICAT)
  * Mantid, install manually ourselves or through FIT servicedesk. Communication with FIT servicedesk on when to update Mantid
* Nice to tackle/investigate tasks:
  * Inestigation into using STFC cloud for compute infrastructure. Anders: status on STFC cloud
  * Making the webapp viewable outside the lab
    * Discuss work estimate for this and evaluate risk/pros/cons/concerns of this
  * Making the WebApp control how users can edit reduction scrips
    * flesh out predicted work units and predicted estimates for this
  * Storing data going into and going out of autoreduce into catalogue 
  (as discussed [data management](/meetings/2018-7th-Mar-data-management.md))
    * flesh out predicted work units and predicted estimates for this

13:00-16:00
* Create remaining issues
* Create workplan and get started

