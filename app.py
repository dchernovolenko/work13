from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    api = urllib2.urlopen('http://xkcd.com/info.0.json')
    api_dict = json.loads(api.read())
    return render_template('template.html', image=api_dict['img'], title=api_dict["title"], desc=api_dict["alt"], day = api_dict["day"], month = api_dict["month"], year = api_dict["year"])

if __name__ == '__main__':
  app.debug = True
  app.run()
