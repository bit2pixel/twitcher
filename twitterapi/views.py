import json
from twython import Twython
from twython import TwythonAuthError

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from twitcher.settings import TWITTER_APP_KEY
from twitcher.settings import TWITTER_APP_SECRET
from twitcher.settings import TWITTER_OAUTH_TOKEN
from twitcher.settings import TWITTER_OAUTH_TOKEN_SECRET

twitter = Twython(TWITTER_APP_KEY,
                  TWITTER_APP_SECRET,
                  TWITTER_OAUTH_TOKEN,
                  TWITTER_OAUTH_TOKEN_SECRET)

@login_required
def timeline(request, screen_name):
    """Returns a collection of the most recent Tweets posted by the user.

    Args:
        request: Django request object
        screen_name: Twitter users screen name

    Returns:
        HttpResponse(content_type='application/json')
    """

    # How many tweets to show at a time
    count = request.GET.get('count', 10)

    # Twitter will only send the user_id instead of
    # the user object if set to True.
    trim_user = request.GET.get('trim_user', False)

    try:
        timeline = twitter.get_user_timeline(screen_name=screen_name,
                                             count=count,
                                             trim_user=trim_user)
    except TwythonAuthError:
        timeline = []

    content = json.dumps(timeline)

    return HttpResponse(content=content,
                        content_type='application/json')
