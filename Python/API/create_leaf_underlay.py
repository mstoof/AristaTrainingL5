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

with open('templates/json_rpc_template.json', 'r') as rpc_template:
    rpc_template = json.load(rpc_template)

for datacenter, site in datacenters.items():
    for name, devices in site.items():
        for device, attributes in devices.items():

            print(f'Currently configuring {device}')
            url = f"https://{device}/command-api"
            if name == 'Spines':
                commands = spine_template.render(Interfaces=attributes['Interfaces'])
            else:
                commands = leaf_template.render(Interfaces=attributes['Interfaces'])
            
            rpc_template["params"]["cmds"] = commands
            
            request_json = json.dumps(rpc_template)
            r = requests.post(url, auth=('arista', 'aristaklgj'), data=commands, verify=False)
    




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
