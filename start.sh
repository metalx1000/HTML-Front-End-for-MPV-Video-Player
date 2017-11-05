#!/bin/bash

if [ ! -f "/bin/busybox" ]
then
  echo "Busybox Needed."
  echo "installing busybox"
  sudo apt update && sudo apt install busybox
fi

echo "Starting Busybox..."
busybox httpd -p8080 && echo "Busybox Started on port 8080" || echo "Busybox Server Failed..."
