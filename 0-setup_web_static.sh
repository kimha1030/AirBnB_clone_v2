#!/usr/bin/env bash
# Task 0: Prepare your web servers
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p "/data/web_static/shared/"
sudo mkdir -p "/data/web_static/releases/test/"
echo -e "<html>\n<head></head>\n<body>Holberton School</body>\n</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
sudo sed -i "51i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
