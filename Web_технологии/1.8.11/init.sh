#!/bin/bash

mkdir -p ~/web/etc

cp -f ~/stepic.org/Web_технологии/1.9.11/etc/* ~/web/etc
cp -f ~/stepic.org/Web_технологии/1.9.11/web/* ~/web

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

# NEXT
# git clone https://github.com/your_account/stepic_web_project.git /home/box/web
# bash /home/box/web/init.sh