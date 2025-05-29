from .setup import *

def getAllProduct():
  try:
    dbCursor.execute('SELECT * FROM product')
    result = dbCursor.fetchall()
    return result
  except Exception as e:
    print('Error fetching the data', e)
    return None

def getAllCategory():
  try:
    dbCursor.execute('SELECT * FROM category')
    result = dbCursor.fetchall()
    return result
  except Exception as e:
    print('Error fetching the data', e)
    return None

def getAllReview():
  try:
    dbCursor.execute('SELECT * FROM product')
    result = dbCursor.fetchall()
    return result
  except Exception as e:
    print('Error fetching the data', e)
    return None