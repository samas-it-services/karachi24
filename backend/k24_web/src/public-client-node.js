const axios = require("axios")

const url = process.env.API_KARACHI24API_GRAPHQLAPIENDPOINTOUTPUT
const api_key = process.env.API_KARACHI24API_GRAPHQLAPIKEYOUTPUT

const gql_simple_query = `
query listK24Tweets {
  result: listK24Tweetss(limit: 10, filter: {enabled: {eq: true}}) {
    items {
      id
      text
      topic
      category
      user_name
      tweet_date
      tweet_created_at
      configID
      hashtags
    }
    nextToken
    }
}
`  

const gql_detailed_query = `
query listK24Tweets {
  result: listK24Tweetss(limit: 10, filter: {enabled: {eq: true}}) {
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
const gql_query_by_topic = `
query tweetByTopic {
  tweetByTopic(limit: 10, topic: "karachi", sortDirection: DESC, filter: {enabled: {eq: true}}) {
    items {
      id
      text
      topic
      category
      user_name
      tweet_date
      tweet_created_at
      configID
      hashtags
    }
    nextToken
  }
}

`

const gql_query_tweet_by_day = `
query tweetByTopic {
  tweetByDay(limit: 10, sortDirection: DESC, tweet_created_at: {beginsWith: "2020-10-31"}, tweet_date: "2020-10-31", filter: {enabled: {eq: true}}) {
    items {
      id
      text
      topic
      category
      user_name
      tweet_date
      tweet_created_at
      configID
      hashtags
    }
    nextToken
  }
}
`
const gql_query_tweet_by_user = `
query MyQuery {
  tweetByUser(limit: 10, sortDirection: DESC, tweet_created_at: {beginsWith: "2020-10-31"}, user_name: "Blood Donors Pakistan 🇵🇰", filter: {enabled: {eq: true}}) {
    items {
      id
      text
      topic
      category
      user_name
      tweet_date
      tweet_created_at
      configID
      hashtags
    }
    nextToken
  }
}

`

gql_query_VideoTweets = `
query VideoTweets {
  tweetByCategory(category: Video, limit: 10, sortDirection: DESC, tweet_created_at: {beginsWith: "2020-10-31"}) {
    items {
      id
      text
      topic
      category
      user_name
      tweet_date
      tweet_created_at
      configID
      hashtags
      video_url # contains video url
    }
    nextToken
  }
}

`
// gql_query = gql_simple_query
// gql_query = gql_detailed_query
// gql_query = gql_query_by_topic
// gql_query = gql_query_tweet_by_day
// gql_query = gql_query_tweet_by_user
gql_query = gql_query_VideoTweets

const gql_update_value_query = ` 
mutation MyMutation {
  updateK24Config(input: {enabled: false, id: "1"}) {
    id
    enabled
  }
}
`
// gql_query = gql_update_value_query // this will fail because API Key method has read-only access

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
    console.log(JSON.stringify(result.data,null,2))
  })
  .catch((error) => {
    console.error(error);
  });
