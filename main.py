from flask import Flask, request
from controller.fetch import *

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello world'

@app.route('/getAllProduct', methods=['GET'])
def fetchAllProduct():
  response = getAllProducts()
  return response


@app.route('/getAllCategory', methods=['GET'])
def fetchAllCategory():
  response = getAllCategories()
  return response

@app.route('/getAllReview', methods=['GET'])
def fetchAllReview():
  response = getAllReviews()
  return response

@app.route('/getAllProductByCategory', methods=['GET'])
def fetchAllProductsByCategory():
  categoryId = request.args.get('category')
  response = getAllProductsByCategory(categoryId)
  return response

@app.route('/getAllReviewByProduct', methods=['GET'])
def fetchAllReviewsByProduct():
  productId = request.args.get('product')
  response = getAllReviewsByProduct(productId)
  return response

@app.route('/getAllReviewByCategory', methods=['GET'])
def fetchAllReviewsByCategory():
  categoryId = request.args.get('category')
  response = getAllReviewsByCategory(categoryId)
  return response

if __name__ == '__main__':
  app.run(debug=True)