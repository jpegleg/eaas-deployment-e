#!/usr/bin/env bash

if test -f /var/tmp/chain.dat; then
  echo "Content-Type: text/html";
  echo
  chain=$(sha256sum /var/tmp/chain.dat | cut -d' ' -f1),$(echo $1 | sha256sum | cut -d' ' -f1),$(date +%y%m%d%H%M%S%N)_$(openssl rand -hex 16)_id
  echo $chain >> /var/tmp/chain.dat
  echo "$chain"
  echo
else
  echo "Content-Type: text/html";
  echo
  echo "Chain init at $(date +%y%m%d%H%M%S) with chaos of $(cat /dev/urandom | base64 | fold -128 | head -n1 | tr -d '\n')" | tee /var/tmp/chain.dat
  echo
fi
