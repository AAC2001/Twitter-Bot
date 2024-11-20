import tweepy

# Twitter API credentials

BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAKMeqAEAAAAAUsKIywZB14zeWgxBgtnjRHswjCM%3DG2JVdeDEVU6o0zjYfCw2mXBj0MTPQ464ORUqeJ4uWgle1Dqxwk'
API_KEY = 'fJALnBjKkOXKdkgQ29zpdc2I8'
API_SECRET_KEY = 'vo2MWFHMEYCSQ1Yekc4qoAi4exDjsXVneJiRSvaz9IcXk3Saao'
ACCESS_TOKEN = '1403012288676761606-DCm9Y3CZND5UcoEGmWa6ZjqN0nn0Op'
ACCESS_TOKEN_SECRET = 'tzYKkx0KKpSUvgqKCCOrMXUTDsYJlnneVabgqZNv6vpmy'
# Authenticate using Twitter API v2 (Tweepy Client)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Function to like tweets
def auto_like(search_term, max_tweets):
    query = f"{search_term} -is:retweet"
    try:
        tweets = client.search_recent_tweets(query=query, max_results=max_tweets)
        if tweets.data:
            for tweet in tweets.data:
                try:
                    client.like(tweet.id)
                    print(f"Liked tweet by ID: {tweet.id}")
                except tweepy.TweepyException as e:
                    print(f"Error liking tweet: {e}")
    except tweepy.TweepyException as e:
        print(f"Error searching tweets: {e}")

# Function to retweet
def auto_retweet(search_term, max_tweets):
    query = f"{search_term} -is:retweet"
    try:
        tweets = client.search_recent_tweets(query=query, max_results=max_tweets)
        if tweets.data:
            for tweet in tweets.data:
                try:
                    client.retweet(tweet.id)
                    print(f"Retweeted tweet by ID: {tweet.id}")
                except tweepy.TweepyException as e:
                    print(f"Error retweeting: {e}")
    except tweepy.TweepyException as e:
        print(f"Error searching tweets: {e}")

# Function to comment on tweets
def auto_comment(search_term, max_tweets, comment_text):
    query = f"{search_term} -is:retweet"
    try:
        tweets = client.search_recent_tweets(query=query, max_results=max_tweets)
        if tweets.data:
            for tweet in tweets.data:
                try:
                    client.create_tweet(
                        text=f"@{tweet.author_id} {comment_text}",
                        in_reply_to_tweet_id=tweet.id
                    )
                    print(f"Commented on tweet by ID: {tweet.id}")
                except tweepy.TweepyException as e:
                    print(f"Error commenting: {e}")
    except tweepy.TweepyException as e:
        print(f"Error searching tweets: {e}")

if __name__ == "__main__":
    # Main parameters
    search_keyword = "Python"
    number_of_tweets = 10
    comment_message = "Great tweet!"

    # Execute functions
    auto_like(search_keyword, number_of_tweets)
    auto_retweet(search_keyword, number_of_tweets)
    auto_comment(search_keyword, number_of_tweets, comment_message)