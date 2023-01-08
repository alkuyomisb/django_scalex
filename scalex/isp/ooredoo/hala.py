import requests
from bs4 import BeautifulSoup


class OoredooHala:
    hala_titles=[]
    hala_data=[]
    hala_local_mins=[]
    hala_valid_for=[]
    hala_bonus_data=[]
    hala_cross_mins=[]
    url = "https://www.ooredoo.om/Personal/Mobile/NewShababiah/tabid/5370/Agg11142_SelectTab/1/Default.aspx"
    res = requests.get(url,verify=False)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser") 


    def __init__(self):
        self.get_hala_SIM()
        # self.get_hala_titiles()
        # self.get_hala()




      
    def get_hala_SIM(self):
        div_tags = self.soup.find_all("div") 
        blocks=[]

        
        
        

        for div in div_tags:
            try:
                if div['class'][0]=="item": 
                    hala_SIM={}
                    foundValues = {"data": False , "localMints":False, "title":True ,"IntlMins" : False,"bonusData":False, "ValidFor":False,"OpenCredit":False,"CrossMins":False}

                    # find title then put it in dictionary 
                    h2_tags = div.find_all("h2")
                    hala_SIM["title"] = h2_tags[0].text

                    # find  table1 data from span tag 
                    span_tags = div.find_all("span")
                    for span in span_tags:
                        if span['class'][0] == "ly-title":
                            span_parent = span.parent
                            sub_spans = span_parent.find_all("span") 
                            for sub_span in sub_spans :
                                if sub_span['class'][0] == "ly-subtitle":
                                    # get Data or local data 
                                    if sub_span.text =="Data"  or sub_span.text =="Local Data":
                                        foundValues["data"] = True
                                        hala_SIM["data"]=span.text
                                    # get local mints 
                                    if sub_span.text =="Local Mins":
                                        foundValues["localMints"] = True
                                        hala_SIM["Local Mins"]=span.text
                                    # get Int’l. Mins
                                    if sub_span.text =="Int’l.   Mins":
                                        foundValues["IntlMins"] = True
                                        hala_SIM["Int’l.Mins"]=span.text
                                    
                                if  "%" in sub_span.text:
                                    foundValues["bonusData"] = True
                                    hala_SIM["bonus data"] = span.text
                                if  sub_span.text.startswith("Valid"):
                                    foundValues["ValidFor"]= True
                                    hala_SIM["valid for"]=span.text
                                if sub_span.text == "Open Credit":
                                    foundValues["OpenCredit"]=True
                                    hala_SIM["Open credit"]=span.text
                                if "Cross Mins" in sub_span.text:
                                    foundValues["CrossMins"]=True
                                    hala_SIM["Cross mins"] = span.text

                    if not foundValues["data"]:
                        hala_SIM["data"] = "-"
                    if not foundValues["localMints"]:
                        hala_SIM["Local Mins"] = "-"
                    if not foundValues["IntlMins"]:
                        hala_SIM["Int’l.Mins"]="-"
                    if not foundValues["bonusData"]:
                        hala_SIM["bonus data"] = "-"
                    if not foundValues["ValidFor"]:
                        hala_SIM["valid for"] = "-"
                    if not foundValues["OpenCredit"]:
                        hala_SIM["Open credit"] = "-"
                    if not foundValues["CrossMins"]:
                        hala_SIM["Cross mins"] = "-"
                    print(hala_SIM)

                    blocks.append(hala_SIM)
            except:
                pass

        # print(blocks)




    # def get_hala(self):
    #     span_tags = self.soup.find_all("span") 
        
    #     for span in span_tags:
    #         try:
    #               if span['class'][0] == "ly-title":
    #                 span_parent=span.parent
    #                 sub_spans = span_parent.find_all("span") 
    #                 for sub_span in sub_spans :
    #                     #print(sub_span.text)
    #                     if sub_span['class'][0] == "ly-subtitle":
    #                         if sub_span.text =="Data"  or sub_span.text =="Local Data":
    #                             self.hala_data.append(span.text)
    #                         if sub_span.text =="Local Mins":
    #                             self.hala_local_mins.append(span.text)
    #                     if sub_span.text.startswith("Cross Mins"):
    #                         self.hala_cross_mins.append(span.text)
    #                     if sub_span.text.startswith("Valid for"):
    #                         self.hala_valid_for.append(span.text)
    #                     if "%" in sub_span.text:
    #                         self.hala_bonus_data.append(span.text)
                            

    #         except:
    #             pass
    #         print(self.hala_cross_mins)
        
    

    # def get_hala_titiles(self):
    #     h2_tags = self.soup.find_all("h2") 

    #     for h2 in h2_tags:
    #         try:
    #             if h2['class'][0]=="ly-promotion-head":
    #                 self.hala_titles.append(h2.text)
    #         except:
    #             pass
            
                
          
         


        
