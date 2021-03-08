from datetime import datetime, timedelta, timezone
import twitter
from creds import TWITTER_KEY, TWITTER_KEY_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET
from dateutil import tz

# twitter api object

api = twitter.Api(consumer_key=TWITTER_KEY,
                  consumer_secret=TWITTER_KEY_SECRET,
                  access_token_key=TWITTER_TOKEN,
                  access_token_secret=TWITTER_TOKEN_SECRET)


def removeTweets(tweet_age):
    ''' Removes tweets older than tweet_age (in seconds) '''

    statuses = api.GetUserTimeline(count=200)
    current_time = datetime.now().replace(tzinfo=tz.gettz("UTC"))

    if statuses:
        for tweet in statuses:
            created_at = datetime.strptime(tweet.created_at, '%a %b %d %H:%M:%S %z %Y')
            delta =  current_time - created_at

            if delta.total_seconds() > tweet_age:
                api.DestroyStatus(tweet.id)
                print('Deleted:', tweet.text)

removeTweets(86400)
# remove tweets that are older than a day
