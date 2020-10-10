import os
import json 
from datetime import datetime
import botocore
import boto3
 
def _get_env_params():
    env = os.environ['Environment']
    endpoint_url = os.environ['DynamoDbEndPointURL']
    bucket_name = os.environ['InputBucketName']
    table_name = os.environ["DDBtable"]
    debug = os.environ['Debug']
    return env, endpoint_url, bucket_name, table_name, debug

def _get_input_params(event):
    query = event["body"]["query"] 
    category = event["body"]["category"] 
    count = event["body"]["count"] if event["body"] else 0
    file_path = event["body"]["file_path"] 

    return query, category, count, file_path

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

    result = {
        'Id':                item["id"],
        'user_name':         item["user"]["name"],
        'screen_name':       str(item["user"]["screen_name"]),
        'retweet_count':     item["retweet_count"],
        'text':              str(item["text"]),
        'tweet_created_at':  str(item["created_at"]),
        'favorite_count':    item["favorite_count"],
        'hashtags':          str(item["entities"]['hashtags']),
        'user_status_count': item["user"]["statuses_count"],
        'location':          str(item["place"]),
        'source_device':     str(item["source"]),
        'truncated':         str(item["truncated"]),
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

def lambda_handler(event, context):
    env, endpoint_url, bucket_name, table_name, debug  = _get_env_params()
    query, category, count, file_path= _get_input_params(event)

    if debug=="1": 
        print("Env:", env, endpoint_url, bucket_name, table_name)
        print("Event:", query, category, count, file_path)

    try:    
        ddbclient = _get_dynamoDb_connection(env, endpoint_url)
        result = {}
        if count:
            extra_data = {"category": category, "file_path": file_path}
            json_data = _get_s3_file_content_as_json(bucket_name, file_path)

            dynamoTable = ddbclient.Table(table_name)
            print("dynamoTable created on:", dynamoTable.creation_date_time)

            with dynamoTable.batch_writer() as batch:
                for key in json_data.keys():
                    batch.put_item(_parse_tweet_from_json(json_data[key], extra_data))

        return count

    except botocore.exceptions.ClientError as err:
        if err.response['Error']['Code'] == 'InternalError': # Generic error
            print('Error Message: {}'.format(err.response['Error']['Message']))
            print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
            print('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        else:
            raise err

    except Exception as e:
        print("saveToDynamoDb: Unexpected error: ", str(e))
        print("saveToDynamoDb: env: endpoint_url: ", str(endpoint_url))
        print("saveToDynamoDb: param: file_path: ", str(file_path))
        print("saveToDynamoDb: param: query: ", str(query))
        raise e
