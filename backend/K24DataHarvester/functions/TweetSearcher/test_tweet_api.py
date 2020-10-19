# python3 functions/TweetSearcher/test_tweet_api.py 
import json
import tweepy
from datetime import datetime

def _create_twitter_api1(twitter_key, twitter_secret_key):
    print("input:", twitter_key, twitter_secret_key)
    auth = tweepy.OAuthHandler(twitter_key, twitter_secret_key)
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    print("auth:", auth)
    api = tweepy.API(auth)
    # api = tweepy.API(auth, wait_on_rate_limit=True,
    #                 wait_on_rate_limit_notify=True)

    if (not api):
        raise Exception("Can't Authenticate")

    return api

def _create_twitter_api(twitter_key, twitter_secret_key):
    auth = tweepy.AppAuthHandler(twitter_key, twitter_secret_key)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)
    if (not api):
        raise ("Can't Authenticate")

    return api

api = _create_twitter_api1(twitter_key="key", twitter_secret_key="secret")
searchQuery="Karachi OR #Karachi OR karachi OR #karachi min_retweets:10 min_faves:10 -filter:replies -filter:images -filter:videos -filter:news geocode:24.874553,67.0398131,200mi"
tweet = api.search(q=searchQuery, count=1500, since_id="1312862399490220002", return_json=True) 
print(tweet)

