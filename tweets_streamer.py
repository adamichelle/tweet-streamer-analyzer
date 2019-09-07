import credentials
import tweepy
import json

consumer_key = credentials.API_KEY
consumer_secret_key = credentials.API_SECRET_KEY
access_token = credentials.ACCESS_TOKEN
access_token_secret = credentials.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = ['Vote Cindy', 'Vote Esther', 'Vote Frodd', 'Vote Sir Dee', 'Vote Tacha', 'Vote Venita']

def stream_tweets(search_term):
    data = []
    counter = 0
    for tweet in tweepy.Cursor(api.search, q='\"{}\" -filter:retweets'.format(search_term), count=100, lang='en', tweet_mode='extended').items():
        tweet_details = {}
        tweet_details['name'] = tweet.user.screen_name
        tweet_details['tweet'] = tweet.full_text
        tweet_details['retweets'] = tweet.retweet_count
        tweet_details['location'] = tweet.user.location
        tweet_details['created'] = tweet.created_at.strftime("%d-%b-%Y")
        tweet_details['followers'] = tweet.user.followers_count
        tweet_details['is_user_verified'] = tweet.user.verified

        data.append(tweet_details)
        
        counter += 1
        if counter == 1000:
            break
        else:
            pass
    with open('data/{}.json'.format(search_term), 'w') as f:
        json.dump(data, f)
    print('done!')

if __name__ == "__main__":
    print('Starting to stream...')
    for search_term in search_terms:
        stream_tweets(search_term)
    print('finished!')