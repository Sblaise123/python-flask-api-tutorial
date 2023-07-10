from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_test = jsonify(todos)
    return json_test

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    todos.append(request_body)
    return jsonify(todos), 201
    #print("Incoming request with the following body", request_body)
   # return 'Response for the POST todo'

@app.route('/todos/<int:postion', methods=['DELETE'])
def delete_todo():
    print("This is the position to delete",position)
    return 'something' 

@app.route('/todos/<int:postion', methods=['DELETE'])
def delete_todo():
    del todos(position)
    return jsonify(todos), 200

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)