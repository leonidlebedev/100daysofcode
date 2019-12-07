from collections import namedtuple, defaultdict, Counter
import json

FILE_NAME = 'example.json'
Channel_Info = namedtuple('Channel_Info', ['author', 'email', 'subscribers'])

def get_channels(filename):
    channels = defaultdict(list)

    with open(filename, 'r') as f:
        data = json.load(f)

        for channel in data:
            try:
                id = channel['channel_id']
                author = channel['author']
                email = channel['email']
                subscribers = channel['subscribers']
            except:
                continue

            info = Channel_Info(author, email, subscribers)
            channels[id] = info

    return channels

def get_top_channels_by_subscribers(channels, n=10):
    return Counter(sorted(channels.items(), key=lambda k_v: k_v[1].subscribers, reverse=True)).most_common(n)


channels = get_channels(FILE_NAME)
top = get_top_channels_by_subscribers(channels, 5)
print('---', top)