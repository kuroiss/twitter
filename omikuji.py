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

test_list = ["大吉", "中吉", "中吉", "吉", "吉", "吉", "末吉", "末吉", "末吉", "末吉", "凶", "凶", "大凶"]
list_detect = ["おみくじ", "おみくしﾞ", "おみくし゛", "おみㄑじ"]
reply_list = list(range(1000))

while 1:
    TL = api.mentions_timeline()
    for reply_TL in TL:
        for detection in list_detect:
            if (detection in reply_TL.text) and (reply_TL.id not in reply_list):
                print("--------------------------------")
                print(reply_TL.user.name + "@" + str(reply_TL.user.screen_name) + "\n")
                print(reply_TL.text + "\n")
            
                api.update_status("@" + str(reply_TL.user.screen_name) + " " + random.choice(test_list), in_reply_to_status_id = reply_TL.id)
                reply_list.append(reply_TL.id)

    print("Now loading... \n")
    time.sleep(60)
