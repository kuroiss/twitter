import tweepy
import random
import time

CONSUMER_KEY = '***************************'
CONSUMER_SECRET = '*****************************************************'
ACCESS_TOKEN = '*************************************************'
ACCESS_SECRET = '********************************************'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

test_list = ["Excellent", "Good", "Mediunm", "Bad", "Very Bad"]

while 1:
    TL = api.mentions_timeline()
    for reply_TL in TL:
        print("--------------------------------")
        print(reply_TL.user.name + "@" + str(reply_TL.user.screen_name) + "\n")
        print(reply_TL.text + "\n")


        if "fortune" in reply_TL.text:
            api.update_status("@" + str(reply_TL.user.screen_name) + " " + random.choice(test_list))

    print("Now loading... \n")
    time.sleep(60)
