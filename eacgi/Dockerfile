FROM debian
LABEL maintainer="carefuldata@protonmail.com"
LABEL version="1.0"
LABEL description="EaaS API CGI"

RUN apt-get update && apt-get install -y apt-transport-https aptitude && aptitude install -y openssl apache2
COPY apache2.conf /etc/apache2/apache2.conf
COPY cgi-sec.conf /etc/
COPY serve-cgi-bin.conf /etc/apache2/conf-enabled/
COPY secp384r1.cgi /var/www/html/
RUN ln -sf /dev/stdout /var/log/cgi.log
RUN a2enmod cgi

EXPOSE 80

CMD apachectl -D FOREGROUND

