## User can't submit re-runs
They need to have an account in the webapp and an admin needs to add a token in https://reduce.isis.cclrc.ac.uk/tokens/.

This token is used when a rerun is submitted to authorize the request in the REST API:
https://github.com/autoreduction/autoreduce-rest-api/blob/main/autoreduce_rest_api/runs/views.py#L35

## How to add an admin?
Another admin has to go to https://reduce.isis.cclrc.ac.uk/admin/auth/user/, find the user, click their ID
then select the `Superuser status` and click `Save`.

## Where are the reduction scripts?
They are always at `\\isis\inst$\ndx<instrument>\user\scripts\autoreduction` or `/isis/user/scripts/autoreduction`

## Where are the run-detection last runs saved?
SSH into the run-detection node (check https://openstack.stfc.ac.uk/project/instances/) then change user to the
value of `autoreduction_user` from the ansible production vault.

Then lastruns.csv can be found at `~/.autoreduce/lastruns.csv`

## Packages, containers and deployment
Most repos will build packages on a PR merge into master, when the builds are successful.

Manual packages can be built & published via `make` or `make package` (consult the `Makefile`)
if something doesn't work. You will need to login into pypi locally using the autoreduce pypi account (check Keeper)
or add your personal account with the autoreduce pypi account and use that.

To build & update containers for each one check the
[Makefile in autoreduce-containers](https://github.com/autoreduction/autoreduce-containers/blob/main/Makefile)

To deploy to production check the [Makefile in ansible](https://github.com/autoreduction/ansible/blob/main/Makefile)
