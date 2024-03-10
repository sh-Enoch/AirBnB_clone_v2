#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Output results
echo $?  # Output the exit status of the last command
ls -l /data
ls -l /data/web_static
ls /data/web_static/current
cat /data/web_static/current/index.html

# Restart Nginx
sudo service nginx restart

# Test if Nginx is serving the content correctly
curl localhost/hbnb_static/index.html
