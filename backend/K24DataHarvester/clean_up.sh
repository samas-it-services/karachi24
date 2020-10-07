#!/bin/bash
project=karachi24
DBTableName=K24Tweets
DockerNetwork=k24_data_harvester_local
DockerDynamoDbContainer=dynamodb
delete_everything=1
endpoint_url=http://localhost:8000

if [ $delete_everything -eq "1" ] && docker network ls --format '{{.Name}}' | grep -w $DockerNetwork &> /dev/null; then
    echo Stopping and removing [$DockerDynamoDbContainer] container
    docker rm -f $DockerDynamoDbContainer &> /dev/null;

    echo deleting bridge network [$DockerNetwork] for the [$DockerDynamoDbContainer] container
    docker network rm $DockerNetwork &> /dev/null;

fi

if aws dynamodb list-tables --endpoint-url $endpoint_url | grep -w $DBTableName &> /dev/null; then
    echo dynamodb table $DBTableName is available at endpoint-url $endpoint_url
else    
    echo Warning: Could not find dynamodb table $DBTableName at endpoint-url $endpoint_url
fi
