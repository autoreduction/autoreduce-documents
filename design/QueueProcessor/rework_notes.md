Queue Processor Rework Notes
============================


Discussion Points:
----------------------

- data_ready() currently creates instruments in the DB on the fly, is this expected?
- Is there a way to poll Active MQ to see if messages are waiting
  (we could process all then exit. A lock file in /tmp ensures we don't start two) 


Tidy-Up Opportunities:
----------------------

- Add Stomp interface classes (e.g. on_message)
- Throw instead of returning strings 
- Python 2 style classes (missing Object superclass)
- Move hard-coded queue names up to module scope (for testing)
- Drop "except Exception:" since some, like OOM, we should not handle
- DI Database
- Unified "order by" for versions
- Split out handling and message queueing: Base handler then
  deriving classes which implement each step such as `data_ready`