# eaas-deployment-e
EasS API deployment "e" with microk8s and docker. API backend not included. 

Also see https://github.com/jpegleg/eaas-deployment-d

Differences from deployment d in deployment e:

- no throttle in place by default in deployment e eaasapi config
- eaas api e default backend does not use gpg
- redis is available to the eaas api backend

...

Ideas in progress // TODO:

- include PHP fpm template
- Apache2 CGI template ( in progress eacgi container )
