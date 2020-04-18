import datetime
import numpy as np
import tweepy.streaming
from tweepy import Stream, OAuthHandler
import csv
import sys
import pandas as pd
import re

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

class StdOut(tweepy.StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOut()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)
    stream.filter(track=["shortness of breath" , "sore throat" , "headache" , "respiratory virus" , "bronchoalveolar lavage fluid" , "ground glass opacities" , "Bluish lips or face", "Real-Time RT-PCR Diagnostic Panel", "myalgia", "fever 100", "fever 38C", "rhinorrhea", "dyspnea", "Nausea"])




