import requests
import random

#wordList = "https://www.mit.edu/~ecprice/wordlist.10000"
WORDS = ["Chiefs","Jayhawks","Mizzou","Royals","RockChalk","Comets","Bearcats","KSU","Wildcats","Monarchs","KU"]

#response = requests.get(wordList)
#WORDS = response.content.splitlines()

#print(WORDS)
word1 = random.choice(WORDS)
word2 = random.choice(WORDS)
word3 = random.choice(WORDS)
word4 = random.choice(WORDS)
word5 = random.choice(WORDS)

with open("words.txt", 'w') as f:
        f.write(word1 + '\n')
        f.close()

with open("words.txt", 'a') as f:
        f.write(word2 + '\n')
        f.write(word3 + '\n')
        f.write(word4 + '\n')
        f.write(word5)
        f.close()
