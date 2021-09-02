headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"}
r = requests.get(url,headers=headers)
string = "빙공의 대가 무림영웅전설 1-5"
print(string[:string.find("1")])