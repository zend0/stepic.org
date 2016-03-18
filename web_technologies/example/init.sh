#!/bin/bash

RootDir=/home/box/web

if [ ! -d $RootDir ]; then
    mkdir -p $RootDir
fi

cp -rf ~/stepic.org/web_technologies/example/* $RootDir

# MySQL
if [ ! -d /var/lib/mysql/mysql ]; then
    mkdir -p /var/lib/mysql
    chown -R mysql:mysql /var/lib/mysql
    mysql_install_db

    #trap "mysqladmin shutdown" TERM
    mysqld_safe &
    #wait
    sleep 5
    mysqladmin -u root password ''
    mysql -u root -e 'GRANT ALL ON *.* TO root@"%" IDENTIFIED BY "" WITH GRANT OPTION'
    mysql -u root -e 'GRANT ALL ON *.* TO root@"localhost" IDENTIFIED BY "" WITH GRANT OPTION'
    mysql -u root -e 'FLUSH PRIVILEGES'
fi

sudo /etc/init.d/mysql restart

# Create DB for 'examp'
mysql -u root -e 'CREATE DATABASE IF NOT EXISTS examp'
mysql -u root -e 'GRANT ALL PRIVILEGES ON ask.* TO examp@"%" IDENTIFIED BY "passwd"'
mysql -u root -e 'GRANT ALL PRIVILEGES ON ask.* TO examp@"localhost" IDENTIFIED BY "passwd"'
mysql -u root -e 'FLUSH PRIVILEGES'

# Nginx and Gunicorn

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf $RootDir/etc/nginx.conf /etc/nginx/sites-enabled/web.conf
sudo /etc/init.d/nginx restart

sudo ln -sf $RootDir/etc/gunicorn.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart

# NEXT
# git clone https://github.com/your_account/stepic_web_project.git /home/box/web
# bash /home/box/web/init.sh
