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
        self.get_our_plans_blocks()


    def get_our_plans_blocks(self):
        divs_tags = self.soup.find_all("div")
        for div in divs_tags:
            try:
                if div['class'][0] == "plan__wrapper":
                    our_plan_block = {}
                    
                    title = div.find_all("div" , {"class": "plan__middle"})[0]
                    titles_fileds = div.find_all("div" , {"class": "plan__title"})
                    sub_titles_fileds = div.find_all("div" , {"class" : "plan__subtitle"})
                    price = div.find_all("span" , {"class" : "plan__price"})[0]
                    gb = div.find_all("span")[0]


                    our_plan_block["GB"] = gb.text
                    our_plan_block["price"] = price.text.replace("\n" , " ").strip()
                    our_plan_block["title"] = title.text

                    for filed in titles_fileds:
                        if 'Local Data' in filed.text:
                            our_plan_block["local_data"] = filed.text
                        if 'Calling' in filed.text:
                            our_plan_block["calling_minutes"] = filed.text
                        if 'Social Pass' in filed.text:
                            our_plan_block["social_pass"] = filed.text
                        if 'Entertainment' in filed.text:
                            our_plan_block["entertainment_pass"] = filed.text
                        if 'Unlimited' in filed.text:
                            our_plan_block["minutes_sms"] = filed.text
                        if 'Take' in filed.text:
                            our_plan_block["home_tariff"] = filed.text
                        if 'International' in filed.text:
                            our_plan_block["international_minutes"] = filed.text
                        if 'weeks' in filed.text:
                            our_plan_block["weeks"] = filed.text
                        if 'VAT' in filed.text:
                            our_plan_block["vat"] = filed.text
                        if 'Great' in filed.text:
                            our_plan_block["add-ons"] = filed.text
                            
                    self.mobile_plans_blocks.append(our_plan_block)

                    print(self.mobile_plans_blocks)
                    
                   
                   
                #     for span in span_tags:
                #         if '35' in span.text:
                #             our_plan_block1["GB"] = span.text
                #         if '16' in span.text and 'OMR' in span.text:
                #             our_plan_block1["price"] = span.text.replace("\n" , " ")
               
               
               
               
               
               
                # if div['class'][0] == "plan__middle":
                #     if "Vodafone" in div.text and "Elite" in div.text:
                #         our_plan_block1["title"] = div.text
                # if div['class'][0] == "plan__title":
                #     if "20" in div.text and "Local Data" in div.text:
                #         our_plan_block1["local_data"] = div.text
                #     # if "10 GB" in div.text and "Social Pass" in div.text:
                #     #     print(div.text)
                #     if "5 GB" in div.text and "Entertainment Pass" in div.text:
                #         our_plan_block1["entertainment_pass"] = div.text
                #     # if "Unlimited" in div.text:
                #     #     print(div.text)
                #     # if "Take your" in div.text:
                #     #     print(div.text)
                #     if "60" in div.text :
                #         our_plan_block1["international_minutes"] = div.text
                #         # print(our_plan_block1)
                #         # print(our_plan_block1)
                #     # if "4 weeks" in div.text:
                #     #     print(div.text)
                #     # if "VAT" in div.text:
                #     #     print(div.text)
                        
                        
                # if div['class'][0] == "plan__subtitle":
                    # if "Surf" in div .text:
                    #     print(div.text)
                    # if "Enjoy" in div.text:
                    #     print(div.text)
                    # if "Stream" in div.text:
                    #     print(div.text)
                    # if "Call and text" in div.text:
                    #     print(div.text)
                    # if "Use your local data," in div.text:
                    #     print(div.text)
                    # if "Keep in touch" in div.text:
                    #     print(div.text)
                    # if "Valid for 4 weeks" in div.text:
                    #     print(div.text)
                    # if "All prices" in div.text:
                    #     print(div.text)
                    


            except:
                pass
   

                
    def reset(self):
        self.prices = []
        self.times = []
        self.data_allowance = []
        self.social_media_data = []
        self.flexi_minutes = []
        self.categories = []