# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import banana_dev as banana
# import requests
import json
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.environ.get('banana_api_key')
model_key = os.environ.get('banana_model_key')

model_inputs = {"prompt": [
    "My name is Neerthigan",
    "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
    "The person box was packed with jelly many dozens of months later",
    "Standing on one's head at job interviews forms a lasting impression.",
    "Neerthigan is is 10 years old",
    "My name is also Nickel",
    "My name is Neerthigan"
    ]}

# res = requests.post('http://localhost:8000/', json = model_inputs)

# Disabled to avoid accidental server usage

# res = banana.run(api_key, model_key, model_inputs)
# pretty = json.dumps(res, indent=4)
# print(pretty)
