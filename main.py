import read_data
import logging
import basic

K = 4
RT_PATH = 'dataset/k%d/root_tweet.json' % K
TR_PATH = 'dataset/k%d/training.json' % K
TS_PATH = 'dataset/k%d/testing.json' % K    ### TO BE CHANGED FOR EVALUATION
SN_PATH = 'social_network.json'

def main():
    # create logger
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    logger.debug('Loading training data '+TR_PATH)
    training_data = read_data.read_data(TR_PATH,100)
    logger.debug('Loading testing data '+TS_PATH)
    testing_data = read_data.read_data(TS_PATH)
    logger.debug('Loading social network '+SN_PATH)
    social_network = read_data.read_data(SN_PATH)
    logger.debug('Loading root tweets '+RT_PATH)
    root_data = read_data.read_data(RT_PATH)


    # extract_labels
    labels = read_data.extract_labels(training_data, K)

    # run basic features
    basic_vectors = basic.get_vectors(root_data, training_data, social_network)

    # run enhanced features


if __name__ == '__main__':
    main()
