import tweepy
from nltk.corpus import wordnet
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List
from keys import consumer_key, consumer_secret, access_key, access_secret

def get_tweets(keyword:str) -> List[str]:
  all_tweets = []
  for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
    all_tweets.append(tweet.full_text)
  return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
  tweets_clean = []
  for tweet in all_tweets:
    tweets_clean.append(p.clean(tweet))
  return tweets_clean

def get_sentiment(tweets_clean: List[str]) -> List[float]:
  sentiment_scores = []
  for tweet in tweets_clean:
    blob = TextBlob(tweet)
    sentiment_scores.append(blob.sentiment.polarity)
  return sentiment_scores

def generate_average_sentiment_score(keyword:str) -> int:
  tweets = get_tweets(keyword)
  tweets_clean = clean_tweets(tweets)
  sentiment_scores = get_sentiment(tweets_clean)
  average_score = statistics.mean(sentiment_scores)
  return average_score

if __name__ == "__main__":
  CONSUMER_KEY=consumer_key
  CONSUMER_SECRET=consumer_secret
  ACCESS_KEY=access_key
  ACCESS_SECRET=access_secret

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  api = tweepy.API(auth)
  
  print("What does Twitter prefer?")
  first_thing = input()
  print("...or...")
  second_thing = input()
  print("\n")

  first_score = generate_average_sentiment_score(first_thing)
  second_score = generate_average_sentiment_score(second_thing)

  if(first_score > second_score):
    print(f"Twitter prefers {first_thing} over {second_thing}")
  else:
    print(f"Twitter prefers {second_thing} over {first_thing}")



