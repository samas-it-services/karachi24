#!/bin/bash

# pls replace this with your twitter key/secret
TwitterKey=*** twitterkey ***
TwitterSecretKey=***twiiter secret key ***
# pls replace this with your own s3 bucket that you have write access to
InputBucketName=data.karachi24.com

# below settings don't need to be changed
Environment=local
eventFile_TweetSearcherFunction=./functions/TweetSearcher/event.json
eventFile_SaveToDynamoDbFunction=./data/result1.json
DBTableName=K24Tweets
RootFolderForTweets=k24dataharvester/local/tweets
DockerNetwork=k24_data_harvester_local
DynamoDbEndPointURL=http://dynamodb:8000/
endpoint_url=http://localhost:8000/
Debug=0

# Before: Make sure to run this once to setup docker container and dynamodb
# ./setup.sh

# ---------- no changes beyond this point ----------

echo Validating SAM template
sam validate -t template.yaml

echo Building CloudFormation stack
sam build

# If you don’t have Python3.8 installed on your local environment, use below command
# sam build --use-container

echo Executing TweetSearcherFunction
sam local invoke TweetSearcherFunction --parameter-overrides \
ParameterKey=Environment,ParameterValue=$Environment \
ParameterKey=TwitterKey,ParameterValue=$TwitterKey \
ParameterKey=TwitterSecretKey,ParameterValue=$TwitterSecretKey \
ParameterKey=InputBucketName,ParameterValue=$InputBucketName \
ParameterKey=RootFolderForTweets,ParameterValue=$RootFolderForTweets \
ParameterKey=Debug,ParameterValue=$Debug \
-e $eventFile_TweetSearcherFunction \
> $eventFile_SaveToDynamoDbFunction

echo Executing SaveToDynamoDbFunction
sam local invoke SaveToDynamoDbFunction --parameter-overrides \
ParameterKey=Environment,ParameterValue=$Environment \
ParameterKey=InputBucketName,ParameterValue=$InputBucketName \
ParameterKey=DBTableName,ParameterValue=$DBTableName \
ParameterKey=Debug,ParameterValue=$Debug \
ParameterKey=DynamoDbEndPointURL,ParameterValue=$DynamoDbEndPointURL \
--docker-network $DockerNetwork \
-e $eventFile_SaveToDynamoDbFunction \
> ./data/result2.json

# endpoint_url=http://localhost:8000/
# DBTableName=K24Tweets
aws dynamodb scan --table-name $DBTableName --select COUNT --endpoint-url $endpoint_url

# echo Deploying the stack
# sam deploy
