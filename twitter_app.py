from tweepy import API
from tweepy import OAuthHandler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


import credentials

class TwitterClient(object):
    def __init__(self):
        # do the authentication and return the API object
        auth = OAuthHandler(credentials.API_KEY, credentials.API_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
        self.auth = auth
        self.api = API(self.auth)

    def get_twitter_client_api(self):
        return self.api

if __name__ == '__main__':

    twitter_client = TwitterClient()
    twitter_api = twitter_client.get_twitter_client_api()
    people = ["FreeMemesKids", "neymarjr", "lilpump", "cristiano", "realDonaldtrump", "pewdiepie", "kimkardashian"]
    count = 100

    tweets = {}
    for ppl in people:
        tweets[ppl] = twitter_api.user_timeline(screen_name=ppl, count=count)

    dfs = {}
    for ppl in people:
        dfs[ppl] = pd.DataFrame()
        texts = []
        favs = []
        rets = []
        for tweet in tweets[ppl]:
            texts.append(tweet.text)
            favs.append(tweet.favorite_count)
            rets.append(tweet.retweet_count)

        dfs[ppl]["Text"] = texts
        dfs[ppl]["Favorites"] = favs
        dfs[ppl]["Retweets"] = rets

    # print(dfs)

    # display a graph of average retweets
    y_pos = np.arange(len(people))
    average_ret = []
    for ppl in people:
        average_ret.append(dfs[ppl]["Retweets"].max())

    plt.bar(y_pos, average_ret, align='center', alpha=0.5)
    plt.xticks(y_pos, people)
    plt.ylabel('Retweets')
    plt.title('Most famous on Twitter based on past retweets')
    plt.show()
