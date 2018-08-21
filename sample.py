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
      print(name1)
      keys = list(result.keys())
      val = dict()
      val['Name'] = name1
      # if name1=="" and power1=="" and level1=="":
      #       val = "Name and power and level not entered"
      # # val = mongo.db.heroes.find({"name":name1})
      # elif name1=="" and power1=="":
      #       val = "name and power entered"
      # elif name1=="" and level1=="":
      #       val = "name and level entered"
      # elif level1=="" and power1=="":
      #       val = "level and power entered"
      return render_template("dummy.html",result = val)
if __name__ == '__main__':
   app.run(debug = True)
