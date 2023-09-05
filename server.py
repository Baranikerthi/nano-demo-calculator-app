'''
import required 
'''
from flask import Flask,request,jsonify


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])

def greeting():
    '''function to add'''
    return jsonify("Hello world"),200

@app.route("/calculator/add", methods=['POST'])
def add():

    data =request.get_json()
    if "first" in data and "second" in data:
        f = data["first"]
        s = data["second"]
        result={"result":f+s}
        

        return jsonify(result),200

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data =request.get_json()
    if "first" in data and "second" in data:
        f = data["first"]
        s = data["second"]
        result={"result":f-s}
        return jsonify(result),200

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
