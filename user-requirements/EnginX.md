09-04-2019
* [ ]Runs that are in the queued state are never removed and can not be removed by the user. If these runs are stuck in the queued state, it is impossible for the user to sbumit new runs manually.
* [x] Remove the first underscore from the `ENGINX_<run>_1.his` file so it reads `ENGINX<run>_1.his` (Mantid requirement)
* [ ]Investigate what happens with Event files. If these don't work in the Mantid script, ensure they are skipped in autoreduction and a helpful error message is displayed.
