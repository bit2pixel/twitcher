virtualenv twitcher_env
source twitcher_env/bin/activate
git clone git@github.com:bit2pixel/twitcher.git
pip install -r requirements.txt
./manage.py syncdb
./manage.py runserver