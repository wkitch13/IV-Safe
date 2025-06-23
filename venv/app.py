from flask import Flask, render_template, request

app = Flask(__name__) # for hosting the website

@app.route('/') # specifies to run this method when the URL contains whatever is in the '',
# in this case it is the homepage, because it runs whenever there is just a / after the URL
def index(): # homepage method
    return render_template('index.html')