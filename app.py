from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def search_data():
	city = request.form.get("search")
	checkin = request.form.get("checkin")
	checkout = request.form.get("checkout")
	print city
	print checkin
	print checkout
	return redirect(url_for("index"))

@app.route("/search")
def expedia_api():
	print "I tried to go to the expedia api"
	return redirect("http://api.ean.com")

if __name__ == "__main__":
	app.run(debug = True)