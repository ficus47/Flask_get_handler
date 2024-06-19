import os
import sys

from flask import Flask, request

from valid_db import valid_db

app = Flask(__name__)

@app.route('/get-example', methods=['GET'])
def get_example():
  # Récupérer les paramètres de la requête GET
  mod = request.args.get('mod')
  content = request.args.get('content')

  if mod == 'valid':
    return valid_db(request)
  
  return f'Param1: {content}, Param2: {mod}'

if __name__ == '__main__':
  app.run(debug=True)
