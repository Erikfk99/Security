# Adding connectors too OpenCTI
Here you will find a collection of connectors where all will have its 
own innstallation readme. Though here on this page you will find what is normal for all installations. 

## Connectors OPENCTI
When deploying OPENCTI with portainer than adding connectors is prettu straight forward. Some connectors are as simple as to only add the "docker-compose.yml" to your stack and the connector is up and running, these are usally "external connectors" such as AlienVault. 

"Internal connectors" usally implies that you need a server which has the product you are trying to connect preloaded such as "MISP". These services can be used togheter other places as with Sentinel.

## Installation of Connectors
All connectors that is installed here comes from [OpenCTI-Platform Connectors Github](https://github.com/OpenCTI-Platform/connectors) and you will find all you need there to install it. Here I have copied the files and added a bit of explination. 

When installing the connectors we add the Docker-compose.yml file from the connector to the stack we have in our portainer. When looking at the YML file we can see that it has a version template.