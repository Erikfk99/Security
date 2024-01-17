# Reverse proxy 
I have created a reverse proxy to my virtualbox instances to be able to access my services from anywhere in the world 

# NGINX

1. download nginx 
2. go to /etc/nginx/sites-avaliable/your-domain
   1. sudo vi domain.com
   2. add code server etc (fill me) 
3. link domain 
   1. sudo ln -s /etc/nginx/sites-available/your-domain /etc/nginx/sites-enabled/
4. port forwarding on your router 



# Adding SSL (HTTPS) https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04

https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1

