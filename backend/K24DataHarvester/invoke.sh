sam build
sam local invoke "TweetSearcherFunction" --env-vars env.json -e event.json > ./data/result1.json
# sam local invoke "SaveToDynamoDbFunction" --env-vars env.json -e event_savetoDynamoDb.json > ./data/result2.json
sam local invoke "SaveToDynamoDbFunction" --env-vars env.json -e ./data/result1.json > ./data/result2.json
