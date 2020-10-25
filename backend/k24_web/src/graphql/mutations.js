/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const createK24Config = /* GraphQL */ `
  mutation CreateK24Config(
    $input: CreateK24ConfigInput!
    $condition: ModelK24ConfigConditionInput
  ) {
    createK24Config(input: $input, condition: $condition) {
      id
      name
      category
      topic
      query
      enabled
      file_path
      last_updated
      count
      since_id
      createdAt
      updatedAt
    }
  }
`;
export const updateK24Config = /* GraphQL */ `
  mutation UpdateK24Config(
    $input: UpdateK24ConfigInput!
    $condition: ModelK24ConfigConditionInput
  ) {
    updateK24Config(input: $input, condition: $condition) {
      id
      name
      category
      topic
      query
      enabled
      file_path
      last_updated
      count
      since_id
      createdAt
      updatedAt
    }
  }
`;
export const deleteK24Config = /* GraphQL */ `
  mutation DeleteK24Config(
    $input: DeleteK24ConfigInput!
    $condition: ModelK24ConfigConditionInput
  ) {
    deleteK24Config(input: $input, condition: $condition) {
      id
      name
      category
      topic
      query
      enabled
      file_path
      last_updated
      count
      since_id
      createdAt
      updatedAt
    }
  }
`;
export const createK24Tweets = /* GraphQL */ `
  mutation CreateK24Tweets(
    $input: CreateK24TweetsInput!
    $condition: ModelK24TweetsConditionInput
  ) {
    createK24Tweets(input: $input, condition: $condition) {
      id
      text
      category
      tweet_created_at
      tweet_date
      user_name
      topic
      enabled
      file_path
      last_updated
      duration_millis
      favorite_count
      followers_count
      hashtags
      location
      media_url_https
      reply_count
      retweet_count
      retweeted
      row_timestamp
      screen_name
      source_device
      truncated
      user_status_count
      video_url
      configID
      config {
        id
        name
        category
        topic
        query
        enabled
        file_path
        last_updated
        count
        since_id
        createdAt
        updatedAt
      }
      createdAt
      updatedAt
    }
  }
`;
export const updateK24Tweets = /* GraphQL */ `
  mutation UpdateK24Tweets(
    $input: UpdateK24TweetsInput!
    $condition: ModelK24TweetsConditionInput
  ) {
    updateK24Tweets(input: $input, condition: $condition) {
      id
      text
      category
      tweet_created_at
      tweet_date
      user_name
      topic
      enabled
      file_path
      last_updated
      duration_millis
      favorite_count
      followers_count
      hashtags
      location
      media_url_https
      reply_count
      retweet_count
      retweeted
      row_timestamp
      screen_name
      source_device
      truncated
      user_status_count
      video_url
      configID
      config {
        id
        name
        category
        topic
        query
        enabled
        file_path
        last_updated
        count
        since_id
        createdAt
        updatedAt
      }
      createdAt
      updatedAt
    }
  }
`;
export const deleteK24Tweets = /* GraphQL */ `
  mutation DeleteK24Tweets(
    $input: DeleteK24TweetsInput!
    $condition: ModelK24TweetsConditionInput
  ) {
    deleteK24Tweets(input: $input, condition: $condition) {
      id
      text
      category
      tweet_created_at
      tweet_date
      user_name
      topic
      enabled
      file_path
      last_updated
      duration_millis
      favorite_count
      followers_count
      hashtags
      location
      media_url_https
      reply_count
      retweet_count
      retweeted
      row_timestamp
      screen_name
      source_device
      truncated
      user_status_count
      video_url
      configID
      config {
        id
        name
        category
        topic
        query
        enabled
        file_path
        last_updated
        count
        since_id
        createdAt
        updatedAt
      }
      createdAt
      updatedAt
    }
  }
`;
