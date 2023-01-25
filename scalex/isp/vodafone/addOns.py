import requests
from bs4 import BeautifulSoup


class vodafoneAddOns:
    add_ons_blocks = []
    url = "https://www.vodafone.om/plans"
    res = requests.get(url)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser")


    def __init__(self):
        self.get_add_ons()

    def get_add_ons(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "carousel" and div['class'][1] == "carousel--plans-addons" and div['class'][2] == "slick-initialized" and div['class'][3] == "slick-slider" and div['class'][4] == "slick-dotted":
                    add_ons_block = {}
                    # print(div)

            except:
                pass
