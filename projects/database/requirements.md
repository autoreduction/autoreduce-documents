## Reasons for rewritting the database

### Functional:

1. Autoreduction must be able to support multiple runs associated with a single job in order to be fit for purpose for SANS / Reflectometry
  * *Specific example is: Could you provide example thanks?*
2. Autoreduction must be able to cater for enum type variables 
  * The value of these should be able to be set or automatically discovered
  * *Elliot is this functional, i.e. to enable new behaviour or function?*
3. Autoreduction should store information about the software + version used to reduce data
  * To work towards being able offer better function for reproducing past runs either external to or within Autoreduction services

### Non-functional:

1. Autoreduction needs better performance when accessing pages (currently slow due to large amounts of database duplication)
  * requirement: less than 2 seconds to access any individual run page
2. Autoreduction should use a single ORM as to not needlessly inflate the code base, thereby improving maintainability
3. Autoreduction should be able to track all the files it outputs (not just a path to the directory) and the type of file they are
  * *Elliot what will this enable and is it functional or non-functional?*

The current Schema does not allow for any of the above without significant rewrite or highly complex code to manipulate the records.
