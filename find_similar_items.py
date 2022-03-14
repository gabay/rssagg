import difflib
import itertools
from typing import List

from rssagg.common import RSSItem
from rssagg.storage import FeedStorage, storages


def find_similar_items(channels: List[FeedStorage]) -> None:
    channel_items = {channel: list(channel.items()) for channel in channels}
    for a, b in itertools.combinations(channel_items, 2):
        for a_item, b_item in itertools.product(channel_items[a], channel_items[b]):
            if is_similar(a_item, b_item):
                print(a_item)
                print(b_item)


def is_similar(a: RSSItem, b: RSSItem) -> bool:
    if difflib.SequenceMatcher(a.title, b.title).ratio() > 0.5:
        if difflib.SequenceMatcher(a.description, b.description).ratio() > 0.5:
            return True
    return False


def main():
    channels = list(storages())
    find_similar_items(channels)


if __name__ == "__main__":
    main()
