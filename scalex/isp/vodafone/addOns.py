import requests
from bs4 import BeautifulSoup


class vodafoneAddOns:
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
                if div['class'][0] == "slick-list":
                    add_ons_block = {}
                    # print(div)

            except:
                pass
