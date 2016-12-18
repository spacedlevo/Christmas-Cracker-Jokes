import tweepy
import random

def postJoke(joke):

    consumer_key = # ADD CONSUMER KEY
    consumer_secret = # ADD CONSUMER SECRET
    access_token = # ADD ACCESS TOKEN
    access_token_secret = # ADD ACCESS TOKEN

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    api.update_status(status=joke)

def getJoke():

    openFile = open(r'D:\Programming\JokeBot\crackerjokes.txt', 'r')
    jokes = openFile.readlines()
    openFile.close()

    joke = jokes[random.randint(0,(len(jokes)-1))]
    joke = str(joke)
    if len(joke) < 140:
        print(joke)
        postJoke(joke)
    else:
        getJoke()

getJoke()
