#!/usr/bin/env bash
# placeholder cgi script for template
echo "Content-Type: text/html";
echo
echo "$(openssl ecparam -name secp384r1 -genkey -noout)"
echo
