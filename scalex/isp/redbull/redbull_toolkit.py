import requests
from bs4 import BeautifulSoup
from scalex.scalex_toolkit import ScaleXToolkit


class RedbullToolkit(ScaleXToolkit):
    MOBILE_PLANS_URL = "http://www.rennamobile.com/data-bundles/"

    def get_soup(self, URL):
        res = requests.get(URL)
        txt = res.text
        soup = BeautifulSoup(txt, features="html.parser")
        return soup
