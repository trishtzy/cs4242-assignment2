import ass2_read_data as main
import enhanced
import basic
import numpy as np
from sklearn import svm
import json

TS_PATH = 'dataset/k4/testing.json'

TR_PATH = 'dataset/k4/training.json'

OUT_FILE = 'testing_online_prediction.json'

# This is a pseudocode for classifer. Please change your parameters and function name accordingly.

def write2json(data):
    with open(OUT_FILE, 'w') as f:
        f.write(json.dumps(data))


def basic_classify(tr, ts):
    train = basic.get_vectors(tr)
    tests = basic.get_vectors(ts)
    labels = main.extract_labels2(tr, 4)

    clf = svm.SVC()
    clf.fit(train, labels)
    for test in tests:
        ts[url]['predicted_label'] = clf.predict(test)

    write2json(ts)



def enhanced_classify(tr, ts):
    basic_train = basic.get_vectors(tr)
    basic_tests = basic.get_vectors(ts)
    train = enhanced.get_vectors(tr).concatenate(basic_train)
    tests = enhanced.get_vectors(ts).concatenate(basic_tests)

    labels = main.extract_labels2(tr, 4)
    clf = svm.SVC()
    clf.fit(train, labels)
    for test in tests:
        ts[url]['predicted_label'] = clf.predict(test)

    write2json(ts)


if __name__ == '__main__':
    tr, ts = main.read_data(TR_PATH, TS_PATH)
    basic_classify(tr, ts)
    enhanced_classify(tr, ts)

