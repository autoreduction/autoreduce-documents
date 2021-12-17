## Feasability
#### System Scope
* One test per page
* Test typical workflows (limited to a small number)

#### Frequency
* Nightly? 

#### Browser coverage
* Chrome / FireFox / Edge / Safari (if nightly)

#### Local running considerations
* Adding docs to wiki that link to good resources


## Framework
#### Selenium instance persistance
* New session per workflow
* Consider options with testing individual pages
  * start with new session per page

#### Code base integration
* Templating selenium tests
* Transferability

#### Test Scope
* Element existence
* Test button / page links are correct
* Form submission
* Basic assert on data correctness

#### Next steps
* Try to break web app with random button / form submission / etc.
  * record these and ensure they are reproducible
