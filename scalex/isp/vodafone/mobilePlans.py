import requests
from bs4 import BeautifulSoup


class vodafonePlans:
    mobile_plans_blocks = []
    url = "https://www.vodafone.om/plans"
    res = requests.get(url)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser")

    def __init__(self):
        self.reset()
        self.get_our_plans_block1()
        self.get_our_plans_block2()
        self.get_our_plans_block3()
        self.get_our_plans_block4()
        self.get_our_plans_block5()

    def get_our_plans_block1(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    span_tags = div.find_all("span")
                    our_plan_block1 = {}
                    for span in span_tags:
                        if '35' in span.text:
                            our_plan_block1["GB"] = span.text
                        if '16' in span.text and 'OMR' in span.text:
                            our_plan_block1["price"] = span.text.replace("\n" , " ")
                if div['class'][0] == "plan__middle":
                    if "Vodafone" in div.text and "Elite" in div.text:
                        our_plan_block1["title"] = div.text
                if div['class'][0] == "plan__title":
                    if "20" in div.text and "Local Data" in div.text:
                        our_plan_block1["local_data"] = div.text
                    if "5 GB" in div.text and "Entertainment Pass" in div.text:
                        our_plan_block1["entertainment_pass"] = div.text
                    if "60" in div.text :
                        our_plan_block1["international_minutes"] = div.text
            except:
                pass
    
    def get_our_plans_block2(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    span_tags = div.find_all("span")
                    our_plan_block2 = {}
                    for span in span_tags:
                        if "80" in span.text:
                            our_plan_block2["GB"] = span.text
                        if "24" in span.text and "OMR" in span.text:
                            our_plan_block2["price"] = span.text.strip().replace("\n" , " ")
                if div['class'][0] == "plan__middle":
                    if "RED Pioneer" in div.text:
                        our_plan_block2["title"] = div.text
                if div['class'][0] == "plan__title":
                    if "40 GB" in div.text:
                        our_plan_block2["local_data"] = div.text
                    if "20 GB" in div.text and "Social Pass" in div.text:
                        our_plan_block2["social_pass"] = div.text
                    if "20 GB" in div.text and "Entertainment Pass" in div.text:
                        our_plan_block2["entertainment_pass"] = div.text
                    if "200" in div.text:
                        our_plan_block2["international_minutes"] = div.text
            except:
                pass

    def get_our_plans_block3(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    span_tags = div.find_all("span")
                    our_plan_block3 = {}
                if div['class'][0] == "plan__data":
                    for span in span_tags:
                        if "25" in span.text:
                            our_plan_block3["GB"] = span.text
                        if "12" in span.text and "OMR" in span.text:
                            our_plan_block3["price"] = span.text.strip().replace("\n" , " ")
                if div['class'][0] == "plan__middle":
                    if "RED Explore" in div.text:
                        our_plan_block3["title"] = div.text
                if div['class'][0] == "plan__title":
                    if "15 GB" in div.text:
                        our_plan_block3["local_data"] = div.text
                    if "10 GB Social Pass" in div.text:
                        our_plan_block3["social_pass"] = div.text
                    if "500" in div.text:
                        our_plan_block3["calling_minutes"] = div.text
                        # print(our_plan_block3)
            except:
                pass

    def get_our_plans_block4(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    span_tags = div.find_all("span")
                    our_plan_block4 = {}
                if div['class'][0] == "plan__data":
                    for span in span_tags:
                        if span.text.startswith(('5GB')):
                            our_plan_block4["GB"] = span.text
                if div['class'][0] == "plan__middle":
                    if "RED Advance" in div.text:
                        our_plan_block4["title"] = div.text
                if div['class'][0] == "plan__title":
                    if div.text.startswith('5') and "Local Data" in div.text:
                        our_plan_block4["Local_data"] = div.text
                    if "150" in div.text and "Calling Minutes" in div.text:
                        our_plan_block4["calling_minutes"] = div.text
            except:
                pass

    def get_our_plans_block5(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    span_tags = div.find_all("span")
                    our_plan_block5 = {}
                if div['class'][0] == "plan__data":
                    for span in span_tags:
                        if "2GB" in span.text:
                            our_plan_block5["GB"] = span.text
                        # if "2" in span.text and "OMR" in span.text:
                        #     print(span.text)
                if div['class'][0] == "plan__middle":
                    if "Start" in div.text:
                        our_plan_block5["title"] = div.text
                if div['class'][0] == "plan__title":
                    if "2 GB" in div.text:
                        our_plan_block5["local_data"] = div.text
                    if "20" in div.text and "Calling Minutes" in div.text:
                        our_plan_block5["calling_minutes"] = div.text
                    if "7 Days" in div.text:
                        our_plan_block5["days"] = div.text
                if div['class'][0] == "plan__subtitle":
                    if "Valid for 7 days" in div.text:
                        our_plan_block5["days_sub_title"] = div.text
            except:
                pass


                
    def reset(self):
        self.prices = []
        self.times = []
        self.data_allowance = []
        self.social_media_data = []
        self.flexi_minutes = []
        self.categories = []