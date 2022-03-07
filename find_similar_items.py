import difflib
import itertools
from typing import List

from rssagg.common import RSSItem
from rssagg.storage import FeedStorage, storages


def find_similar_items(channels: List[FeedStorage]) -> None:
    for a, b in itertools.combinations(channels, 2):
        for a_item_id, b_item_id in itertools.product(a.item_ids(), b.item_ids()):
            a_item = a.load(a_item_id)
            b_item = b.load(b_item_id)
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
