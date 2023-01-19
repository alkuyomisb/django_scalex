import requests
from bs4 import BeautifulSoup


class vodafonePlans:
    mobile_plans_blocks = []
    url = "https://www.vodafone.om/plans"
    res = requests.get(url)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser")

    def __init__(self):
        self.get_our_plans_blocks()


    def get_our_plans_blocks(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    our_plan_block = {}
                    
                    title = div.find_all("div" , {"class": "plan__middle"})[0]
                    titles_fileds = div.find_all("div" , {"class": "plan__title"})
                    price = div.find_all("span" , {"class" : "plan__price"})[0]
                    gb = div.find_all("span")[0]


                    our_plan_block["GB"] = gb.text
                    our_plan_block["price"] = price.text.replace("\n" , " ").strip()
                    our_plan_block["title"] = title.text

                    for filed in titles_fileds:
                        parent_filed = filed.parent 
                        sub_parent = parent_filed.find_all("div")
                        for sub_filed in sub_parent:
                            if sub_filed['class'][0] == "plan__subtitle":
                                if "Surf, chat," in sub_filed.text:
                                    # plan_title
                                     our_plan_block["local_data"] = filed.text
                                     # sub_title
                                     our_plan_block["local_data_sub_title"] = sub_filed.text
                                if "Enjoy more" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["social_pass"] = filed.text
                                    # sub_title
                                    our_plan_block["social_pass_sub_title"] = sub_filed.text
                                if "Call your friends" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["calling_minutes"] = filed.text
                                    # sub_title
                                    our_plan_block["calling_minutes_sub_title"] = sub_filed.text
                                if "Choose the add-on" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["add-ons"] = filed.text
                                    # sub_title
                                    our_plan_block["add-ons_sub_title"] = sub_filed.text
                                if "Stream more" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["entertainment_pass"] = filed.text
                                    # sub_title
                                    our_plan_block["entertainment_pass_sub_title"] = sub_filed.text
                                if "Call and text" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["minutes_sms"] = filed.text
                                    # sub_title
                                    our_plan_block["minutes_sms_sub_title"] = sub_filed.text
                                if "Use your local data," in sub_filed.text:
                                    # plan_title
                                    our_plan_block["home_tariff"] = filed.text
                                    # sub_title
                                    our_plan_block["home_tariff_sub_title"] = sub_filed.text
                                if "Keep in touch" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["international_minutes"] = filed.text
                                    # sub_title
                                    our_plan_block["international_minutes_sub_title"] = sub_filed.text
                                if "All prices" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["vat"] = filed.text
                                    # sub_title
                                    our_plan_block["vat_sub_title"] = sub_filed.text
                                if "Valid for" in sub_filed.text:
                                    # plan_title
                                    our_plan_block["valid"] = filed.text
                                    # sub_title
                                    our_plan_block["valid_sub_title"] = sub_filed.text
                                
                    self.mobile_plans_blocks.append(our_plan_block)
                    print(self.mobile_plans_blocks)
            except:
                pass