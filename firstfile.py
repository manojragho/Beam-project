# I am using tweepy package for interaction with twitter API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import json



import Credentials

class Listen(StreamListener):

    def __init__(self,filename):
        self.filename = filename

    def on_data(self, a):
        a=a.encode('UTF-8')
        a=json.loads(a)
        print(a)
        a=a['text'].encode('UTF-8')
        print(type(a))
        print(a)
        with open(self.filename,'a') as write_file:
            write_file.write(a)


    def on_error(self, b):
        print(b)

  #  def on_status(self, status):
       # print('full_text:', status.text['full_text'])


if __name__=="__main__":
    a_Listen = Listen("tweets1.csv")
    authenticate = OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
    authenticate.set_access_token(Credentials.Access_Token,Credentials.Access_Token_Secret)

    streamer = Stream(authenticate,a_Listen)
    tweets = streamer.filter(track=['CHEARS'])
    #print tweets.text







