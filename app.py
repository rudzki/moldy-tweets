from datetime import datetime
import tweepy
from creds import TWITTER_KEY, TWITTER_KEY_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET

# twitter api object

auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_KEY_SECRET)
auth.set_access_token(TWITTER_TOKEN, TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

def removeTweets(tweet_age):
    ''' Removes tweets older than tweet_age (in seconds) '''

    tweets = api.user_timeline(count=100)
    current_time = datetime.utcnow()

    if tweets:
        for tweet in tweets:
            delta =  current_time - tweet.created_at
            if delta.total_seconds() > tweet_age:
                api.destroy_status(tweet.id)
                print('Deleted:', tweet.text)

removeTweets(86400)
# remove tweets that are older than a day
