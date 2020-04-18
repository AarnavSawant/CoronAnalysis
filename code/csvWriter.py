import csv
import json
tweets_data_path = "../tweets/twitter_data.txt"
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue


fields = ["created_at", "text", "lang", "coordinates"] #This line determines what fields get written to the CSV
file = open("../tweets/twitter_data.csv", "w")
writer = csv.writer(file)
writer.writerow(fields)
for row in tweets_data:
    writer.writerow([row.get("created_at"), row.get("text").encode('unicode_escape'), row.get("lang"), row.get("coordinates")])

file.close()
