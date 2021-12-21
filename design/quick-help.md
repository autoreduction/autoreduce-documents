## User can't submit re-runs
They need to have an account in the webapp and an admin needs to add a token in https://reduce.isis.cclrc.ac.uk/tokens/.

This token is used when a rerun is submitted to authorize the request in the REST API:
https://github.com/autoreduction/autoreduce-rest-api/blob/main/autoreduce_rest_api/runs/views.py#L35

## How to add an admin?
Another admin has to go to https://reduce.isis.cclrc.ac.uk/admin/auth/user/, find the user, click their ID
then select the `Superuser status` and click `Save`.

## Where are the reduction scripts?
They are always at `\\isis\inst$\ndx<instrument>\user\scripts\autoreduction` or `/isis/user/scripts/autoreduction`
