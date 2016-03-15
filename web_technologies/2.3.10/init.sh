#!/bin/bash

RootDir=/home/box/web

if [ ! -d $RootDir ]; then
    mkdir -p $RootDir
fi

cp -rf ~/stepic.org/web_technologies/web/* $RootDir

# MySQL
if [ ! -d /var/lib/mysql/mysql ]; then
  mkdir -p /var/lib/mysql
  chown -R mysql:mysql /var/lib/mysql
  mysql_install_db
fi

#trap "mysqladmin shutdown" TERM
mysqld_safe &
#wait
sleep 5
mysqladmin -u root password ''
mysql -u root -e 'GRANT ALL ON *.* TO root@"%" IDENTIFIED BY "" WITH GRANT OPTION'
mysql -u root -e 'GRANT ALL ON *.* TO root@"localhost" IDENTIFIED BY "" WITH GRANT OPTION'
mysql -u root -e 'FLUSH PRIVILEGES'

# Create DB for ask
mysql -u root -e 'CREATE DATABASE ask'
mysql -u root -e 'GRANT ALL PRIVILEGES ON ask.* TO ask@"%" IDENTIFIED BY "passwd"'
mysql -u root -e 'GRANT ALL PRIVILEGES ON ask.* TO ask@"localhost" IDENTIFIED BY "passwd"'
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
