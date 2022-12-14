import requests
from bs4 import BeautifulSoup


class OmantelPrepaid:
	prices = []
	times = []
	data_allowance = []
	social_media_data = []
	flexi_minutes = []
	categories = []
	url = "https://www.omantel.om/Personal/mobile/hayyak/Hayyak-Plus"
	res = requests.get(url)
	txt = res.text
	soup = BeautifulSoup(txt, features="html.parser")

	def __init__(self):
		self.reset()
		self.get_personal_packages_price()
		self.get_personal_packages_time()
		self.get_personal_packages_data()
		self.get_personal_packages()

	def get_personal_packages(self):
		url = "https://portal.omantel.om/Personal"
		res = requests.get(url)
		txt = res.text

		soup = BeautifulSoup(txt, features="html.parser")
		a_tags = soup.find_all("a" , href=True)

		for a in a_tags:
			if a['href'].startswith("https://www.omantel.om/Personal/mobile"):
				if not len(a.text.strip())  == 0  and not "View Details" in  a.text:
					self.categories.append(a.text.strip())



	def get_personal_packages_price(self):
		prices = []

		h6_tags = self.soup.find_all("h6") 

		for h6 in h6_tags:
			try:
				if h6['class'][0] == 'fw-bold':
					prices.append(h6.text)
			except:
				pass
		self.prices = prices



	def get_personal_packages_time(self):
		big_tags = self.soup.find_all("big")

		#get number of weeks
		num_of_weeks = []
		num = self.soup.find_all("h1")
		for span in num:
			#print(span)
			try:
				#print(span['class'])
				if span['class'][0] == "number":
					if len(span.text) != 0:
						num_of_weeks.append(span.text+' Weeks')
					else:
						num_of_weeks.append('Weekly')

			except:
				pass

		self.times = num_of_weeks



	def get_personal_packages_data(self):
		h6_tags = self.soup.find_all("h6")

		for i, h6 in enumerate(h6_tags):
			package_column = h6_tags[i].parent.parent.parent
			column_detiles = package_column.find_all("p")
			temp_list = []

			for p in column_detiles:
				try:
					if p['class'][0] == 'Body-1':
						temp_list.append(p.text)
				except:
					pass
			try:
				if not len(temp_list) == 0 :
					self.data_allowance.append(temp_list[0])
					self.social_media_data.append(temp_list[1])
					self.flexi_minutes.append(temp_list[2])
			except:
				pass
		

					
	def display(self):
		for i , price in enumerate(self.prices):
			print (price + ' - ' + self.times[i] + ' - ' + self.data_allowance[i] + ' - ' + self.social_media_data[i]  + ' - ' + self.flexi_minutes[i] )	


	def reset(self):
		self.prices = []
		self.times = []
		self.data_allowance = []
		self.social_media_data = []
		self.flexi_minutes = []
		self.categories = []