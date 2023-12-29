# INSTALLATION of Portainer on Ubuntu server

## Requirments: 
- Docker installed on VM (refrence link)
- Follow download of Docker here: [Docker Docs](https://docs.docker.com/engine/install/ubuntu/)

### Check docker is installed
- Update apt get: `sudo apt-get update`
- Check version: `docker --version`

## Docker installation:
1. uninstall conflicting packages: 
   1. `for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done`