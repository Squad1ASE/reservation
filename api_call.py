import requests
import json
import os

from requests import Response

#API_GATEWAY_SERVICE = 'http://127.0.0.1:5000/'
#USER_SERVICE = 'http://127.0.0.1:5060/'
#RESTAURANT_SERVICE = 'http://127.0.0.1:5070/'
API_GATEWAY_SERVICE = os.environ['API_GATEWAY_SERVICE']
API_GATEWAY_SERVICE = os.environ['USER_SERVICE']
API_GATEWAY_SERVICE = os.environ['RESTAURANT_SERVICE']

# get a restaurant example
def get_restaurant(restaurant_id):
    reply = object
    try:
        reply = requests.get(RESTAURANT_SERVICE+'restaurants/'+str(restaurant_id), timeout=10) #todo
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        reply = Response()
        reply.status_code = 500
    finally:
        return reply

def put_notification(notification):
    reply = object
    try:
        reply = requests.put(USER_SERVICE+'notification', json=json.dumps(notification), timeout=10)
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        reply = Response()
        reply.status_code = 500
    finally:
        return reply
