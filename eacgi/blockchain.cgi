#!/usr/bin/env bash

if test -f /var/tmp/chain.dat; then
  echo "Content-Type: text/html";
  echo
  chained="$(date +%Y%m%d%H%M%S%N)_$(openssl rand -hex 12),trxnid=$(sha256sum /var/tmp/chain.dat | cut -d' ' -f1)"
  echo $chained >> /var/tmp/chain.dat
  echo $chained
  ssecr=$(openssl rand -hex 28)
  echo $ssecr > /var/tmp/$ssecr
  echo $chained > /var/tmp/$ssecr.chain
  openssl enc -pbkdf2 -aes256 -base64 -k $(base64 /var/tmp/$ssecr) -e -in /var/tmp/$ssecr.chain -out /var/tmp/segment.evbin
  cat /var/tmp/segment.evbin | xxd -p >> /var/tmp/chain.dat
  echo "one time secret is: $ssecr"
  echo
else
  echo "Content-Type: text/html";
  echo
  chaos=$(cat /dev/urandom | base64 | fold -128 | head -n1)
  echo $chaos > /var/tmp/chain.dat
  echo "starting new chain..."
  echo "seed is $chaos"
  echo "$chaos" > /var/tmp/seed.chain
  echo
fi
