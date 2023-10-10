import requests
import json

# Define the JSON-RPC request template with variables
request_template = {
    "jsonrpc": "2.0",
    "method": "runCmds",
    "params": {
        "version": 1,
        "cmds": [],
        "format": "json"
    },
    "id": 1
}

# Device-specific information
with open('devices.json', 'r') as devices:
    devices = json.load(devices)
print(devices)


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
