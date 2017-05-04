apt-get -y install apache2
apt-get -y install php5
apt-get -y install mysql-server
apt-get -y install mysql-client
apt-get -y install openssl
apt-get -y install bash
apt-get -y install phpmyadmin


rm /var/www/html/index.html
cp index.php /var/www/html/index.php
cp ajax.php /var/www/html/ajax.php
cp robots.txt /var/www/html/robots.txt
cp jquery-1.12.3.min.js /var/www/html/jquery-1.12.3.min.js
cp jquery.js /var/www/html/jquery.js

