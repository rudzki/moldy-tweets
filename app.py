from datetime import datetime
import tweepy
from creds import TWITTER_KEY, TWITTER_KEY_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET

# twitter api object

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_KEY_SECRET)
auth.set_access_token(TWITTER_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

def removeTweets():
    ''' Removes tweets older than 8 hours '''

    # check the last hundred tweets
    # you should do an initial purge
    # and not tweet more than 100 times per 8 hours
    # which would indicate a problem that no script could fix

    tweets = api.user_timeline(count=100)

    current_time = datetime.utcnow()

    if tweets:
        for tweet in tweets:
            delta =  current_time - tweet.created_at
            if delta.total_seconds() > 28800: # 28800 seconds = 8 hours
                api.destroy_status(tweet.id)
                # print('Deleted ' + tweet.text)

removeTweets()
