import csv
import json
tweets_data_path = "5-14-2020.txt"
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

# tweets_file2 = open(tweets_data_path2, "r")
# for line in tweets_file2:
#     try:
#         tweet = json.loads(line)
#         tweets_data.append(tweet)
#     except:
#         continue
# tweets_file3 = open(tweets_data_path3, "r")
# for line in tweets_file2:
#     try:
#         tweet = json.loads(line)
#         tweets_data.append(tweet)
#     except:
#         continue

<<<<<<< HEAD


fields = ["created_at", "text", "lang", "coordinates", "location"]
file = open("../tweets/5-14-2020.csv", "w")
texts = []
=======
fields = ["created_at", "text", "lang", "coordinates"] #This line determines what fields get written to the csv
file = open("../tweets/twitter_data.csv", "w")
>>>>>>> 64a02cc09c09a68f572a9627cb1b0d51b9b47ec3
writer = csv.writer(file)
writer.writerow(fields)
for row in tweets_data:
    if row.get("text") not in texts and not row.get("text") is None:
        print(row)
        writer.writerow([row.get("created_at"), row.get("text").encode('unicode_escape'), row.get("lang"), row.get("coordinates"), row.get("location")])
        texts.append(row.get("text"))

file.close()
