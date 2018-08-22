import firstfile as ff
import wordcount as ww
import Example as eg
import big_query_trending as trends
import big_query_tweets_file as tweets
import big_query_count_file as tweetcount




def main():
    ww.get_trending()
    ww.get_tweets()
    eg.run()
    trends.upload_trending()
    tweets.upload_tweets()
    tweetcount.upload_wordcount()


if __name__ == '__main__':
    main()
