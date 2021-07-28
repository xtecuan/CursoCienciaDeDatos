import credentials
import tweepy

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

id = None
count = 0
lines = 100
busqueda = ["El Salvador", "La Selecta"]
while count <= lines:

    tweets = api.search(q=busqueda, lang='es', tweet_mode='extended', max_id=id)

    for tweet in tweets:
        #if tweet.full_text.startswith('RT'):
            #count += 1
            #continue

        f = open('./tweets.txt', 'a', encoding='utf-8')
        f.write(tweet.full_text + '\n')
        f.close

        count += 1

    id = tweet.id
    print(count)