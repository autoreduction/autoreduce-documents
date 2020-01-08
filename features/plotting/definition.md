Final implementation:

It must be possible to view a variety of interactive plots of either one or more pecices of reduced data in the web application.
It must be possible to change the plot type on the fly, to view different aspects of the data depending on instrument requirements.
The plots must render on the page within an acceptable amount of time (ideally, no more than 5 seconds maximum. Most should load within 1 second)


Break down of feature:
1. Display a single interactive plot for the most recent run on the main page
2. Treat reduced data so that it can be accessed and plotted in a timely manor.
3. Display a single interactive plot for all runs on their run summary pages
4. Possible to display different styles of plots for a data set
5. Possible to display different information about the data set (e.g. detector image)
6. Possible to display a dataset that is a combination of several runs

Considerations:
* At what stage should data be treated (2):
  * On the fly: Longer time to render graphs (but may be acceptable)
  * At reduction time: Would mean storing additional files on CEPH
* How can we minimise execution and avoid high server load (if on the fly):
  * Cache plots locally?
    * How long do we cache for?
* How do we combine datasets automatically:
  * Will have to have IS input for this

