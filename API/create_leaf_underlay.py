import requests
import pyeapi
import json
from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader("templates/"))
spine_template = environment.get_template("spines_template.j2")
leaf_template = environment.get_template("leafs_template.j2")
# Device-specific information
with open('devices.json', 'r') as DC:
    datacenters = json.load(DC)



for datacenter, site in datacenters.items():
    for device in site['Spines']:
        print(f'Currently configuring {device}')
        node = pyeapi.connect_to(device)

        result = node.config([spine_template])
        print(result)



# Replace variables in the request template
# request = request_template.copy()
# request["params"]["cmds"] = device_info["commands"]

# # Convert the request to JSON
# request_json = json.dumps(request)

# # Send the JSON-RPC request to the device
# url = "http://switch1/command-api"
# headers = {"Content-Type": "application/json"}
# response = requests.post(url, data=request_json, headers=headers)

# # Process the JSON-RPC response
# response_json = response.json()
# ... Process the response data as needed
