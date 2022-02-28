#!/bin/bash

xhost -localhost

docker rm -f badger-handson &> /dev/null
echo "Badger related docker containers have been removed"
