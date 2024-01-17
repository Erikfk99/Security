# Insattling phishunt connector to opencti
Phishunt is a paid service, so there is a free way of implementing this and a paid version 

## Free
1. Add the phishunt.yaml file to your OpenCTI stack
2. add the phishunt.env to your variables in portainer
   1. create a UUIDV4 token for the connector id (marked with Changeme in env file)
3. Do not add anything to API key section of the yaml as this is optional

## Paid
Follow the steps above only that you add API key. I would recommend adding that as a variable.