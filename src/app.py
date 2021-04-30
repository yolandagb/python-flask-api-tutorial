from flask import Flask, jsonify
app = Flask(__name__)
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]
@app.route('/todos', methods=['GET'])
def hello_world():
    # puedes convertir esa variable en un string json así
    json_result = jsonify(todos)
    # y luego puedes retorarla (return) en el response body así:
    return json_result

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
     print("Incoming request with the following body", request_body)
    return 'Response for the POST todo' 

















# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)