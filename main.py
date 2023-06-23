from flask import Flask, render_template


app = Flask(__name__)

#https://unpkg.com/clippyts@1.0.4/dist/index.js

@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def hello_world():
    return render_template('index.html')


@app.route('/about',methods=["GET"])
def about():
    return render_template('about.html')
