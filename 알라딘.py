from flask import Flask, render_template, request, redirect, send_file
from aladinscrap import scraping

db = {}


app = Flask(__name__)

@app.route("/")
def home():
	wow_db = db
	if wow_db:
		wow = wow_db["알라딘"]
	else:
		db["알라딘"] = scraping()
		wow=db["알라딘"]
	result = sorted(wow, key=lambda potato: potato['price'], reverse=False)	
	return render_template("main.html",wow=result)

app.run(host="0.0.0.0", port="8000", debug=True)
if __name__ == "__main__":
    app.run()