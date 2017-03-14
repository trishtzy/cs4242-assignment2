import ass2_read_data as main
import datetime as dt

TWEET_INFO_PATH = 'dataset/k4/root_tweet.json'

TS_PATH = 'dataset/k4/testing.json'

TR_PATH = 'dataset/k4/training.json'

K = 4


def calc_avg_time(timestamps):
    total_time_diff = dt.timedelta(microseconds=0)
    for i in range(0, K):
        timeA = dt.datetime.fromtimestamp(int(timestamps[i])/1000)
        if i+1 >= K :
            break
        timeB = dt.datetime.fromtimestamp(int(timestamps[i+1])/1000)
        time_diff = timeB - timeA
        total_time_diff += time_diff
    avg = total_time_diff / (K-1)
    # minute, sec = divmod(avg.total_seconds(), 60)
    return avg.total_seconds()


def temporal(cascade):
    timestamps = []
    for i in range(1, K+1):
        timestamps.append(cascade[str(i)]['created_at'])
    return calc_avg_time(timestamps)

if __name__ == '__main__':
    tr, ts = main.read_data(TR_PATH, TS_PATH)

    for url in tr:
        print(url)
        cascade = tr[url]
        seconds = temporal(cascade)
        print(str(seconds) + ' sec')

