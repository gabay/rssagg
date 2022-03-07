import argparse

from . import rss, storage


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--feeds", default="feeds.txt")

    return parser.parse_args()


def main():
    args = parse_args()

    with open(args.feeds) as f:
        feeds = f.read().splitlines()

    for feed in feeds:
        print(feed)
        channel = rss.fetch(feed)
        feed_storage = storage.FeedStorage(feed)
        for item in channel.items:
            feed_storage.store(item)


if __name__ == "__main__":
    main()
