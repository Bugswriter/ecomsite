from . import app
from flask import render_template

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/shop')
def products():
	return render_template("shop.html")

@app.route('/profile')
def profile():
	return render_template("profile.html")

@app.route('/payout')
def payout():
	return render_template("payout.html")

