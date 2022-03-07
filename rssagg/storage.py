import json
import os
from typing import Iterable

from .common import RSSItem, url_to_filename


class FeedStorage:
    def __init__(self, feed_id: str):
        self._feed_dir = os.path.join("storage", url_to_filename(feed_id))
        os.makedirs(self._feed_dir, exist_ok=True)

    def store(self, item: RSSItem) -> None:
        with open(self._path_for(item.id()), "w") as f:
            json.dump(item.asdict(), f)

    def item_ids(self) -> Iterable[str]:
        return os.listdir(self._feed_dir)

    def load(self, item_id: str) -> RSSItem:
        with open(self._path_for(item_id)) as f:
            return RSSItem(**json.load(f))

    def _path_for(self, item_id: str) -> str:
        return os.path.join(self._feed_dir, item_id)


def storages() -> Iterable[FeedStorage]:
    for folder in os.listdir("storage"):
        yield FeedStorage(folder)
