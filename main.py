# Import packages
from sys import argv
from crawler import TweetCrawler


# If statements that give the options the user has when running the program
def mainFunc():
    tweet_crawler = TweetCrawler()
    if '--search' in argv:  # search <keyword>
        tweet_crawler.searchTweets(argv[2])
    elif '--searchHistorical' in argv:  # search old tweets by <keyword>
        tweet_crawler.searchHistorical(argv[2])
    elif '--hashtag' in argv:  # hashtag search <#keyword>
        tweet_crawler.searchHashtag(argv[2])
    elif '--timeline' in argv:  # get tweets from account timeline and write to timeline text file
        tweet_crawler.timeLine()
    elif '--file' in argv:  # read from the scraped tweets text file
        tweet_crawler.readTweets(argv[2])
   

# Start the main program to run the if statements
if __name__ == '__main__':
    mainFunc()
