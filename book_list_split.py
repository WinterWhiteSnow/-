
def book_list_split(book_list):
	string_list = book_list.split("[중고]")
	list_list = []
	result_list = []
	for i in string_list:
		a = i.replace(" ","")
		list_list.append(a)
	for i in list_list:
		if i != "":
			b = i[:i.find("1")]	
			if "(" in b:
				b = b[:b.find("(")]
			if "[" in b:
				b = b[:b.find("[")]
			if "{" in b:
				b = b[:b.find("{")]
    
			if "(" in b:
				b = b[:b.find("(")]
			if "[" in b:
				b = b[:b.find("[")]
			if "{" in b:
				b = b[:b.find("{")]
    
			if ")" in b:
				b = b[b.find(")")+1:]
			if "]" in b:
				b = b[b.find("]")+1:]
			if "}" in b:
				b = b[b.find("}")+1:]
    
			for d in ".!@#$%^&*()_+|☆★}※{[]":
				b=b.replace(d,"")
			new_str = ""
			for bb in b:
				if 44032<=ord(bb)<=ord("힣"):
					new_str+=bb
			result_list.append(new_str)
	return result_list
