# microservice
import os
import time
import random

from flask import Flask, jsonify, request

import definitions
import get_env

app = Flask(__name__)


# fixme : this does not give info about the actual exception
@app.errorhandler(500)
def error_handling(error):
    answer = {}
    answer['error'] = str(error)

    print('light_service() : error : ' + error.__str__())
    response = jsonify(answer, 500)

    return response


# an endpoint that can be polled with little overhead
# @app.route('/status')
# def status():
#     answer = {}
#     app_name = request.args.get('app_name')
#     uuid = request.args.get('uuid')
#
#     answer['status'] = 'OK'
#     answer['uuid'] = uuid.__str__()
#     answer['service_name'] = 'light-service'
#     answer['version'] = get_env.get_version()
#
#     print('status() : uuid=' + uuid + ', app_name=' + app_name.__str__() + ', version=' + answer['version'])
#     response = jsonify(answer)
#
#     return response

@app.route('/')
def status():
    answer = {}

    answer['status'] = 'OK'
    answer['time'] = time.ctime()
    response = jsonify(answer)
    return response

# @app.route('/stats')
# def stats():
#     answer = {}
#     app_name = request.args.get('app_name')
#     uuid = request.args.get('uuid')
#
#     answer['status'] = 'OK'
#     answer['uuid'] = uuid.__str__()
#     # answer['api_calls'] = -1    # not yet implemented
#
#     print('status() : uuid=' + uuid + ', app_name=' + app_name.__str__() + ', api_calls=' + answer['api_calls'])
#     response = jsonify(answer)
#
#     return response


@app.route('/get_lux')
def get_lux_api():
    """

    :param app_name: e.g. name of the calling app so it can be identified in logs
    :return:
    """
    try:
        answer = {}

        lux = 100 * random.randint(1, 100)

        # Create response
        answer['status'] = 'OK'
        answer['lux'] = lux.__str__()

        response = jsonify(answer)
        time.sleep(random.randint(0, 2))

        return response

    except Exception as e:
        answer['function'] = 'get_lux_api'
        answer['error'] = str(e)
        response = jsonify(answer, 500)

        return response


if __name__ == '__main__':
    os.environ['PYTHONUNBUFFERED'] = "1"            # does this help with log buffering ?
    version = get_env.get_version()                 # container version

    print('test-service started, version=' + version)

    app.run(host='0.0.0.0', port=definitions.listen_port.__str__())
