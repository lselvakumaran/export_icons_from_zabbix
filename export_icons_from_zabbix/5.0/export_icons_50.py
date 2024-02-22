import requests
import csv
import configparser
import pybase64

config = configparser.ConfigParser()
config.read('config.ini')

# Set the Zabbix API URL
ZABBIX_API_URL = config['zabbix']['url']

# Set the Zabbix API token
ZABBIX_API_TOKEN = config['zabbix']['token']

# Create a Zabbix API session
zabbix_api_session = requests.Session()

# Get all hosts from the Zabbix API
zabbix_api_request = {
           "jsonrpc": "2.0",
           "method": "image.get",
           "params": {
               "output": "extend",
               "select_image": "true"
           },
           "auth": ZABBIX_API_TOKEN,
           "id": 1
       }
zabbix_api_response = zabbix_api_session.post(ZABBIX_API_URL, json=zabbix_api_request)

# Check the Zabbix API response status code
if zabbix_api_response.status_code != 200:
    raise Exception("Failed to get all hosts from the Zabbix API: {}".format(zabbix_api_response.content))

# Get the host data from the Zabbix API response
zabbix_host_data = zabbix_api_response.json()["result"]

for zabbix_host in zabbix_host_data:
        decoded_data=pybase64.b64decode((zabbix_host["image"]))
        imagefile=zabbix_host["name"]+'.jpeg'
        #write the decoded data back to original format in  file
        img_file = open(imagefile, 'wb')
        img_file.write(decoded_data)
        img_file.close()
