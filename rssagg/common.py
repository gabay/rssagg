from dataclasses import asdict, dataclass
from typing import List

import bs4


@dataclass
class RSSItem:
    title: str
    description: str
    link: str
    pub_date: str

    @classmethod
    def from_xml(cls, xml: bs4.BeautifulSoup) -> "RSSItem":
        title = trim_html(xml.title.text)
        description = trim_html(xml.description.text)
        link = xml.link.text
        pub_date = xml.pubDate.text
        return cls(title, description, link, pub_date)

    def id(self):
        return f"{self.pub_date}_{url_to_filename(self.link)}"

    def asdict(self) -> dict:
        return asdict(self)


@dataclass
class RSSChannel:
    url: str
    title: str
    items: List[RSSItem]

    @classmethod
    def from_xml(cls, url: str, xml: bs4.BeautifulSoup) -> "RSSChannel":
        title = trim_html(xml.title.text)
        items = [RSSItem.from_xml(item_xml) for item_xml in xml.find_all("item")]
        return cls(url, title, items)

    def id(self):
        return url_to_filename(self.url)

    def asdict(self) -> dict:
        return asdict(self)


def trim_html(text):
    # Some RSS feeds embed HTML inside their description text. Remove it.
    return bs4.BeautifulSoup(text, "html.parser").text


def url_to_filename(url: str) -> str:
    return url.split("://", 1)[-1].replace("/", "_")
