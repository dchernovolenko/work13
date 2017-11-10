from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route("/")
def root():
    api = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=eqrkm70XPoAxvxbcrHZnC37LAB5dXa5odR9cdWYd')
    api_dict = json.loads(api.read())
    return render_template('template.html', image=api_dict['url'], title=api_dict["title"], desc=api_dict["explanation"])

if __name__ == '__main__':
  app.debug = True
  app.run()
