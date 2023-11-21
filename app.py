from main import getSimilarProduct
from flask import Flask, request, jsonify

import pandas as pd

app = Flask(__name__)

@app.route('/')
def main():
    # random generate from PoS
    df_pos = pd.read_excel('Product Name from PoS Transactions.xlsx')\
        .sample()\
        .reset_index()
    pos = df_pos.head()['Product Name'][0]
    print(pos)

    out = getSimilarProduct(pos)
    return out

@app.route('/getSimilarProduct', methods=['GET'])
def process_input():
    data = request.json  # Assuming input is in JSON format
    if data is None:
        return jsonify({'error': 'No data provided'}), 400
    
    # Perform some action based on the input
    pos = data.get('pos')  # Replace 'input_data' with your input field
    print(pos)

    # Example action: reversing the input string
    if pos is not None and isinstance(pos, str):
        processed_result = getSimilarProduct(pos)
        return jsonify({'result': processed_result})
    else:
        return jsonify({'error': 'Invalid input format or field'}), 400

if __name__ == '__main__':
    app.run(debug=True)
