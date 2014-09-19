#!/bin/bash

virtualenv twitcher_env
source twitcher_env/bin/activate
pip install -r requirements.txt
mv config.ini.example config.ini
./configure.py
source twitcher_env/bin/activate
./manage.py syncdb
./manage.py runserver