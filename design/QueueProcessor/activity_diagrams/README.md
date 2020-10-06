Queue Processor Activity Diagrams
=================================

- The Queue Processor registers a listener to Active MQ
- When a message is sent `on_message()` runs. This is documented in `message_handling`
- Depending on the queue the message came from one of the message handling branches is called

For example:

If we get data from `/queue/DataReady` the method calls `data_ready` which is 
documented in its own file

- Some Queue Handlers will call others, for example `reduction_error()`
- Once the handler is finished the script will either loop waiting for another message
- (TODO) or close down if there are no pending messages