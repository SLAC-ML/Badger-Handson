#!/bin/bash

xhost +localhost

export BADGER_ROOT=$PWD/playground
docker-compose run --name badger-handson badger
