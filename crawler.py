# Import the needed packages
import csv
from functions import *
from textblob import TextBlob
import tweepy
from tweepy import OAuthHandler

# Set the Directory and the Maximum amount of tweets to scrape.
DIRECTORY = 'Scraped_Tweets/'
MAX_TWEETS = 1000

# Define the Twitter Crawler class to setup and connect to the twitter api
class TweetCrawler:

    def __init__(self):
        self.api = ''
        self.access_token = '1573152022299398147-xI6kglHXpAaQUi2ncVdQYFHskSpGbA'
        self.access_token_secret = 'X8ObJ411hbafScMLRuK9AM2h96sH1N4cSp9q6zcssKCSI'
        self.consumer_key = 'RUHoLs03QSb3awIlD451cVdSr'
        self.consumer_secret = 'iY1DepXgviki4l5Coml9whR0KBeg5fGrbNiqWTMRDdzsnTfbbK'
        self.buildAPI()
        create_directory(DIRECTORY)

    # Function to Authenticate to the API
    def buildAPI(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    # Function to read the tweets that have already been scraped.
    def readTweets(self, keyword):
        path = DIRECTORY + keyword + '/scrapedTweets.txt'
        content = []
        with open(path, 'r') as f:
            data = f.read()
            data = data.split('<#@#>')
            content = [x for x in data if not x == '']
        print(content)
        return content

    # Function to search tweets by keyword
    def searchTweets(self, keyword):
        public_tweets = self.api.search_tweets(keyword)
        self.writeTweet(keyword, public_tweets)
        return public_tweets

    # Function to search tweets by hashtag
    def searchHashtag(self, keyword):
        hashtag = keyword
        count = 0
        HASHTAG_DIRECTORY = DIRECTORY + hashtag + '/'
        create_directory(HASHTAG_DIRECTORY)
        path = HASHTAG_DIRECTORY + 'scrapedTweets.txt'
        for tweet in tweepy.Cursor(self.api.search_tweets, q='#' + hashtag, rpp=10000, lang="en", since_id=0).items(MAX_TWEETS):
            count += 1
            tweetDate = tweet.created_at
            append_data(path, str(tweetDate) + ' ' + tweet.text + '<#@#>')
        count = 0

    # Function to use the sentiment api to crawl and analyze the tweets that get scraped

    # Function to get the tweets from the users timeline
    def timeLine(self):
        timelines = ''
        for tweet in tweepy.Cursor(self.api.user_timeline).items():
            tweetDate = tweet.created_at
            timelines = (str(tweetDate) + ' ' + tweet.text + '<#@#>')
        create_file(DIRECTORY, 'timeline.txt', timelines)

    # Function to write the tweets to the scraped tweets text file
    def writeTweet(self, keyword, tweets):
        THIS_DIR = DIRECTORY + keyword + '/'
        create_directory(THIS_DIR)
        path = THIS_DIR + 'scrapedTweets.txt'
        for tweet in tweets:
            tweetDate = tweet.created_at
            append_data(path, str(tweetDate) + ' ' + tweet.text + '<#@#>')
