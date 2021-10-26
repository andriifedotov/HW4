import requests
import json
import os


def app(**kwargs):

    API = {'url': 'https://robot-dreams-de-api.herokuapp.com',
           'endpoint': '/out_of_stock',
           'content-type': 'application/json',
           'directory': './data/'}

    AUTH = {'endpoint': '/auth',
            'payload': {"username": 'rd_dreams', "password": 'djT6LasE'},
            'content-type': 'application/json',
            'Authorization': 'JWT '}

    os.makedirs(os.path.join(API['directory'], kwargs['date']), exist_ok=True)

    url = API['url']
    headers = {"content-type": AUTH['content-type']}
    data = AUTH['payload']
    r = requests.post(url + AUTH['endpoint'], headers=headers, data=json.dumps(data))
    token = r.json()['access_token']

    headers = {"content-type": API['content-type'], "Authorization": AUTH['Authorization'] + token}
    data = {"date": kwargs['date']}
    r = requests.get(url + API['endpoint'], headers=headers, data=json.dumps(data))

    r.raise_for_status()

    with open(os.path.join(API['directory'], kwargs['date'],
                           kwargs['date'] + '.json'), 'w') as json_file:
        data = r.json()
        json.dump(data, json_file)


