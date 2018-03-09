import os
import time
import tweepy
consumer_key=mQ4ukLvNMr8NnxaLVhiK6C8tp
consumer_secret=DqVVV0FsfIuZL7gn5iySsjg7ibgIU3vpK3vCxPXlgjCn9kZk3x
access_token=966898413588570112-lGG1zCA872OdMAyYvVy39uA7EcVVuVQ
access_token_secret=S61EUPmckFjFyojnR2VSglrvOBDhZixqxcv6f1mARqsx5


auth=tweepy.OAuthHandler
auth.set_access_token_(access_token, access_token_secret)
api=tweepy.api(auth)
a=0
b=1
while(a<2):
    img="/home/user/desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 1200*800 "+img
    os.system(cmd)
    print("selfie taken")
    file = open(img,'rb')
    data =file.read()
    api.upload_with_media(img,status="pic of the day")
    print("wait for 5 seconds")
    time.sleep(5)
    a+=1
    b+=1
    print("success")

