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


screen_name_me = "*************" #your twitter ID(screen name)
while 1:
    TL_usr = api.user_timeline(screen_name = screen_name_me)
    for TL in TL_usr:
        if(not TL.retweeted) and ("@" not in TL.text):
            if("みんなで早押しクイズ" in TL.text):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(TL.text)
                print(TL.created_at)
                print(TL.source)
                
                api.destroy_status(TL.id)
                # print("--------------------------------")
                # print(reply_TL.user.name + "@" + str(reply_TL.user.screen_name) + "\n")
                # print(reply_TL.text + "\n")
                print("ツイートは削除されました\n")

    print("Now loading... \n")
    time.sleep(60)
