import tweepy

API_KEY = "INSERT_API_KEY_HERE"
API_KEY_SECRET = "API_SECRET_KEY_HERE"
ACCESS_TOKEN = "ACCESS_TOKEN_HERE"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET_HERE"
BEARER_TOKEN ="BEARER_TOKEN_HERE"


api = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
query = "covid"
response = api.search_recent_tweets(query, user_auth=True)

for tweet in tweepy.Paginator(api.search_recent_tweets, query=query, max_results=100).flatten(limit=5000):
    ### WRITE CODE TO SAVE these tweets into a file here.
    with open("tweets.txt", "a") as file:
        tweet = str(tweet).replace("\n", " ")
        file.write("\n" + str(tweet.encode(encoding = "utf-8")))

print("Written to file!")
