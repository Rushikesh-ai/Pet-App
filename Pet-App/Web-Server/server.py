from flask import Flask
import pymongo as mongo
from urllib.parse import quote_plus
from bson.json_util import dumps

app = Flask(__name__)

def database():
    uri = 'mongodb+srv://%s:%s@petshopapp.hyvlm.mongodb.net/?retryWrites=true&w=majority' % (quote_plus('Administrator'), quote_plus('hemant@2000'))
    myclient = mongo.MongoClient(uri)
    return myclient['PetShopApp']

@app.route('/', methods=['GET'])
def homepage():
    return '<h1>Server GET at /<h1>'

@app.route('/products', methods=['GET'])
def getProducts():
    dbProducts = database()['products']
    products = list(dbProducts.find())

    return dumps(products, indent=4)

@app.route('/products/<string:id>', methods=['GET'])
def getProduct(id):
    dbProducts = database()['products']
    products = dbProducts.find_one({'itemCode': id})

    return dumps(products, indent=4)