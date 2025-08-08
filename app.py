from flask import Flask, render_template, request

app = Flask(__name__) # for hosting the website

@app.route('/') # specifies to run this method when the URL contains whatever is in the '',
# in this case it is the homepage, because it runs whenever there is just a / after the URL
def homepage(): # homepage method
    return render_template("index.html")

@app.route('/swelling')
def swelling():
    return render_template("swelling.html")

@app.route('/leakage')
def leakage():
    return render_template("leakage.html")

@app.route('/team') # meet the team
def team():
    return render_template("team.html")

@app.route('/about') # contact, support us, publications, etc.
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)