import requests
import json
from pprint import pprint

from utils.auth import IntersightAuth, get_authenticated_aci_session
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'

urlAuth = f"{BASE_URL}/ntp/Policies"

responseAuth = requests.get(urlAuth, auth=auth)

pprint(responseAuth.json(), indent=4)

