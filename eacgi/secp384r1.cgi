#!/usr/bin/env bash

echo "Content-Type: text/html";
echo
echo "$(openssl ecparam -name secp384r1 -genkey -noout)"
echo
