import json
import logging
import os.path
from dateutil.parser import parse
import datetime

# create logger
logger = logging.getLogger('main.read_data')


def read_data(path, limit=-1):
    """Given a path to JSON file, load and return contents up to limit items."""
    logger.debug("Reading " + path)
    if (not os.path.isfile(path)):
        logger.error("File " + path + " does not exist!")
        return None
    with open(path, 'r') as f:
        data = json.load(f)
    logger.debug("Loaded %d items" % len(data))
    if limit < 0:
        return data
    count = 0
    new_data = {}
    for d in data:
        new_data[d] = data[d]
        count += 1
        if count >= limit:
            return new_data
    return new_data


def read_tweet_content(tw_id):
    """Given tweet ID, load and return tweet contents"""
    with open('tweets/'+tw_id+'.json', 'r') as f:
        tw_content = json.load(f)
    return tw_content


'Return the integer id of the root of the cascade (because 1 sometimes may be missing)'
def find_root_of_cascade(cascade):
    tweets = cascade.keys()
    return str(sorted(map(int, tweets))[0])


'''Get the label viral/non-viral (True or False) for a cascade.'''
def get_label(cascade, k):
    return len(cascade) >= 2*k

def extract_labels(dataset, k):
    """Extract viral labels from dataset - WORKING FUNCTION"""
    labels={}
    for key in dataset:
        labels[key] = get_label(dataset[key], k)

    return labels

def parse_datetime(datetime_str):
    """Takes in datetime string in format "1285421777000" or "Tue Aug 31 14:57:43 +0000 2010"
    and returns datetime object"""
    try:
        return datetime.datetime.fromtimestamp(int(datetime_str)/1000)
    except ValueError:
        return parse(datetime_str)


def json_datetime(obj):
    """JSON serializer for datetime objects
    Change this to the required format for outputting json for evaluation"""
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

# if __name__ == '__main__':
#     tr, ts = read_data('dataset/k4/training.json', 'dataset/k4/testing.json')
#     inspect_data(tr, 'dataset/k4/root_tweet.json')
#     social_network = read_social_network('social_network.json')
#     ft = extract_example_features(tr, social_network)
#     tr_labels = extract_labels(tr, 4)
