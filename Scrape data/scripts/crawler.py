def get_tweets(screen_names):
    a_ids = []
    a_times = []
    a_texts = []
    a_favs = []
    a_retweets = []
    a_entities = []
    a_languages = []
    a_hashtag=[]
    a_user_names = []
    a_descriptions = []
    a_followers = []
    a_friends = []
    a_tweet_count = []
    a_verified = []
    a_created_at = []
    a_location = []

    
    for name in screen_names:
        
        ids = []
        times = []
        texts = []
        favs = []
        retweets = []
        entities = []
        langs = []
        hash_=[]
        user_names = []
        descriptions = []
        followers = []
        friends = []
        tweet_count = []
        verify = []
        created_at = []
        locations = []
        
        tweets = tweepy.Cursor(api.user_timeline, screen_name = name, since = '2019-12-01', wait_on_rate_limit=True).items(500)
        for tweet in tweets:
#             for i in tweet.entities['hashtags']:
#                 if i['text'].lower() in hashtag2:
            id_ = tweet.id_str
            time = tweet.created_at
            text_ = tweet.text
            fav = tweet.favorite_count
            retweet = tweet.retweet_count
            entities_ = tweet.entities
            hashtag_=[x['text'] for x in  tweet.entities['hashtags']]
            lang = tweet.lang
            name = tweet.user.screen_name
            desc = tweet.user.description
            followers_count = tweet.user.followers_count
            following = tweet.user.friends_count
            tweets = tweet.user.statuses_count
            very = tweet.user.verified
            created_at_ = tweet.user.created_at
            location = tweet.user.location

            ids.append(id_)
            times.append(time)
            texts.append(text_)
            favs.append(fav)
            retweets.append(retweet)
            entities.append(entities_)
            langs.append(lang)
            hash_.append(hashtag_)
            user_names.append(name)
            descriptions.append(desc)
            followers.append(followers_count)
            friends.append(following)
            tweet_count.append(tweets)
            verify.append(very)
            created_at.append(created_at_)
            locations.append(location)

            a_ids.append(ids)
            a_times.append(times)
            a_texts.append(texts)
            a_favs.append(favs)
            a_retweets.append(retweets)
            a_entities.append(entities)
            a_languages.append(langs)
            a_hashtag.append(hash_)
            a_user_names.append(user_names)
            a_descriptions.append(descriptions)
            a_tweet_count.append(tweet_count)
            a_friends.append(friends)
            a_followers.append(followers)
            a_verified.append(verify)
            a_created_at.append(created_at)
            a_location.append(locations)


    a_ids = [y for x in a_ids for y in x]
    a_times = [y for x in a_times for y in x]
    a_texts = [y for x in a_texts for y in x]
    a_favs = [y for x in a_favs for y in x]
    a_retweets = [y for x in a_retweets for y in x]
    a_entities = [y for x in a_entities for y in x]
    a_languages = [y for x in a_languages for y in x]
    a_hashtag = [y for x in a_hashtag for y in x]
    a_descriptions = [y for x in a_descriptions for y in x]
    a_followers = [y for x in a_followers for y in x]
    a_tweet_count = [y for x in a_tweet_count for y in x]
    a_friends = [y for x in a_friends for y in x]
    a_verified = [y for x in a_verified for y in x]
    a_created_at = [y for x in a_created_at for y in x]
    a_location = [y for x in a_location for y in x]
    a_user_names = [y for x in a_user_names for y in x]
    
    
        
    df = pd.DataFrame({'id':a_ids, 'time':a_times, 'screen_name':a_user_names, 'desc':a_descriptions, 
                       'friends':a_friends, 'no_tweets':a_tweet_count, 'followers':a_followers, 'location':a_location, 
                       'text':a_texts, 'favourite_count':a_favs, 'created_at':a_created_at, 'verified':a_verified, 
                       'retweet_count':a_retweets,'entities':a_entities, 'lang':a_languages,'hashtag':a_hashtag})
    return df 
