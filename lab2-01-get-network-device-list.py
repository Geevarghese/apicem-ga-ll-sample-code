from apicem_config import * # APIC-EM IP is assigned in apicem_config.py

# Get token - function is in apicem_config.py
ticket = get_X_auth_token()
headers = {"X-Auth-Token": ticket}

# API base url
api = "/api/v1/network-device"
url = "https://"+apicem_ip+api

# The request and response of "GET /network-device" API
resp= requests.get(url,headers=headers,verify = False)

# Get the json-encoded content from response
response_json = resp.json()

# all network-device detail is in "response"
device = response_json["response"]

if device != [] :   # if response is not empty 
    device_list = []
    for item in device:
        device_list.append([item["hostname"],item["managementIpAddress"],item["type"],item["id"]])
else:   # response is not empty, no network-device is discovered.
    print ("No network device found !")
    sys.exit()

# We use tabulate module here to print a nice table format. You should use "pip" tool to install in your local machine
# For the simplicity we just copy the source code in working directory didn't install it
print (tabulate(device_list, headers=['hostname','ip','type','id'],tablefmt="rst"))
