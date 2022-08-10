import re
import time
from flair.models import TextClassifier
from flair.data import Sentence

bearer = "AAAAAAAAAAAAAAAAAAAAAJEqewEAAAAA0Yk3EkkegUzmvYrO05QXHy9tAcw" \
         "%3DvBt3tVvagszWed67Aqp7Qg4hsTxuojDyUQmcFXsbfOjtFkwyvN "
consumer_key = "3Hp1Rz5WsRtRxI5YQwJk45ozx"
consumer_secret = "XKk1R3v2vOZ3deY4Z4A7ZNk8iAFsnIbpfbL9isktQgyHq7jcmX"
access_token = "1547267955041325056-KCji0pY8MfqAmJcehXojwg7ozzEfkm"
access_token_secret = "sSClnNqQToVpLRTlZTROkYOAKYPh31GcQx99jE31rKaVq"
api = tweepy.Client(bearer, consumer_key, consumer_secret, access_token, access_token_secret)
api.get_me()


def preprocess_text(text):
    text = text.lower()
    text = re.sub("@[\w]*", "", text)
    text = re.sub("http\S+", "", text)
    text = re.sub("[^a-zA-Z#]", " ", text)
    text = re.sub("rt", "", text)
    text = re.sub("\s+", " ", text)

    return text


classifier = TextClassifier.load('en-sentiment')


def get_sentiment(twit):
    sentence = Sentence(twit)
    classifier.predict(sentence)
    return str(sentence.labels).split("\'")[3]


a = input("enter field")
while True:
    tweets = api.search_recent_tweets(a).data

    for tweet in tweets:
        original_tweet = tweet.text
        clean_tweet = preprocess_text(original_tweet)
        sentiment = get_sentiment(clean_tweet)

        print('------------------------Tweet-------------------------------')
        print(original_tweet)
        print('------------------------------------------------------------')
        print('Sentiment:', sentiment)
        time.sleep(1)
        print('\n\n')
