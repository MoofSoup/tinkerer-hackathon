from flask import Flask, jsonify, request
from check_if_poisoned import hello_world, hello_openai

app = Flask(__name__)

@app.route('/is_poisoned', methods=['POST'])
def is_poisoned():
    data = request.get_json()
    text = data.get('text', '')
    val = hello_openai(text)
    return jsonify({"is_poisoned": val})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
