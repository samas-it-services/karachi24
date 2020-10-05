from datetime import datetime
from random import randint
from uuid import uuid4
import boto3
import json 
import os
import numpy as np

BATCH_SIZE = 25

def _parse_tweet_from_json(item, extra_data):
    duration_millis = media_url  = video_url = ""

    if "extended_entities" in item:
        media = item["extended_entities"]["media"][0]
        duration_millis = media["video_info"]["duration_millis"] if "video_info" in media and "duration_millis" in media["video_info"] else ""
        media_url = str(media["media_url_https"]) if "media_url_https" in media else ""
        video_url = str(media["video_info"]["variants"][0]["url"]) if "video_info" in media else ""

    result = {
        'Id':                item["id"],
        'user_name':         item["user"]["name"],
        'screen_name':       str(item["user"]["screen_name"]),
        'retweet_count':     str(item["retweet_count"]),
        'text':              str(item["text"]),
        'tweet_created_at':  str(item["created_at"]),
        'favorite_count':    str(item["favorite_count"]),
        'hashtags':          str(item["entities"]['hashtags']),
        'user_status_count': str(item["user"]["statuses_count"]),
        'location':          str(item["place"]),
        'source_device':     str(item["source"]),
        'truncated':         str(item["truncated"]),
        'duration_millis':   str(duration_millis),
        'media_url_https':   media_url,
        'video_url':         video_url,
        'row_timestamp':     str(datetime.now().isoformat()),
    }
    return {**result, **extra_data}

def lambda_handler(event, context):
    """Lambda function

    Parameters
    ----------
    event: dict, required
        Input event to the Lambda function

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------
        dict: Object containing results
    """

    bucket_name = os.environ['InputBucketName']
    table_name = os.environ["DDBtable"]
    query = event["body"]["query"] 
    category = event["body"]["category"] 
    file_path = event["body"]["file_path"] 
    count = event["body"]["count"] if event["body"] else 0

    try:    
        result = {}
        if count:
            s3 = boto3.client('s3')
            fileObj = s3.get_object(Bucket=bucket_name, Key=file_path)
            file_content = fileObj["Body"].read().decode("utf-8")
            all_data = json.loads(file_content)
            chunks = (count//BATCH_SIZE)+1
            all_keys = list(all_data.keys())
            chunked_ids = np.array_split(all_keys, chunks)
            dynamo_db = boto3.resource('dynamodb')
            dynamoTable = dynamo_db.Table(table_name)

            for key_batch in chunked_ids:
                for key in key_batch:
                    extra_data = {"category": category, "file_path": file_path}
                    data = _parse_tweet_from_json(all_data[key], extra_data)
                    dynamoTable.put_item(Item = {
                        'Id':                str(data["Id"]),
                        'src_file':          str(data["file_path"]),
                        'category':          str(data["category"]),
                        'user_name':         str(data["user_name"]),
                        'screen_name':       str(data["screen_name"]),
                        'retweet_count':     str(data["retweet_count"]),
                        'text':              str(data["text"]),
                        'tweet_created_at':  str(data["tweet_created_at"]),
                        'favorite_count':    str(data["favorite_count"]),
                        'hashtags':          str(data["hashtags"]),
                        'user_status_count': str(data["user_status_count"]),
                        'location':          str(data["location"]),
                        'source_device':     str(data["source_device"]),
                        'truncated':         str(data["truncated"]),
                        'duration_millis':   str(data["duration_millis"]),
                        'media_url_https':   str(data["media_url_https"]),
                        'video_url':         str(data["video_url"]),
                        'row_timestamp':     str(data["row_timestamp"]),
                    })

        return count

    except Exception as e:
        print("file_path: ", file_path)
        print(e)
        raise e
