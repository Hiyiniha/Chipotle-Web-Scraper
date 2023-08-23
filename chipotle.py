import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import time
import requests
from imessage_reader import fetch_data
from py_imessage import imessage

#Phone number of receiver
phone = "888222"

#Query search of chipotle twitter
query = "(from:ChipotleTweets) since:2023-04-06"

limit = 1 #number of tweets grabbed
promo = '' #promo code in tweet

while True:
    tweets = [] #list of tweets
    word = [] #list of words in tweet
    
    #Web scrape the most recent tweet from Chipotle
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        #Checks if tweet contains the number to send
        if "888222" in tweet.rawContent:
            tweets.append([tweet.rawContent])

    #Search tweet for promo code
    for tweet in tweets:
        for word in tweet:
            for ss in word.split():
                #Every promo code contains FREE in it
                if "FREE" in ss:
                    #Checks if promo code has already been used
                    if promo != ss:
                        promo = ss
                        #Send code to receiever using iMessage
                        os.system("osascript sendMessage.applescript {} {}".format(phone, promo))
