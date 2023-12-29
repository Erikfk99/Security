# INSTALLATION of Portainer on Ubuntu server
We will be installing Docker using the APT repository before installing portainer.

## Requirments: 
- Docker installed on VM (refrence link)
- Follow download of Docker here: [Docker Docs](https://docs.docker.com/engine/install/ubuntu/)

### Check docker is installed
- Update apt get: `sudo apt-get update`
- Check version: `docker --version`

## Docker installation:
1. uninstall conflicting packages: 
   1. `for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done`
2. Set up Dockers APT repository:
   1. > `#Add Docker's official GPG key:
      > sudo apt-get update
      > sudo apt-get install ca-certificates curl gnupg
      > sudo install -m 0755 -d /etc/apt/keyrings
      > curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
      > sudo chmod a+r /etc/apt/keyrings/docker.gpg
      > #Add the repository to Apt sources:
      > echo \
      >  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      >  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      >  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
      > sudo apt-get update`

