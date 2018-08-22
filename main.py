import firstfile as ff
import wordcount as ww
import Example as eg
import big_query_trending as trends
import big_query_tweets_file as tweets
import big_query_count_file as tweetcount




def main():
    ww.get_trending()
    print('trending topics generated')
    ww.get_tweets()
    print('tweets based on trending topics are generated')
    eg.run()
    print('Apache beam pipeline working and counting tweets words')
    trends.upload_trending()
    tweets.upload_tweets()
    tweetcount.upload_wordcount()


if __name__ == '__main__':
    main()
