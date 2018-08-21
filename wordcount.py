import tweepy
import Credentials
import json
from firstfile import Listen
from firstfile import OAuthHandler
from  firstfile import Stream
auth = tweepy.OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
auth.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
api = tweepy.API(auth)

india_trending = api.trends_place(23424848)

trends_list=json.loads(json.dumps(india_trending,indent=1))
b=[]
for trend in trends_list[0]["trends"]:
     a = ((trend["name"]).encode('UTF-8').strip('#'))
     b.append(a.decode('UTF-8'))
print(b)

a_Listen = Listen("celebstweets.txt")
authenticate = OAuthHandler(Credentials.Consumer_Key, Credentials.Consumer_Secret)
authenticate.set_access_token(Credentials.Access_Token, Credentials.Access_Token_Secret)
streamer = Stream(authenticate, a_Listen)
tweets = streamer.filter(track=b)










