FROM debian
LABEL maintainer="carefuldata@protonmail.com"
LABEL version="1.0"
LABEL description="EaaS API CGI"

RUN apt-get update && apt-get install -y apt-transport-https aptitude && aptitude install -y openssl sec apache2
COPY httpd.conf /etc/apache2/httpd.conf
COPY cgi-sec.conf /etc/
RUN ln -sf /dev/stdout /var/log/cgi.log

EXPOSE 80

CMD ["/usr/bin/sec", "--conf=/etc/cgi-sec.conf", "--input=/var/log/apache2/access.log", "--log=/var/log/cgi.log", "--detach"]
CMD apachectl -D FOREGROUND
