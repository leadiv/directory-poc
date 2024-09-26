# directory-poc
A proof of concept for using Planning Center for a read only directory

## FTP Information
The username, and the ftp host server can be found on the hosting admin
pages. If these are updated be sure to update the repository secrets as
well (`FTP_DEPLOY_USERNAME` and `FTP_DEPLOY_HOST` respectively). The
ftp password is not kept anywhere in plain text. A new password can
always be generated and updated on the hosting admin pages. Make sure
the secrets for the `FTP_DEPLOY_PASSWORD` on the repository is updated
as well.

For debug purposes a tempoary ftp account can be created and used
locally as outlined below.

## Debugging FTP Action
The deploy pipeline use the
[FTP Deploy Action](https://github.com/SamKirkland/FTP-Deploy-Action)
to push files up. If there is a need to test locally the configuration
do the following:

1. Run `npm install` from the root of this repository.
2. Use npx to run the ftp-deploy module. The deploy.yml `with` properties for the action should tranalate into commandline parameters.
3. Instead of secrets provide the FTP account username and password created to debug.

## Documention
For more documentation see the [wiki](https://github.com/leadiv/directory-poc/wiki) on this repository.
