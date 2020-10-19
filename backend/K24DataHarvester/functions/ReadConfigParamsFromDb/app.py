import json
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime
import os 

def _get_env_params():
    env = os.environ['Environment']
    config_DB_table_name = os.environ['ConfigDBTableName']
    endpoint_url = os.environ['DynamoDbEndPointURL']
    debug = os.environ['Debug']
    return env, config_DB_table_name, endpoint_url, debug

def _get_input_params(event):
    queries = event["queries"] if "queries" in event else "0"
    return queries

def _get_dynamoDb_connection(env, endpoint_url):
    ddbclient=''
    if env == 'local':
        ddbclient = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    else:
        ddbclient = boto3.resource('dynamodb')

    return ddbclient

def lambda_handler(event, context):
    env, config_DB_table_name, endpoint_url, debug = _get_env_params()
    queries = _get_input_params(event)

    if debug=="1": 
        print("env:", env, ", config_DB_table_name: ", config_DB_table_name)

    try:    
        ddbclient = _get_dynamoDb_connection(env, endpoint_url)
        dynamoTable = ddbclient.Table(config_DB_table_name)
        print(f"dynamoTable [{config_DB_table_name}] created on: {dynamoTable.creation_date_time}")
        response = dynamoTable.scan()
        db_response = [x for x in response['Items'] if x['enabled'] == "1"]

        return {
            'statusCode': 200,
            'queries': db_response
        }

    except Exception as e:
        print("ReadConfigParamsFromDb: Unexpected error: ", str(e))
        raise e
