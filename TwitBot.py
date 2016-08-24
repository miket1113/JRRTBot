# AUthor: Michael Terranova
# @mikeyt1113
# Github: miket1113


import os
import time
from markovbot import MarkovBot


tweetbot = MarkovBot.MarkovBot()

dir = os.path.dirname(os.path.abspath(__file__))

quotes = os.path.join(dir, 'Tol Quotes.txt')

tweetbot.read(quotes)

first_tweet = tweetbot.generate_text(10)
print('Tolkien: ')
print(first_tweet)

cons_key = #left empty intentioanlly, enter your own
cons_secret = #left empty intentioanlly, enter your own
access_token = #left empty intentioanlly, enter your own
access_token_secret = #left empty intentioanlly, enter your own 

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)


tweetbot.twitter_tweeting_start(days=1, hours=0, minutes=0, keywords=None, prefix=None, suffix=None)

secsinweek = 7 * 24 * 60 * 60
time.sleep(secsinweek)





