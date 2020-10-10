import json
import boto3
import tweepy
from datetime import datetime
import os 

def _get_env_params():
    env = os.environ['Environment']
    twitter_key = os.environ['TwitterKey']
    twitter_secret_key = os.environ['TwitterSecretKey']
    bucket_name = os.environ['InputBucketName']
    root_folder = os.environ['RootFolderForTweets']
    debug = os.environ['Debug']
    return env, twitter_key, twitter_secret_key, bucket_name, root_folder, debug

def _get_input_params(event):
    default_query = "Karachi OR #Karachi OR karachi OR #karachi min_retweets:10 min_faves:10 -filter:replies filter:videos"
    q = event["q"] if "q" in event else default_query
    category = event["category"] if "category" in event else "default"
    count = event["count"] if "count" in event else "10"
    since_id = event["since_id"] if "since_id" in event else None
    return q, category, count, since_id

def _create_twitter_api(twitter_key, twitter_secret_key):
    auth = tweepy.AppAuthHandler(twitter_key, twitter_secret_key)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                    wait_on_rate_limit_notify=True)
    if (not api):
        raise ("Can't Authenticate")

    return api

def _search(api, searchQuery, tweetsPerQry, since_id=None):
    """Search for tweets matching the given search text."""
    return api.search(q=searchQuery, count=tweetsPerQry, since_id=since_id, return_json=True) 

def _get_json_result(tweets):
    """Returns a map of tweet id and json data result"""
    return {tweet.id: tweet._json for tweet in tweets}

def _save_json_to_s3(bucket_name, object_name, data):
    s3 = boto3.client('s3')
    body=json.dumps(data, ensure_ascii=False)
    response = s3.put_object(
        Bucket=bucket_name,
        Key=object_name,
        Body=body
    )
    return str (response) 

def _get_file_path(root_folder, prefix, file_name):
    year_month = datetime.now().strftime("%Y/%m")
    ts = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")    
    return f'{root_folder}/{year_month}/{prefix}-{ts}-{file_name}'

def lambda_handler(event, context):
    env, twitter_key, twitter_secret_key, bucket_name, root_folder, debug = _get_env_params()
    query, category, max_tweet_per_qry, since_id = _get_input_params(event) 
    if debug=="1": 
        print("env:", env, twitter_key, twitter_secret_key, bucket_name, root_folder)
        print("event:", query, category, max_tweet_per_qry, since_id)

    try:    
        api = _create_twitter_api(twitter_key, twitter_secret_key)
        tweets = _search(api, query, max_tweet_per_qry, since_id)
        count = len(tweets)
        json_result = _get_json_result(tweets) 
        file_path = _get_file_path(root_folder, category, file_name = f"result-{count}-rows.json")
        _save_json_to_s3(bucket_name, file_path, json_result)

        return {
            'statusCode': 200,
            'body': {
                "category": category,
                "query":    query,
                "since_id": since_id,
                "count" :   count,
                "file_path": file_path
            } 
        }

    except Exception as e:
        print(e)
        raise e
