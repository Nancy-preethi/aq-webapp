# using flask_restful
from flask import Flask, request
from flask_restful import  Api

# creating the flask app
from test1 import get_data

app = Flask(__name__)
# creating an API object
api = Api(app)

STATUS_RUNNING = "Running"
STATUS_SOLVE = "Solve"
STATUS_FINISHED = "Finished"


def parse_request_variable(variable, default):
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and variable in request_json:
        return request_json[variable]
    elif request_args and variable in request_args:
        return request_args[variable]
    return default

@app.route('/Solve', methods=['GET'])
def get_string():
    return STATUS_SOLVE


@app.route('/Status', methods=['GET'])
def get_status():
    return STATUS_FINISHED


@app.route('/View', methods=['GET'])
def get_view():
    model_selected = parse_request_variable('model', 'Swift')
    print(model_selected)
    df = get_data()
    # img_url = df[df.model.eq(model_selected)]['img_url']
    car = df[df.model.eq(model_selected)].to_json()
    print(car)
    return car
    # return img_url.values[0]


# driver function
if __name__ == '__main__':
    app.run(debug=True)
