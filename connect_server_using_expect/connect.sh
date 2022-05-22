#!/bin/bash
# A Shell script to connect target server through kerberos gateway server
# Wriiten by: Jaekwon.ha
# Last updated on: 2022.05.22

PATH=""
GATEWAY=$1
GATEWAY_PW=""
KERBEROS_PW=""
HOST_USER=""
HOST=$2
YUBIKEY=""

if [[ $GATEWAY == "" ]]; then
  echo "TOUCH Yubikey:"
  read -s YUBIKEY
fi

/usr/bin/expect -f $PATH/expect.exp $GATEWAY $GATEWAY_PW $KERBEROS_PW $HOST_USER $HOST $YUBIKEY
