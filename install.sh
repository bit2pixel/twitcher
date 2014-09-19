virtualenv twitcher_env
source twitcher_env/bin/activate
pip install -r requirements.txt
mv config.ini.example config.ini
echo
echo "Don't forget to fill your config.ini file"
echo
./manage.py syncdb
./manage.py runserver