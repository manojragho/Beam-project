# I am using tweepy package for interaction with twitter API
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
import csv
import string


import json



import Credentials

class Listen(StreamListener):

    def __init__(self,filename,topic):
        self.filename = filename
        self.num_tweets = 0
        self.topic=topic
        self.printable = set(string.printable)

    def on_data(self, a):
        try :
            if(self.num_tweets  > 4) :
                return False;
            self.num_tweets=self.num_tweets+1
            a = a.encode('UTF-8')
            a = json.loads(a)
            a = a['text'].encode('UTF-8')
            #print(a)
            #a = filter(lambda x: x in self.printable, a)
            print(a)

            with open(self.filename, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ', lineterminator='\n')
                count = 0
                spamwriter.writerow([a])
                count = count + 1
                '''
            with open(self.filename, 'a') as write_file:
                write_file.write(a)
                write_file.write("\n")
                '''


        except Exception:
            pass

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







