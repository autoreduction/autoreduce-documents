## What is an ORM
An ORM (object relational mapping) is a framework used to perform some mapping between classes and objects to tables and records in a database.
Using an ORM give the advantage of being able to access databases without writting raw SQL.
This therefore makes database records more readable and easier to access from code. 

### Current implementation
There are currently 2 ORMs in use in autoreduction:
* `Django ORM`
* `SQLAlchemy`

As the name suggests, `Django ORM` is specific to the django python web framework. We use `Django ORM` to access database records and display them within the web application.
In addition, the `Django ORM` is used to initialise the Autoreduction database and therefore contains the specific information on the tables, fields and types used in the database.
`Django ORM` has both the access and building of the database rolled into one.
`Django ORM` requires the database to be a relational databases and offically supports read/write to `PostgreSQL`, `MariaDB`, `MySQL`, `Oracle` and `SQLite` (with some other third party libraries supporting other systems).   

`SQLAlchemy` is a stand alone python library used for writing, reading, building and accessing databases written in SQL style languages.
In autoreduction we use this ORM to access the database from the queue processor code.
In order to access the database, we create an ORM mapping file in python that defines a mapping between Database tables and python classes.
This is not difficult to implement as you are not required to redefine all the fields on a table (this is done for you) but you do need to add the realtionships between tables to the python classes manually. 

### Problems with current implementation
* 2 different database access mechanisms in the project
* `SQLAlchemy` implementation is abstracted from the underlying schema design so if a relationship was to change it would have to updated in both. 
* API's are different

## Proposed approach
Remove `SQLAlchemy` implementation in favour of using the `Djagno ORM` throughout the project

### Advantages
* Only have one ORM in the project
* Model and access will be together
* Avoid redfinition of ORM classes
* Only one API

### Disadvantages
* Will have to use `Django ORM` outside of Django
* Might have to change `DatabaseClient` to work with `Django ORM`

### Considerations
* What actually is running to use `Django ORM`? Is it a whole lightweight webapp? 
* How much of the code base will have to change
* What affect will this have on current and future testing
* Will the `Django ORM` be in anyway tied to the running web application? 
