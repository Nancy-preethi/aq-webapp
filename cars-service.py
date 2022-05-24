# using flask_restful
from flask import Flask, request
from flask_restful import  Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

STATUS_RUNNING = "Running"
STATUS_SOLVE = "Solve"
STATUS_FINISHED = "Finished"


@app.route('/Solve', methods=['GET'])
def get_string():
    return STATUS_SOLVE


@app.route('/Status', methods=['GET'])
def get_status():
    return STATUS_FINISHED


@app.route('/View', methods=['GET'])
def get_view():
    return "PROGRAM RUN SUCCESSFULLY"


# driver function
if __name__ == '__main__':
    app.run(debug=True)
