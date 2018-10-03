# Before we can add more compute nodes

## What is needed before we can do this

Move files currently on a samba share on the compute node. These files are e.g. calibration files which are (as of today WISH stores 1.1GB of these, although that may include old calibration files)

1. updated infrequently, typically start of cycle
2. loaded during each reduction run

Because of 2 it is a requirement that the compute node has fast load access to these, i.e. they can’t, for example, be loaded over a ‘slow’ network. 
Possible solutions:

* User accessible disk area somewhere not on a compute node. Have this synced with disk area on each compute node
* User accessible disk area somewhere not on a compute node, which each compute node have fast network access to. This assumes all compute node will access to a common storage disk area, which right now can be assumed true

Would there be any advantage of these being version controlled? Check with Pascal. Sometime in the future, to able to reproduce reduction results, these would need to be archived.  

## Highly desirable to do

To consider our reduction script location, which is currently located on \isis\inst$

Should these be located where at the same location as the calibration files?

For debugging etc. global version history of these make sense, e.g. GitHub repo. Although whether a pull or push model is best (need to check with Pascal). 
Longer term we would likely be attractive if these were only editable via the WebApp.

