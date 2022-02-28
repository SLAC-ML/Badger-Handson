#!/bin/bash

xhost +localhost

export BADGER_ROOT=$PWD/playground
docker-compose run --rm --name badger-handson badger
