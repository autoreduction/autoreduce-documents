The reasons for rewritting the database are as follow:
* Autoreduction must be able to support multiple runs associated with a single job in order to be fit for purpose for SANS / Reflectometry
* Autoreduction needs better performance when accessing pages (currently slow due to large amounts of database duplication)
* Autoreduction should use a single ORM as to not needlessly inflate the code base
* Autoreduction must be able to cater for enum type variables 
  * The value of these should be able to be set or automatically discovered
* Autoreduction should store information about the software + version used to reduce data
* Autoreduction should be able to track all the files it outputs (not just a path to the directory) and the type of file they are

The current Schema does not allow for any of the above without significant rewrite or highly complex code to manipulate the records.
