
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)
app.config ['MONGO_URI'] = 'mongodb://localhost:27017/myDatabase'
mongo = PyMongo(app)


@app.route('/')
def hello():
    return "welcome to live-with-cs"



@app.route('/article/<int:id>', methods=['GET'])
def get_one_artical(id):
    print('data entering', id)
    a_article =  mongo.db.blog.find_one_or_404({'_id': id})
    result = dumps(a_article)
    return result


if __name__ == "__main__":
    app.run(debug=True)


