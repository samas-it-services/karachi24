/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const listK24Configs = /* GraphQL */ `
  query ListK24Configs(
    $filter: ModelK24ConfigFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listK24Configs(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
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
      nextToken
    }
  }
`;
export const getK24Config = /* GraphQL */ `
  query GetK24Config($id: ID!) {
    getK24Config(id: $id) {
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
export const configByTopic = /* GraphQL */ `
  query ConfigByTopic(
    $topic: String
    $category: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24ConfigFilterInput
    $limit: Int
    $nextToken: String
  ) {
    configByTopic(
      topic: $topic
      category: $category
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
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
      nextToken
    }
  }
`;
export const configByCategory = /* GraphQL */ `
  query ConfigByCategory(
    $category: Category
    $topic: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24ConfigFilterInput
    $limit: Int
    $nextToken: String
  ) {
    configByCategory(
      category: $category
      topic: $topic
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
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
      nextToken
    }
  }
`;
export const getK24Tweets = /* GraphQL */ `
  query GetK24Tweets($id: ID!) {
    getK24Tweets(id: $id) {
      id
      text
      category
      tweet_created_at_raw
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
      flagged
      flaggedData
      createdAt
      updatedAt
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
    }
  }
`;
export const listK24Tweetss = /* GraphQL */ `
  query ListK24Tweetss(
    $filter: ModelK24TweetsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listK24Tweetss(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
        id
        text
        category
        tweet_created_at_raw
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
        flagged
        flaggedData
        createdAt
        updatedAt
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
      }
      nextToken
    }
  }
`;
export const tweetByTopic = /* GraphQL */ `
  query TweetByTopic(
    $topic: String
    $tweet_created_at: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24TweetsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    tweetByTopic(
      topic: $topic
      tweet_created_at: $tweet_created_at
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        text
        category
        tweet_created_at_raw
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
        flagged
        flaggedData
        createdAt
        updatedAt
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
      }
      nextToken
    }
  }
`;
export const tweetByCategory = /* GraphQL */ `
  query TweetByCategory(
    $category: Category
    $tweet_created_at: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24TweetsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    tweetByCategory(
      category: $category
      tweet_created_at: $tweet_created_at
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        text
        category
        tweet_created_at_raw
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
        flagged
        flaggedData
        createdAt
        updatedAt
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
      }
      nextToken
    }
  }
`;
export const tweetByUser = /* GraphQL */ `
  query TweetByUser(
    $user_name: String
    $tweet_created_at: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24TweetsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    tweetByUser(
      user_name: $user_name
      tweet_created_at: $tweet_created_at
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        text
        category
        tweet_created_at_raw
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
        flagged
        flaggedData
        createdAt
        updatedAt
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
      }
      nextToken
    }
  }
`;
export const tweetByDay = /* GraphQL */ `
  query TweetByDay(
    $tweet_date: AWSDate
    $tweet_created_at: ModelStringKeyConditionInput
    $sortDirection: ModelSortDirection
    $filter: ModelK24TweetsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    tweetByDay(
      tweet_date: $tweet_date
      tweet_created_at: $tweet_created_at
      sortDirection: $sortDirection
      filter: $filter
      limit: $limit
      nextToken: $nextToken
    ) {
      items {
        id
        text
        category
        tweet_created_at_raw
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
        flagged
        flaggedData
        createdAt
        updatedAt
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
      }
      nextToken
    }
  }
`;
