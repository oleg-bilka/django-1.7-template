#!/bin/bash

virtualenv --clear --distribute env
source env/bin/activate

easy_install curdling
curd install -r requirements.txt
