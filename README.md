# eaas-deployment-e
EasS API deployment "e" with microk8s and docker. API backend not included. 

Also see https://github.com/jpegleg/eaas-deployment-d

Differences from deployment d in deployment e:

- eaas api is not throttled to 1/TPS per cluster, no throttle in place by default in deployment e eaasapi config
- eaas api backend does not use gpg
- redis is available to the eaas api backend

