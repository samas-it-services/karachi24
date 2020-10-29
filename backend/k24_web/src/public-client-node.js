const axios = require("axios")

// const url = process.env.API_KARACHI24API_GRAPHQLAPIENDPOINTOUTPUT
// const api_key = process.env.API_KARACHI24API_GRAPHQLAPIKEYOUTPUT

const gql_query = `
query listK24Tweets {
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

axios({
    url: url,
    headers: {
        'Access-Control-Allow-Origin': '*',        
        'x-api-key': api_key
      },
    method: 'post',
    data: {
      query: gql_query    
    }
  }).then((result) => {
    console.log(JSON.stringify(result.data))
  });
