#!/usr/bin/env bash

if test -f /var/tmp/chain.dat; then
  echo "Content-Type: text/html";
  echo
  chained="$(date +%Y%m%d%H%M%S%N)_$(openssl rand -hex 12),trxnid=$(sha256sum /var/tmp/chain.dat | cut -d' ' -f1)"
  echo $chained >> /var/tmp/chain.dat
  echo $chained
  echo
else
  echo "Content-Type: text/html";
  echo
  chaos=$(cat /dev/urandom | base64 | fold -128 | head -n1)
  echo $chaos > /var/tmp/chain.dat
  echo "starting new chain..."
  echo "seed is $chaos"
  echo
fi
