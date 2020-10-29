const axios = require('axios');
const gql = require('graphql-tag');
const graphql = require('graphql');
const { print } = graphql;

/*
Copyright 2017 - 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at
    http://aws.amazon.com/apache2.0/
or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
*/


/* Amplify Params - DO NOT EDIT
	API_KARACHI24API_GRAPHQLAPIENDPOINTOUTPUT
	API_KARACHI24API_GRAPHQLAPIIDOUTPUT
	API_KARACHI24API_GRAPHQLAPIKEYOUTPUT
	ENV
	REGION
Amplify Params - DO NOT EDIT */

var express = require('express')
var bodyParser = require('body-parser')
var awsServerlessExpressMiddleware = require('aws-serverless-express/middleware')

// declare a new express app
var app = express()
app.use(bodyParser.json())
app.use(awsServerlessExpressMiddleware.eventContext())

// Enable CORS for all methods
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*")
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  next()
});

const url = process.env.API_KARACHI24API_GRAPHQLAPIENDPOINTOUTPUT
const api_key = process.env.API_KARACHI24API_GRAPHQLAPIKEYOUTPUT
const gql_query = gql`
    query result {
      result: listK24Tweetss(limit: 10) {
        items {
          id
          text
          screen_name
          row_timestamp
          retweeted
          retweet_count
          reply_count
          location
          last_updated
          category
          enabled
          followers_count
          file_path
          favorite_count
          flagged
          flaggedData
          hashtags
          media_url_https
          source_device
          topic
          truncated
          tweet_created_at
          tweet_date
          user_name
          user_status_count
          video_url
          duration_millis
          createdAt
        }
        nextToken
        }
    }
`  

get_data = async (event) => {
  try {
    const graphqlData = await axios({
      url: url,
      method: 'post',
      headers: {
        'x-api-key': api_key
      },
      data: {
        query: print(gql_query)
      }
    });
    
    return graphqlData.data.data.result

  } catch (err) {
    console.log('error posting to appsync: ', err);
  } 
}


/**********************
 * Example get method *
 **********************/

app.get('/', async (req, res) => {
  data = await get_data(req)
  res.json( {
    statusCode: 200,
    body: data,
    headers: {
        "Access-Control-Allow-Origin": "*",
    }
  })
});

app.listen(3000, function() {
    console.log("App started")
});

// Export the app object. When executing the application local this does nothing. However,
// to port it to AWS Lambda we will create a wrapper around that will load the app from
// this file
module.exports = app
