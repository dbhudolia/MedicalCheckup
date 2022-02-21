import sys

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import os
import sklearn.neighbors._dist_metrics

sys.modules['sklearn.neighbors.dist_metrics'] = sklearn.neighbors._dist_metrics

app = Flask(__name__)
# api = Api(app)

filename = 'modelAdaBoost.pkl'
if os.path.getsize(filename) > 0:
    with open(filename, 'rb') as f:
        unpickle = pickle.Unpickler(f)
        model = unpickle.load()


@app.get('/')
def getmethod():
    output = {'depression': 'depressed'}
    return output


"""def post(self):
    # use parser and find the user's query
    parser = reqparse.RequestParser()
    parser.add_argument('sex', required=True)
    parser.add_argument('age', required=True)
    parser.add_argument('year', required=True)
    args = parser.parse_args()
    sex = args['sex']
    age = args['age']
    year = args['year']
    prediction = model.predict(
        [['Yes', 'NaN', 2022, 24, '21-30', 'Male', 1.0, 'Above Average', 'Yes', 1, 'NaN', 0.0, 'Maybe', 'Maybe',
          0, 1.0]])

    prediction = model.predict(
        [['Yes', 'NaN', year, age, '21-30', sex, 1.0, 'Above Average', 'Yes', 1, 'NaN', 0.0, 'Maybe', 'Maybe',
          0, 1.0]])

    if prediction[0] == 0:
        pred_text = 'No Depression'
    else:
        pred_text = 'Depression'

    output = {'depression': pred_text}

    print(output)
    return output"""


@app.get('/depressed/')
def getdmethod():
    output = {'depression': 'depressed'}
    return output


@app.post('/depressed/')
def postmethod():
    # use parser and find the user's query
    parser = reqparse.RequestParser()
    parser.add_argument('sex', required=True)
    parser.add_argument('age', required=True)
    parser.add_argument('year', required=True)
    parser.add_argument('history', required=True)
    parser.add_argument('agegroup', required=True)
    parser.add_argument('anonymity', required=True)
    parser.add_argument('rate', required=True)
    parser.add_argument('negative', required=True)
    parser.add_argument('access', required=True)
    parser.add_argument('diagnosis', required=True)
    parser.add_argument('insurance', required=True)
    parser.add_argument('discuss', required=True)
    parser.add_argument('responsible', required=True)
    parser.add_argument('disorder', required=True)
    parser.add_argument('tech', required=True)
    args = parser.parse_args()
    sex = args['sex']
    age = args['age']
    year = args['year']
    history = args['history']
    agegroup = args['agegroup']
    anonymity = args['anonymity']
    rate = args['rate']
    negative = args['negative']
    access = args['access']
    diagnosis = args['diagnosis']
    insurance = args['insurance']
    discuss = args['discuss']
    responsible = args['responsible']
    disorder = args['disorder']
    tech = args['tech']
    '''prediction = model.predict(
        [['Yes', 'NaN', 2022, 24, '21-30', 'Male', 1.0, 'Above Average', 'Yes', 1, 'NaN', 0.0, 'Maybe', 'Maybe',
          0, 1.0]])'''

    prediction = model.predict(
        [[history, 'NaN', year, age, agegroup, sex, anonymity, rate, negative, access, diagnosis, insurance,
          discuss, responsible, disorder, tech]])

    if prediction[0] == 0:
        pred_text = 'not depressed'
    else:
        pred_text = 'depressed'

    output = {'depression': pred_text}

    print(output)
    return output


# Setup the Api resource routing here
# Route the URL to the resource
# api.add_resource(DepressionPredict, '/depression')

if __name__ == '__main__':
    app.run()
