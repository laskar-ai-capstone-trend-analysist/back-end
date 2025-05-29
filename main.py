from flask import Flask
from controller.fetch import *

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello world'

@app.route('/getAllProduct')
def fetchAllProduct():
  response = getAllProducts()
  return response

if __name__ == '__main__':
  app.run(debug=True)