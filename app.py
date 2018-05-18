from datetime import datetime
import json
import tweepy
from creds import TWITTER_KEY, TWITTER_KEY_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET

# format 2018-05-12 17:18:34
# dt object directives:
# %Y-%m-%d %H:%M:%S
#api.destroy_status(status_id)

# twitter api object

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_KEY_SECRET)
auth.set_access_token(TWITTER_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

def removeTweets():
    ''' Removes tweets older than 24 hours '''
    tweets = api.user_timeline(count=100)
    current_time = datetime.now()
    if tweets:
        for tweet in tweets:
            created_at = datetime.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S')
            delta =  current_time - created_at

            # 86400 seconds in a day
            if delta.total_seconds() > 86400:
                api.destroy_status(tweet.id)
                # print('Deleted ' + tweet.text)

removeTweets()
