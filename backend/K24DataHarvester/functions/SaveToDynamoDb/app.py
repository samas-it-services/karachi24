import os
import json 
from datetime import datetime
import botocore
import boto3
from dateutil.parser import parse
 
def _get_env_params():
    env = os.environ['Environment']
    endpoint_url = os.environ['DynamoDbEndPointURL']
    bucket_name = os.environ['InputBucketName']
    table_name = os.environ["DDBtable"]
    config_DB_table_name = os.environ['ConfigDBTableName']
    debug = os.environ['Debug']
    return env, endpoint_url, bucket_name, table_name, config_DB_table_name, debug

def _get_input_params(event):
    if "body" in event:
        body = event["body"]
        
        query_id = body["query_id"] if "query_id" in body else "0"
        category = body["category"]  if "category" in body else "default"
        topic = body["topic"] if "topic" in body else "default"
        query = body["query"] if "query" in body else ""
        count = body["count"] if "count" in body else "0"
        since_id = body["since_id"] if "since_id" in body else ""
        file_path = body["file_path"] if "file_path" in body else -1

        return query_id, category, topic, query, count, since_id, file_path
    else:
        raise Exception("SaveToDynamoDb: Invalid input.", event)

def _get_dynamoDb_connection(env, endpoint_url):
    ddbclient=''
    if env == 'local':
        ddbclient = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    else:
        ddbclient = boto3.resource('dynamodb')

    return ddbclient

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

def _get_s3_file_content_as_json(bucket_name, file_path):
    s3 = boto3.client('s3')
    fileObj = s3.get_object(Bucket=bucket_name, Key=file_path)
    file_content = fileObj["Body"].read().decode("utf-8")
    return json.loads(file_content)

def _update_since_id(dynamodb, table_name, query_id, since_id, file_path):
    table = boto3.resource('dynamodb').Table(table_name)
    # table = dynamodb.Table(table_name)
    item = ""
    try:
        # get item
        response = table.get_item(Key={'Id': int(query_id), 'enabled': "1"})
        item = response['Item']

        # update
        item['since_id'] = str(since_id)
        item['file_path'] = file_path
        item['last_updated'] = str(datetime.now())
        table.put_item(Item=item)
    except Exception as e:
        print("saveToDynamoDb: _update_since_id: Unexpected error: ", str(e))
        print("saveToDynamoDb: _update_since_id: query_id:", query_id)
        print("saveToDynamoDb: _update_since_id: item:", item)
        pass

    return True

def lambda_handler(event, context):
    env, endpoint_url, bucket_name, table_name, config_DB_table_name, debug = _get_env_params()
    query_id, category, topic, query, count, since_id, file_path = _get_input_params(event)

    if debug=="1": 
        print("Env:", env, ", endpoint_url:", endpoint_url, ", bucket_name: ", bucket_name, ", table_name: ", table_name, ", config_DB_table_name: ", config_DB_table_name)
        print("event: category:", category, ", topic:", topic, ", count:", count, ", file_path:", file_path)
        print("query: \n", query)

    try:    
        ddbclient = _get_dynamoDb_connection(env, endpoint_url)
        new_since_id = since_id
        if count > 0:
            extra_data = {"category": category, "topic": topic, "file_path": file_path}
            json_data = _get_s3_file_content_as_json(bucket_name, file_path)

            dynamoTable = ddbclient.Table(table_name)
            print("dynamoTable created on:", dynamoTable.creation_date_time)

            with dynamoTable.batch_writer() as batch:
                for key in json_data.keys():
                    data = _parse_tweet_from_json(json_data[key], extra_data)
                    batch.put_item(data)

            new_since_id = max(list(json_data.keys()))
            _update_since_id(ddbclient, config_DB_table_name, query_id, new_since_id, file_path)
            
        return {
            'statusCode': 200,
            'body': {
                "query_id":     query_id,
                "category":     category,
                "topic":        topic,
                "query":        query,
                "count":        count,
                "old_since_id": since_id,
                "new_since_id": new_since_id,
                    }
            }

    except botocore.exceptions.ClientError as err:
        if err.response['Error']['Code'] == 'InternalError': # Generic error
            print('Error Message: {}'.format(err.response['Error']['Message']))
            print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
            print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        else:
            raise err

    except Exception as e:
        print("saveToDynamoDb: Unexpected error: ", str(e))
        raise e
