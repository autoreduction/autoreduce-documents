Agenda
------
* Discuss data management with Tom and data going in and out of autoreduce
Minutes/outcomes
-------
Attendees: Anders, Jamie, Elliot and Tom

* Should not use ICAT just to upload data from MySQL for the purpose of repopulating the webapp interface later.
If we need longer term storage for data to go back into WebApp a separate data solution is needed
(as well as upgrade to the Webapp to be able to cope responsively with serving longer history of data) 
* Look to move reduce.py scripts to local storage area, that selected users can access. 
Scripts could be edited by the webapp and longer term perhaps only allow this option.
* For outputted reduced data. E.g. control upload to ICAT with Python syntax. 
One suggestion is for 1st version have no versioning with ICAT; if job re-run overwrite what is already in ICAT; 
use whatever is most convenient for this and then adjust
* Reduce.py and the log file should be stored with any reduced data uploaded, this providing meta information about how the data was 
reduced. Preferably also any calibration files used. This can be done as a 2nd step, where this may be solved by one of the 
following approaches:
  * Python syntax where users specifies what calibration is used, or perhaps easier by forcing user to specify a partial or full path of 
calibration files, a location which we know 
  * using software that checks what files a given process is loading and saving
