#!/bin/bash
eventFile_TweetSearcherFunction=./functions/TweetSearcher/event.json
eventFile_SaveToDynamoDbFunction=./data/result1.json

echo Validating SAM template
sam validate -t template.yaml

echo Building CloudFormation stack
sam build

echo Executing TweetSearcherFunction
sam local invoke "TweetSearcherFunction" --env-vars env.json -e $eventFile_TweetSearcherFunction > ./data/result1.json

echo Executing SaveToDynamoDbFunction
sam local invoke "SaveToDynamoDbFunction" --env-vars env.json -e $eventFile_SaveToDynamoDbFunction > ./data/result2.json

# echo Deploying the stack
# sam deploy
