from flask import Flask, render_template, request, redirect, send_file
from aladinscrap import scraping

db = {}


app = Flask(__name__)

@app.route("/")
def home():
	from_db = db
	if from_db:
		wow = from_db
	else:
		from_db = scraping()
		db["알라딘"]=from_db
		wow = from_db
	result = sorted(wow, key=lambda potato: potato['price'], reverse=False)	
	return render_template("main.html",wow=result)

app.run(host="0.0.0.0", port="8000", debug=True)
# if __name__ == "__main__":
#     app.run()