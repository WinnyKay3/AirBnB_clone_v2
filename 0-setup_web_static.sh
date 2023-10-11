#!/usr/bin/env bash
# sets up web servers for deployment of web static
apt-get update
apt-get -y install nginx
ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
   </body>
  </html>" > /data/web_static/releases/test/index.html

  ln -s -f /data/web_static/releases/test/ /data/web_static/current

  chown -R ubuntu:ubuntu /data/

  printf %s "server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $HOSTNAME;
      root /var/www/html;
      index index.html index.htm;

      location /hbnb_static {
          alias /data/web_static/current;
	  index index.html index.htm;
      }

      location /redirect_me {
          return 301 http://youtube.com/;
      }

      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
	internal;
      }
   }" > /etc/nginx/sites-available/default

   ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

   service nginx restart

