import bs4
import requests

from .common import RSSChannel


def fetch(url: str) -> RSSChannel:
    response = requests.get(url)
    xml = bs4.BeautifulSoup(response.content.decode("utf8"), "xml")
    return RSSChannel.from_xml(url, xml)
