# python3 functions/SaveToDynamoDb/parse_result.py
import os
import json
from datetime import datetime
from dateutil.parser import parse

def _parse_tweet_from_json(item, extra_data):
    duration_millis = media_url  = video_url = ""

    if "extended_entities" in item:
        media = item["extended_entities"]["media"][0]
        duration_millis = media["video_info"]["duration_millis"] if "video_info" in media and "duration_millis" in media["video_info"] else ""
        media_url = str(media["media_url_https"]) if "media_url_https" in media else ""
        video_url = str(media["video_info"]["variants"][0]["url"]) if "video_info" in media else ""

    reply_count = item["reply_count"] if 'reply_count' in item else 0
    retweeted = item["retweeted"]  if 'retweeted' in item else "NA"
    tweet_date = str(parse(item["created_at"]).strftime('%Y-%m-%d'))

    result = {
        'Id':                item["id"],
        'user_name':         item["user"]["name"],
        'screen_name':       str(item["user"]["screen_name"]),
        'followers_count':   str(item["user"]["followers_count"]),
        'retweet_count':     item["retweet_count"],
        'text':              str(item["text"]),
        'tweet_created_at':  str(item["created_at"]),
        'favorite_count':    item["favorite_count"],
        'hashtags':          str(item["entities"]['hashtags']),
        'user_status_count': item["user"]["statuses_count"],
        'location':          str(item["place"]),
        'source_device':     str(item["source"]),
        'truncated':         str(item["truncated"]),
        'reply_count':       reply_count,
        'retweeted':         retweeted,
        'tweet_date':        tweet_date,

        'duration_millis':   duration_millis,
        'media_url_https':   media_url,
        'video_url':         video_url,
        'row_timestamp':     str(datetime.now().isoformat()),
    }

    return {**result, **extra_data}

def _get_file_content_as_json(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        return json.loads(file_content)

file_path="./data/tweet_result_file.json"
json_data = _get_file_content_as_json(file_path)
extra_data = {"category": "text", "topic": "karachi", "file_path": file_path}
for key in json_data.keys():
    data = _parse_tweet_from_json(json_data[key], extra_data)
    print(data['Id'])
    # print(data)

print("since_id", list(json_data.keys())[-1])
print("max_since_id", max(list(json_data.keys())))
