import requests
from bs4 import BeautifulSoup

def seller_check(urls):
	seller_list = []
	urls = urls
	for i in urls:
		url = i["link"]
		headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
		r = requests.get(url,headers=headers)
		soup = BeautifulSoup(r.text,"html.parser")
		parent_tag = soup.find("div",{"class":"Ere_prod_bookwrap"}).find("div",{"class":"Ere_prod_Binfowrap"})
		child_tag = parent_tag.find("div",{"class":"info"}).find("div",{"style":"margin-top:-25px;"})
		seller = child_tag.find("div",{"class":"Ritem"}).find("a").string
		if seller == "tkdjqdlsdlek":
			pass
		elif seller == "도쿠가와":
			pass
		elif seller == "만화뱅크":
			pass
		elif seller == "북코리아":
			pass
		elif seller == "책창고":
			pass
		elif seller == "☆북앤스토리☆":
			pass
		else:
			seller_list.append(i)
	print(seller_list)		
		
	return seller_list
