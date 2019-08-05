import tweepy
import random
import time

CONSUMER_KEY = '8xmbSbWyHEq5RyvozZ3hpAsDA'
CONSUMER_SECRET = 'J5Uih3LzIQYhqQIOVMj8VOtNdoDI72w9cB6A87J7Fi9Hr3J5jr'
ACCESS_TOKEN = '2368833176-jX2uGlIbhQiZkSWMGOKZwX0RIbKd9FqIx2uhP47'
ACCESS_SECRET = 'yHwPRtlX4YLJ2AxPjYzj5NigUz7bSKwDekhA69UaVQyOd'
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
