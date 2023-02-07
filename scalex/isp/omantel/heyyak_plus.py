import requests
from bs4 import BeautifulSoup


class OmantelHeyyakPlus:
    packages = []
    url = "https://www.omantel.om/Personal/mobile/hayyak/Hayyak-Plus"
    res = requests.get(url)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser")

    def __init__(self):
        self.reset()
        self.get_packages()

    # This function will webscrap all the packages from the URL one by one.
    # Each package will be represented as a dictonary then adding them all the main list "self.packages".

    def get_packages(self):
        package_divs = self.soup.select(
            "div._box._background-white.pink")
        for package_div in package_divs:
            package = {
                "price": "",
                "data_allowance": "",
                "social_media_data": "",
                "flexi_minutes": "",
                "duration": "",
                "duration_title": "",
            }
            # WebScrap Price
            price_tag = package_div.select_one("h6.fw-bold")
            package["price"] = price_tag.text

            # WebScrap "Data Allowance"
            data_allowance_tag = package_div.select("p.Body-3")
            for tag in data_allowance_tag:
                if "Data Allowance" in tag.text:  # Althoug this condiation is in a loop, it suppose to be valid on time only
                    allownace_tag = tag.parent.select_one("p.Body-1.fw-bold")
                    package["data_allowance"] = allownace_tag.text

            # WebScrap "Social Media Data"
            social_media_data_tag = package_div.select("p.Body-3")
            for tag in social_media_data_tag:
                if "Social Media Data" in tag.text:  # Althoug this condiation is in a loop, it suppose to be valid on time only
                    social_media_data_tag = tag.parent.select_one(
                        "p.Body-1.fw-bold")
                    package["social_media_data"] = social_media_data_tag.text

            # WebScrap "Flexi Minutes"
            flexi_minutes_tag = package_div.select("p.Body-3")
            for tag in flexi_minutes_tag:
                if "Flexi Minutes" in tag.text:  # Althoug this condiation is in a loop, it suppose to be valid on time only
                    flexi_minutes_tag = tag.parent.select_one(
                        "p.Body-1.fw-bold")
                    package["flexi_minutes"] = flexi_minutes_tag.text

            # WebScrap "Duration"
            duration_tag = package_div.select_one("h1.number")
            duration_title_tag = package_div.select_one(
                "sup.display-inline-block")
            package["duration_title"] = duration_title_tag.text.replace(
                '/', '')
            package["duration"] = duration_tag.text
            self.packages.append(package)
        print(self.packages)

    def reset(self):
        self.packages = []
