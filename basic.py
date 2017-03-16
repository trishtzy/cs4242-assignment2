import json
import logging
import read_data

# create logger
logger = logging.getLogger('main.basic')

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
        vect["followees"] = get_followees(social_network, user)


        vects[key] = vect

    logger.debug(json.dumps(vects))

def get_followees(social_network, user):
    '''Given user, returns number of followees'''
    try:
        return len(social_network[user])
    except KeyError:
        logger.warn("User " + user + " not found in social network!")
        return -1
