## Reasons for rewritting the database

### Functional:

1. Autoreduction must be able to support multiple runs associated with a single job in order to be fit for purpose for SANS / Reflectometry
  * Specific example is: Reflectometry experiments have runs at different angles to the sample. In order to gather meaningful information about the experiment, these should be stitched together and displayed. This would mean collating multiple runs into a single reduction job.
2. Autoreduction must be able to cater for enum type variables 
  * The value of these should be able to be set or automatically discovered
  * This will allow instruemnt scientists to constrain the available options for parameter values given to users
3. Autoreduction should store information about the software + version used to reduce data
  * To work towards being able offer better function for reproducing past runs either external to or within Autoreduction services
4. Autoreduction should be able to track all the files it outputs (not just a path to the directory) and the type of file they are
  * This will allow some instrument better understanding of their data (e.g. MARI outputs several different Ei value files - for which the Ei value is automatically generated)
  * (Non-function): Additionally this will make it easier for the system to identify plotting files and their locations meaning we do not have to make assumptions about naming conventions.

### Non-functional:

1. Autoreduction needs better performance when accessing pages (currently slow due to large amounts of database duplication)
  * requirement: less than 2 seconds to access any individual run page
2. Autoreduction should use a single ORM as to not needlessly inflate the code base, thereby improving maintainability


The current Schema does not allow for any of the above without significant rewrite or highly complex code to manipulate the records.
