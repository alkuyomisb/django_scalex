import requests
from bs4 import BeautifulSoup



class vodafoneMoreServices:
    sms_to_tv = []
    sms_to_radio = []
    url = "https://www.vodafone.om/more-services"
    res = requests.get(url)
    txt = res.text
    soup = BeautifulSoup(txt, features="html.parser")

    def __init__(self):
        self.get_sms_to_media()
    

    def get_sms_to_media(self):
        try:
            tv_channels_table = self.soup.find_all('table', class_='tg')

            for row in tv_channels_table:
                if "TV" in row.text or "Tv" in row.text or "Media" in row.text:
                    tv_channels_column = [row.text for row in row.select('td:nth-of-type(1)')]
                    tv_short_code_column = [row.text for row in row.select('td:nth-of-type(2)')]
                    tv_service_column = [row.text for row in row.select('td:nth-of-type(3)')]
                    tv_tariff_column =[row.text for row in row.select('td:nth-of-type(4)')]
                if "Radio" in row.text or "FM" in row.text:
                    radio_channels_column = [row.text for row in row.select('td:nth-of-type(1)')]
                    radio_short_code_column = [row.text for row in row.select('td:nth-of-type(2)')]
                    radio_service_column = [row.text for row in row.select('td:nth-of-type(3)')]
                    radio_tariff_column =[row.text for row in row.select('td:nth-of-type(4)')]
                    # print(radio_short_code_column)
        except:
            pass