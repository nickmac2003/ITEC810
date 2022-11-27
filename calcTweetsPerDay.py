import re
from datetime import date, datetime, timedelta

DIRECTORY = 'Scraped_Tweets/'

with open('words.txt') as file:
    word = file.read().splitlines()

word1 = word[0]
#word1 = word1[:-1]
#word1 = word1[1:len(word1)]

word2 = word[1]
#word2 = word2[:-1]
#word2 = word2[1:len(word2)]

word3 = word[2]
#word3 = word3[:-1]
#word3 = word3[1:len(word3)]

word4 = word[3]
#word4 = word4[:-1]
#word4 = word4[1:len(word4)]

word5 = word[4]
#word5 = word5[:-1]
#word5 = word5[1:len(word5)]

file.close()

path = {}
path[0] = DIRECTORY + word1 + '/scrapedTweets.txt'
path[1] = DIRECTORY + word2 + '/scrapedTweets.txt'
path[2] = DIRECTORY + word3 + '/scrapedTweets.txt'
path[3] = DIRECTORY + word4 + '/scrapedTweets.txt'
path[4] = DIRECTORY + word5 + '/scrapedTweets.txt'

pattern = {}
pattern[0] = str(date.today())
pattern[1] = str(date.today() + timedelta(days=-1))
pattern[2] = str(date.today() + timedelta(days=-2))
pattern[3] = str(date.today() + timedelta(days=-3))
pattern[4] = str(date.today() + timedelta(days=-4))
pattern[5] = str(date.today() + timedelta(days=-5))
pattern[6] = str(date.today() + timedelta(days=-6))
pattern[7] = str(date.today() + timedelta(days=-7))
zeroDays = 0
oneDay = 0
twoDays = 0
threeDays = 0
fourDays = 0
fiveDays = 0
sixDays = 0
sevenDays = 0

with open(path[0],"r") as file:
    for line in file:
        if re.search(pattern[0], line):
            zeroDays +=1
        elif re.search(pattern[1], line):
            oneDay +=1
        elif re.search(pattern[2], line):
            twoDays +=1
        elif re.search(pattern[3], line):
            threeDays +=1
        elif re.search(pattern[4], line):
            fourDays +=1
        elif re.search(pattern[5], line):
            fiveDays +=1
        elif re.search(pattern[6], line):
            sixDays +=1
        elif re.search(pattern[7], line):
            sevenDays +=1

print(word1)
print(pattern[0], "-", zeroDays, 'Tweets')
print(pattern[1], "-", oneDay, 'Tweets')
print(pattern[2], "-", twoDays,'Tweets')
print(pattern[3], "-", threeDays, 'Tweets')
print(pattern[4], "-", fourDays, 'Tweets')
print(pattern[5], "-", fiveDays,'Tweets')
print(pattern[6], "-", sixDays, 'Tweets')
print(pattern[7], "-", sevenDays, 'Tweets')
print("")

zeroDays = 0
oneDay = 0
twoDays = 0
threeDays = 0
fourDays = 0
fiveDays = 0
sixDays = 0
sevenDays = 0

with open(path[1],"r") as file:
    for line in file:
        if re.search(pattern[0], line):
            zeroDays +=1
        elif re.search(pattern[1], line):
            oneDay +=1
        elif re.search(pattern[2], line):
            twoDays +=1
        elif re.search(pattern[3], line):
            threeDays +=1
        elif re.search(pattern[4], line):
            fourDays +=1
        elif re.search(pattern[5], line):
            fiveDays +=1
        elif re.search(pattern[6], line):
            sixDays +=1
        elif re.search(pattern[7], line):
            sevenDays +=1

print(word2)
print(pattern[0], "-", zeroDays, 'Tweets')
print(pattern[1], "-", oneDay, 'Tweets')
print(pattern[2], "-", twoDays,'Tweets')
print(pattern[3], "-", threeDays, 'Tweets')
print(pattern[4], "-", fourDays, 'Tweets')
print(pattern[5], "-", fiveDays,'Tweets')
print(pattern[6], "-", sixDays, 'Tweets')
print(pattern[7], "-", sevenDays, 'Tweets')
print("")

