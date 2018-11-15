HealthChecker = `HC`
End of Run Monitor = `EoRM`

Motivation
==========

`EoRM` stops working after a certain amount of time being active. This time appears to be random.
The symptoms are that file updates of the `last_run.txt` file will no longer be found and as such the new runs will not be submitted to activemq.

Suggested solution
==================

Produce a service designed to check the health of the `EoRM` and restore autoreduction to a valid state if problems are detected.

Requirements
============

1. The `HC` must be able to detect when the `EoRM` is no longer detecting new runs
2. After detecting a problem, the `HC` must be able to restart the `EoRM` to allow it to resume activity
3. After detecting a problem, the `HC` must be able to submit the runs that were missed while `EoRM` was not in a working state
4. The `HC` must not directly interact with `EoRM` with the exception of restarting the service.
  * This is because we do not want take any processing cycle away from `EoRM` to ensure the `HC` is not causing `EoRM` to miss runs.

Proposed requirement solutions
==============================

1. Compare the most recent run in `ICAT` to the reduction database. Runs are added to the reduction database as soon as they are submitted so we should not have an issue with waiting for reduction of runs.
2. `HC` will have access to `EoRM.start()` and `EoRM.stop()` allowing it to restart the service
3. `HC` will already know the run difference between `ICAT` and the database which we can assume is equal to the difference between real time and `EoRM`.
   `HC` should be able to gather and resubmit all the data associated with a missing run.
4. `HC` runs in a separate execution thread and use `ICAT` and the database - hence does not hold up `EoRM` in any way.
