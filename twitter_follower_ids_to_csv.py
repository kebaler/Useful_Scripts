import yaml
import tweepy
import time
import csv

credentials = yaml.load(open('keeb_credentials.yaml'))
auth = tweepy.OAuthHandler(credentials['CONSUMER_KEY'], credentials['CONSUMER_SECRET'])
auth.set_access_token(credentials['OAUTH_TOKEN'], credentials['OAUTH_TOKEN_SECRET'])

api = tweepy.API(auth)

# variable for target screen name to get follower id list from 
target_sn='DLSoftwareDeal'

ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name=target_sn).pages():
    ids.extend(page)
    time.sleep(60)

print len(ids)

# creates csv named to target screen name 
csvfile = target_sn + "_follower_ids.csv"

# Write csv from ID list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in ids:
        writer.writerow([val])

###