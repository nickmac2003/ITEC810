#!/bin/bash
#
#  Author:    Nick MacDonald
#  Name:      moveInc.sh
#  Version:   1.0
#  Purpose:   This script is to control the flow of execution for the Move Inc. Twitter crawler program.

countTweets() {
 sudo python3 main.py --count $1
}

generateWords() {
  sudo python3 words.py
}

searchTweets() {
  sudo python3 main.py --hashtag '$1'
}

words() {
  wordList=`grep '' words.txt`
  if [[ $1 == "" ]]; then
      exit;
  elif [[ $1 == "all" ]]; then
      for word in $wordList
     do
#       echo $word
       searchTweets $word
       countTweets $word
     done
  else
  word=$1
   searchTweets $word
   countTweets $word
  fi
}

findResults() {
  sudo python3 calcTweetsPerDay.py
}

# Beginning of 'Main'

#sudo rm -r Scraped_Tweets
#sudo mkdir Scraped_Tweets
clear
generateWords
echo
words all
#sleep 10
echo
findResults
