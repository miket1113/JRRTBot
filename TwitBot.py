# AUthor: Michael Terranova
# @mikeyt1113
# Github: miket1113


import os
import time
from markovbot import MarkovBot


tweetbot = MarkovBot.MarkovBot()

dir = os.path.dirname(os.path.abspath(__file__))

quotes = os.path.join(dir, 'Quotes.txt')

tweetbot.read(quotes)

first_tweet = tweetbot.generate_text(10)
print('Tolkien: ')
print(first_tweet)

cons_key = 'ylgW0M6gI8uXrOEsLFFLnheoW'
cons_secret = 't1XmD9KlRcllWQwXHFMASxSJZ7eKKNV7kmdn9tqv05lkoT17mN'
access_token = '766721464917712896-i5YcQCcgbgLD2K1PidTyenPjnD3L1wR'
access_token_secret = 'tdx74a4fRf7crogczxreIphFHqov2bmhIQPMjB3lwsEs0'

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)


tweetbot.twitter_tweeting_start(days=1, hours=0, minutes=0, keywords=None, prefix=None, suffix='#PyGaze')


