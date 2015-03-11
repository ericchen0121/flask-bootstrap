from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/spotmytrend')
def images():
  return render_template('spotmytrend.html')

@app.route('/trend-result')
def result():
  return render_template('trend-result.html')

if __name__ == "__main__":
    app.run()
