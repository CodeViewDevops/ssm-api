import os
import boto3
import flask
import json
from flask_lambda import FlaskLambda
from flask import request

app = FlaskLambda(__name__)

app.config["DEBUG"] = True

region = os.environ['AWS_REGION']
access_key_id = os.environ['AWS_ACCESS_KEY']
secret_access_key = os.environ['AWS_SECRET_KEY']
#os.environ['DEFAULT_REGION'] = "us-west-2"

session = boto3.Session(
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key
    #aws_session_token=SESSION_TOKEN
)

# Function for get_parameters
def get_parameters(param_key):
    ssm = boto3.client('ssm', region_name=region)
    response = ssm.get_parameters(
        Names=[
            param_key,
        ],
        WithDecryption=True
    )
    return response['Parameters'][0]['Value']

@app.route('/', methods=['GET', 'POST'])
def env():
    #app = request.args.get('appname') 
     # parameter name
    param_key = request.args.get('appname') 
    # get parameter value
    param_value = get_parameters(param_key)
    return param_value

@app.route('/healthz', methods=['GET', 'POST'])
def starting_url():
	status_code = flask.Response(status=200)
	return status_code

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)

