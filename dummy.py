from flask import Flask, render_template, request
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/learning"
mongo = PyMongo(app)
@app.route('/')
def search():
      return render_template('search.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      name1 = result.get('Name',None)
      power1 = result.get('Power',None)
      level1 = result.get('Level',None)
      keys = list(result.keys())
      val = dict()
      for i in result.keys():
          temp = result.get(i)
          if(temp!=""):
            val[i] = temp 
          print("Key is {}, Value is {}".format(i,result.get(i)))
    #   result = db.resta.find(val)
      return render_template("dummy.html",result = val)
if __name__ == '__main__':
   app.run(debug = True)
