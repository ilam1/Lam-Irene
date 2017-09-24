'''
Irene Lam
SoftDev1 pd7
K04 -- Fill Up Yer Flask
2017-09-25
'''

from flask import Flask, redirect #url_for
app = Flask (__name__)

@app.route("/")			# first route
def hello_world():		
	return "View: <br>'/words' for the phrase of the day, <br>'/quote' for the quote of the day, <br>  and '/image' for xkcd"

@app.route("/words")		# second route
def words():			
	return "Stack Overflow = Temptation = Agony"

@app.route("/quote")
def quote():
	return "'Computer science is no more about computers than astronomy is about telescopes' <br>- Edsger Dijkstra"

@app.route("/image")		# route?
def image():			
	return redirect("http://www.xkcd.com/399")

if __name__ == "__main__":	
	app.debug = True
	app.run()

