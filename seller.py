import requests
from bs4 import BeautifulSoup

def seller_check(urls):
	seller_list = []
	for i in urls:
		# print("판매자체크", i)
		url = i["link"]
		# print(url)
		headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
		r = requests.get(url,headers=headers)
		# print("리퀘스트",r)
		soup = BeautifulSoup(r.text,"html.parser")
		# print("수프",soup)
		parent_tag = soup.find("div",{"class":"Ere_prod_bookwrap"}).find("div",{"class":"Ere_prod_Binfowrap"})
		child_tag = parent_tag.find("div",{"class":"info"}).find("div",{"style":"margin-top:-25px;"})
		seller = child_tag.find("div",{"class":"Ritem"}).find("a").string
		seller = seller.replace(" ","")
		if seller == "tkdjqdlsdlek":
			continue
		if seller == "도쿠가와":
			continue
		if seller == "만화뱅크":
			continue
		if seller == "북코리아":
			continue
		if seller == "책창고":
			continue
		if seller == "☆북앤스토리☆":
			continue
		if seller == "호계동책방":
			continue
		seller_list.append(i)	
	return seller_list
