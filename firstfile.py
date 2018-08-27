# I am using tweepy package for interaction with twitter API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import csv
import string
import time
import xlsxwriter


import json



import Credentials

class Listen(StreamListener):

    def __init__(self,filename,topic):

        self.filename = filename
        self.num_tweets = 0
        self.topic=topic
        self.printable = set(string.printable)
        self.start_time=time.time()
        self.time_limit=45
        self.tweet_topic='tweet_topic.csv'

    def on_timeout(self):
        print('timeout occured')
    def on_data(self, a):
        try :
            #print(a)
            a = a.encode('UTF-8')
            a = json.loads(a)
            b=a['retweeted_status']['entities']['hashtags'][0]['text']
            self.topic=str(b)
            print(self.topic)
        except Exception:
            return True
        try :

            self.curr_time=time.time();
            if(self.curr_time-self.start_time) > self.time_limit:
                return False
            if(self.num_tweets  > 50) :
                return False;
            self.num_tweets=self.num_tweets+1

            a = a['text'].encode('UTF-8')
            print(a)
            #a = filter(lambda x: x in self.printable, a)

            with open(self.tweet_topic, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
                count = 0
                writer.writerow([self.topic + ':' + str(a)])
                count = count + 1
            with open(self.filename, 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
                count = 0
                writer.writerow([str(a)])
                count = count + 1




        except Exception:
            pass


    def on_error(self, b):
        return False





if __name__=="__main__":
    a_Listen = Listen("tweets1.csv")
    authenticate = OAuthHandler(Credentials.Consumer_Key,Credentials.Consumer_Secret)
    authenticate.set_access_token(Credentials.Access_Token,Credentials.Access_Token_Secret)

    streamer = Stream(authenticate,a_Listen)
    tweets = streamer.filter(track=['CHEARS'])

    #print tweets.text







