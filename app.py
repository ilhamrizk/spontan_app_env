from main import *
from flask import Flask, request, jsonify

import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    return "main"

@app.route('/getSimilarProduct', methods=['GET'])
def processGetSimilar():
    data = request.json  # Assuming input is in JSON format
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    # Perform some action based on the input
    pos = data.get('pos')
    print(data)
    wr = data.get('write')
    print(wr)
    
    # Action
    if pos is not None and isinstance(pos, str):
        processed_result = getSimilarProduct(pos)
        print(processed_result)
        try:
            print(wr.upper())
            inserttoData(processed_result)
        except:
            print('nowrite')
        return jsonify({'result': processed_result})
    else:
        return jsonify({'error': 'Invalid input format or field'}), 400

@app.route('/getListSimilar', methods=['GET'])
def processGetList():
    data = request.json  # Assuming input is in JSON format
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    # Perform some action based on the input
    pos = data.get('pos')
    print("PoS: ", pos)

   # Example action: reversing the input string
    if pos is not None and isinstance(pos, str):
        processed_result = getListSimilar(pos)
        print(processed_result)
        return jsonify({'result': processed_result})
    else:
        return jsonify({'error': 'Invalid input format or field'}), 400

@app.route('/insertSimilar', methods=['POST'])
def processInput():
    data = request.json  # Assuming input is in JSON format
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    # Perform some action based on the input
    index = data.get('index')  # Replace 'input_data' with your input field
    print(index)

    # Example action: reversing the input string
    if index is not None and isinstance(index, int):
        insertbyIndex(index)
        return jsonify({'result': 'success'})
    else:
        return jsonify({'error': 'Invalid input format or field'}), 400

if __name__ == '__main__':
    app.run(debug=True)
