import pandas

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
  
@app.route('/api/<station>/<date>')
def about(station, date):
    #df=pandas.read_csv()
    #temperature=df.station(date)
    #return render_template('about.html')
    temperature='25'
    return {"station":station,
           "date":date,
           "temperature":temperature}


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=True)

