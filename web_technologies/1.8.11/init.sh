#!/bin/bash

HomeDir=/home/box/web

if [ ! -d $HomeDir ]
then
    mkdir -p $HomeDir
fi

cp -rf ~/stepic.org/web_technologies/web/* $HomeDir

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf $HomeDir/etc/nginx.conf /etc/nginx/sites-enabled/web.conf
sudo /etc/init.d/nginx restart

sudo ln -sf $HomeDir/etc/gunicorn.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

# NEXT
# git clone https://github.com/your_account/stepic_web_project.git /home/box/web
# bash /home/box/web/init.sh
