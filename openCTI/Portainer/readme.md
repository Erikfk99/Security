# INSTALLATION of Portainer on Ubuntu server
We will be installing Docker using the APT repository before installing portainer.

This will install the latest version of docker 

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
3. Install the Docker Packages
   1. `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
4. Verify docker Engine with running hello-world image
   1. `sudo docker run hello-world`

## Portainer CE version installation 
Steps can be followed here: [portainer guide](https://docs.portainer.io/start/install-ce/server/docker/linux)
1. create a volume for portainer
   1. `sudo docker volume create portainer_data`
2. Get latest of Portainer 
   1. Change 8000 to 18000 to not interfere with Opencti down the road
   2. `sudo docker run -d -p 18000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest`
   3. Check portainer is running with: `sudo docker ps`
3. Go to localhost:9443 on the server, or incase you have bridged the network adapter go to IP:9443 on your computer


