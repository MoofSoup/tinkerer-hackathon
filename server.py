from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/is_poisoned', methods=['POST'])
def is_poisoned():
    return jsonify({"is_poisoned": True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
