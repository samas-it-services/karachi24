const axios = require("axios")

const url = process.env.API_URL
const api_key = process.env.API_<YOUR_API_NAME>_GRAPHQLAPIKEYOUTPUT

const gql_query = `
    query listK24Tweets {
        listK24Tweetss(limit: 10) {
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
