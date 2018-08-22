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
          spamwriter = csv.writer(csvfile, delimiter=' ', lineterminator='\n')

          for word in b:
               spamwriter.writerow([word])





def get_tweets():
     b=[]
     with open('trending.csv','r') as  csvfile:
          spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
          for row in spamreader:
               b.append(''.join(row))
     count=0;
     for word in b:
          a_Listen = Listen("tweets.csv", word)
          authenticate = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
          authenticate.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
          api = tweepy.API(authenticate,timeout=1)

          streamer = Stream(authenticate, a_Listen)
          tweets = streamer.filter(track=[word], languages=["en"])
          count=count+1
          if count > 10:
               break



     print('done')





