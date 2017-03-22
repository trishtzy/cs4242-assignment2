import json
import logging
import read_data
from afinn import Afinn
from langdetect import detect

# create logger
logger = logging.getLogger('main.basic')

afinn = Afinn()

def get_vectors(root_data, data, social_network):
    vects = {}

    logger.debug("DATA:")
    logger.debug(json.dumps(data))

    for key in data:
        vect = {}
        logger.debug("Processing " +key)
        cascade = data[key]
        # logger.debug("CASCADE:")
        # logger.debug(json.dumps(cascade))
        root = read_data.find_root_of_cascade(cascade)
        user = cascade[root]['user']
        tweet_id = cascade[root]['id']
        tweet = read_data.read_tweet_content(tweet_id)
        vect["followees"] = get_followees(social_network, user)
        vect["sentiment"] = get_afinn_sentiment(tweet["text"])
        vect["hashtags"] = get_number_hashtags(tweet["text"])
        vect["followers"] = tweet["user"]["followers_count"]
        vect["user_since"] = read_data.parse_datetime(tweet["user"]["created_at"])
        vect["user_tweets"] = tweet["user"]["statuses_count"]
        #vect["user_location"] = tweet["user"]["location"]
        if tweet["geo"] or tweet["coordinates"]:
            vect["has_geotag"] = 1
        else:
            vect["has_geotag"] = 0
        vect["lang"] = tweet["lang"]
        vect["langdetect"] = get_langdetect(tweet["text"])


        vects[key] = vect

    logger.debug(json.dumps(vects, default=read_data.json_datetime))

def get_followees(social_network, user):
    """Given user, returns number of followees"""
    try:
        return len(social_network[user])
    except KeyError:
        logger.warn("User " + user + " not found in social network!")
        return -1

def get_afinn_sentiment(tweet_text):
    """Given tweet text, use Afinn to return sentiment score"""
    return afinn.score(tweet_text)


def get_number_hashtags(tweet_text):
    """Given tweet id, count the number of hashtags"""
    count = 0
    for word in tweet_text.split():
        if word.startswith("#"):
            count += 1
    return count

def get_langdetect(tweet_text):
    return detect(tweet_text)