zeroDays = 0
oneDay = 0
twoDays = 0
threeDays = 0
fourDays = 0
fiveDays = 0
sixDays = 0
sevenDays = 0

with open(path[2],"r") as file:
    for line in file:
        if re.search(pattern[0], line):
            zeroDays +=1
        elif re.search(pattern[1], line):
            oneDay +=1
        elif re.search(pattern[2], line):
            twoDays +=1
        elif re.search(pattern[3], line):
            threeDays +=1
        elif re.search(pattern[4], line):
            fourDays +=1
        elif re.search(pattern[5], line):
            fiveDays +=1
        elif re.search(pattern[6], line):
            sixDays +=1
        elif re.search(pattern[7], line):
            sevenDays +=1

print(word3)
print(pattern[0], "-", zeroDays, 'Tweets')
print(pattern[1], "-", oneDay, 'Tweets')
print(pattern[2], "-", twoDays,'Tweets')
print(pattern[3], "-", threeDays, 'Tweets')
print(pattern[4], "-", fourDays, 'Tweets')
print(pattern[5], "-", fiveDays,'Tweets')
print(pattern[6], "-", sixDays, 'Tweets')
print(pattern[7], "-", sevenDays, 'Tweets')
print("")

zeroDays = 0
oneDay = 0
twoDays = 0
threeDays = 0
fourDays = 0
fiveDays = 0
sixDays = 0
sevenDays = 0

with open(path[3],"r") as file:
    for line in file:
        if re.search(pattern[0], line):
            zeroDays +=1
        elif re.search(pattern[1], line):
            oneDay +=1
        elif re.search(pattern[2], line):
            twoDays +=1
        elif re.search(pattern[3], line):
            threeDays +=1
        elif re.search(pattern[4], line):
            fourDays +=1
        elif re.search(pattern[5], line):
            fiveDays +=1
        elif re.search(pattern[6], line):
            sixDays +=1
        elif re.search(pattern[7], line):
            sevenDays +=1

print(word4)
print(pattern[0], "-", zeroDays, 'Tweets')
print(pattern[1], "-", oneDay, 'Tweets')
print(pattern[2], "-", twoDays,'Tweets')
print(pattern[3], "-", threeDays, 'Tweets')
print(pattern[4], "-", fourDays, 'Tweets')
print(pattern[5], "-", fiveDays,'Tweets')
print(pattern[6], "-", sixDays, 'Tweets')
print(pattern[7], "-", sevenDays, 'Tweets')
print("")

zeroDays = 0
oneDay = 0
twoDays = 0
threeDays = 0
fourDays = 0
fiveDays = 0
sixDays = 0
sevenDays = 0

with open(path[4],"r") as file:
    for line in file:
        if re.search(pattern[0], line):
            zeroDays +=1
        elif re.search(pattern[1], line):
            oneDay +=1
        elif re.search(pattern[2], line):
            twoDays +=1
        elif re.search(pattern[3], line):
            threeDays +=1
        elif re.search(pattern[4], line):
            fourDays +=1
        elif re.search(pattern[5], line):
            fiveDays +=1
        elif re.search(pattern[6], line):
            sixDays +=1
        elif re.search(pattern[7], line):
            sevenDays +=1

print(word5)
print(pattern[0], "-", zeroDays, 'Tweets')
print(pattern[1], "-", oneDay, 'Tweets')
print(pattern[2], "-", twoDays,'Tweets')
print(pattern[3], "-", threeDays, 'Tweets')
print(pattern[4], "-", fourDays, 'Tweets')
print(pattern[5], "-", fiveDays,'Tweets')
print(pattern[6], "-", sixDays, 'Tweets')
print(pattern[7], "-", sevenDays, 'Tweets')
print("")