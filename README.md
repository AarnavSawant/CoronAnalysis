# CoronAnalysis
This project takes tweets from Twitter about COVID-19 and perform Latent Dirochlet Allocation to create WordClouds for the tweets and perform Sentiment Analysis on the tweets. Be sure to check the images folder for all of my Sentiment Charts and WordClouds.
###### To get tweets from Twitter:
1. Take tweetReader.py and enter your Twitter Developer Key.
2. Navigate to the CoronAnalysis/code in a Terminal and execute `python tweetReader.py > twitter_data.txt`. This will store the tweets in JSON Format in twitter_data.txt
###### To convert the textfile to a CSV:
1. Use the CSVWriter script and change the rows according to the Twitter Data you would like to use
###### To run the NLP:
1. Put the correct CSV file and correct column for the text so pandas reads the text.


