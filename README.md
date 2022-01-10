# eaas-deployment-e
EasS API deployment "e" template on linux with docker for a single node.

This is a collection of docker containers and a few scripts, used as a starting place template.

The deployment itself needs about 400 MB of RAM and about 4 GB of disk out of the box.

As per usual with these templates, the actual app is not included (ACCOUNT-api). 

This one is set up for using docker local networks for the backend within the deployment.

There are CGI script examples in the eacgi container.

Also see 
https://github.com/jpegleg/eaas-deployment-d 
https://github.com/jpegleg/eaas-deployment-f
