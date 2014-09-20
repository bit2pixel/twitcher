#!/usr/bin/env python

import ConfigParser
import random
import string
from twython import Twython

print
print "==============================================================="
print "                   ~  CONFIGURE TWITCHER  ~"
print "          Please complete the following instructions."
print "==============================================================="
print
print

Config = ConfigParser.ConfigParser()

SECRET_KEY = ''.join([random.SystemRandom().choice(
    "{}{}{}".format(string.ascii_letters, string.digits, string.punctuation)) for i in range(50)])

SECRET_KEY = SECRET_KEY.replace('%', '_')

# WRITE DJANGO SECRET
Config.add_section('DJANGO')
Config.set('DJANGO', 'SECRET_KEY', SECRET_KEY)

print
print "==============================================================="
print "Please go to https://apps.twitter.com and create a new app now."
print "After creating, please complete the following instructions."
print "==============================================================="
print
print

TWITTER_APP_KEY = raw_input('Enter your API key -> ')
TWITTER_APP_SECRET = raw_input('Enter your API secret -> ')

twitter = Twython(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth = twitter.get_authentication_tokens()

TEMP_TWITTER_OAUTH_TOKEN = auth['oauth_token']
TEMP_TWITTER_OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print
print "==============================================================="
print "Please authenticate the app by clicking the following url -> "
print "%s" % auth['auth_url']
print
print "          You will receive a PIN CODE. Enter below."
print "==============================================================="
print
print

twitter = Twython(TWITTER_APP_KEY, TWITTER_APP_SECRET,
                  TEMP_TWITTER_OAUTH_TOKEN, TEMP_TWITTER_OAUTH_TOKEN_SECRET)

OAUTH_VERIFIER = raw_input('Enter your PIN CODE -> ')
final_step = twitter.get_authorized_tokens(OAUTH_VERIFIER)

TWITTER_OAUTH_TOKEN = final_step['oauth_token']
TWITTER_OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

# WRITE TWITTER SECRETS
Config.add_section('TWITTER_API')
Config.set('TWITTER_API', 'TWITTER_APP_KEY', TWITTER_APP_KEY)
Config.set('TWITTER_API', 'TWITTER_APP_SECRET', TWITTER_APP_SECRET)
Config.set('TWITTER_API', 'TWITTER_OAUTH_TOKEN', TWITTER_OAUTH_TOKEN)
Config.set('TWITTER_API', 'TWITTER_OAUTH_TOKEN_SECRET', TWITTER_OAUTH_TOKEN_SECRET)

# CREATE THE CONFIG FILE
config_file = open('config.ini', 'w')
Config.write(config_file)
config_file.close()
