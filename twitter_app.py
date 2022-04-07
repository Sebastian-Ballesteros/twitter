from tweepy import API, OAuth1UserHandler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import credentials

count = 10

def TwitterClient():
    # do the authentication and return the API object
    auth = OAuth1UserHandler(credentials.API_KEY, credentials.API_SECRET, credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
    api = API(auth)

    print(api.verify_credentials().screen_name)
    return api


if __name__ == '__main__':
    twitter_api = TwitterClient()
    people = ["neymarjr", "lilpump", "cristiano", "kimkardashian", "elonmusk"]

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

    # display a graph of average favorites
    y_pos = np.arange(len(people))
    average = []
    for ppl in people:
        average.append(np.average(dfs[ppl]['Favorites'].values))
        print(f"\b\n{ppl} most favorites tweet: \n {dfs[ppl]['Text'][np.argmax(dfs[ppl]['Favorites'].values)]}\n Number of favorites {np.max(dfs[ppl]['Favorites'].values)}")

    plt.bar(y_pos, average, align='center', alpha=0.8)
    plt.xticks(y_pos, people)
    plt.ylabel('Favorites')
    plt.title('Most famous on Twitter based on past favorites')
    plt.show()
