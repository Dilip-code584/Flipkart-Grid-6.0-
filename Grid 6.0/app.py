from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_product_info/<product_id>', methods=['GET'])
def get_product_info(product_id):
    product_info = {
        'product_id': product_id,
        'name': 'Example Product',
        'status': 'Quality Check Passed'
    }
    return jsonify(product_info)

if __name__ == "__main__":
    app.run(debug=True)

