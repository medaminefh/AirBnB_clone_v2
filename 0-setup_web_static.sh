#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "Index Page" | tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
if ! sudo grep -q 'location /hbnb_static/' /etc/nginx/sites-available/default; then
    sudo sed -i '42i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
fi
sudo service nginx restart
