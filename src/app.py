# Y.R.P - Primera aplicación Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Y.R.P - Lista global de tareas

todos = [
    {
        "label": "My first task",
        "done": False
    }
]

# Y.R.P - Endpoint GET /todos

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

# Y.R.P - Endpoint POST /todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    print("Incoming request with the following body", request_body)

    todos.append(request_body)

    return jsonify(todos)

# Y.R.P - Endpoint DELETE /todos/<position>

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):

    todos.pop(position)

    return jsonify(todos)

# Y.R.P - Arranque del servidor Flask

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)