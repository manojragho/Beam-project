import tweepy
import Credentials
import json
from firstfile import Listen
from firstfile import OAuthHandler
from  firstfile import Stream
import csv
import string

def get_trending():
     auth = tweepy.OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
     auth.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
     api = tweepy.API(auth)

     india_trending = api.trends_place(23424848)

     trends_list = json.loads(json.dumps(india_trending, indent=1))
     b = []
     for trend in trends_list[0]["trends"]:
          a = ((trend["name"]).encode('UTF-8').strip('#'))
          b.append(a)
     print(b)
     with open('trending.csv', 'w') as csvfile:
          writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')

          for word in b:
               writer.writerow([word])





def get_tweets():
     b=[]
     with open('trending.csv','r') as  csvfile:
          reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          for row in reader:
               b.append(''.join(row))
     count=0
     a_Listen = Listen("tweets.csv", "")
     authenticate = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
     authenticate.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
     streamer = Stream(authenticate, a_Listen)
     tweets = streamer.filter(track=b, languages=["en"])
'''
     for word in b:
          a_Listen = Listen("tweets.csv", "")
          authenticate = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
          authenticate.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
          streamer = Stream(authenticate, a_Listen)
          print('searching for '+word)
          tweets = streamer.filter(track=[word], languages=["en"])
          count=count+1
          if count > 10:
               break
               '''










