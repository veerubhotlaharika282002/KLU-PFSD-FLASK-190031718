from flask import Flask,render_template

app=Flask(__name__)
#static data to be passed 
gifts = [
{'name':'cards','type':'hardcopy','quantity':10,'price':1000},
{'name':'idle','type':'glass','quantity':2,'price':5000},
{'name':'bouquet','type':'flower','quantity':20,'price':3000}
]
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',title="GS=Home")

@app.route("/register")
def register():
	return render_template('register.html',title="Join Now")

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/view")
def view():
	#flask requires the data to be sent in the form of dictionary only...
	return render_template('view.html',gifts=gifts)

@app.route("/Contactus")
def ContactUs():
	return render_template('Contactus.html')