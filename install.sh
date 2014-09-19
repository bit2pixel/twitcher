virtualenv twitcher
source twitcher/bin/activate
git clone git@twitcher
cd twitcher/twitcher
pip install -r requirements.txt
./manage.py syncdb
./manage.py runserver