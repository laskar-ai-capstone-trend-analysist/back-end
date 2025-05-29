import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.util import *

from flask import jsonify

def getAllProducts():
  try:
    result = getAllProduct()
    return jsonify({
        'error': False,
        'message': 'Data fetched successfully',
        'data': result
    }), 200
  except Exception as e:
    print('Error fetching the data', e)
    return jsonify({
      'error': True,
      'message': 'Error fetching data',
      'data': None
    }), 500
