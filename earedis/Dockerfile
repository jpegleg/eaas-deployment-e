FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf
COPY users.acl /usr/local/etc/users.acl
EXPOSE 6379
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]
