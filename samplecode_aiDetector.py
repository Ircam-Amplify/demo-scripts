import argparse
import requests
import time
import json
from pathlib import Path


# ---------------------------------------------
# Add your API credentials HERE
# ---------------------------------------------

# client_id = "<YOUR_CLIENT_ID>"
# client_secret = "<YOUR_CLIENT_SECRET>"

client_id="4b379e31-61cb-489e-b70e-5f0110931b48"
client_secret="TYzHyA-wTVlrPEajRcbtO2ZAT2ef0X0n0JYAozdqSaU"

# ---------------------------------------------
# Parse args to send file
# ---------------------------------------------

parser = argparse.ArgumentParser()

# Module parameters
parser.add_argument('-i', '--input', type=str,
                    help="Input audio data (file or url)",
                    default="")

args = parser.parse_args()
local_file = args.input

print("Sending " + local_file)

# ---------------------------------------------
# Get auth token
# ---------------------------------------------

auth_url = "https://api.ircamamplify.io/oauth/token"

payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "client_credentials"
}

response = requests.post(auth_url, json=payload)
id_token = response.json()["id_token"]

headers = {"authorization": f"Bearer {id_token}"}

headers = {
'Content-Type': 'application/json',
'Accept': 'application/json', 
'Authorization': f'Bearer {id_token}'
}



# ---------------------------------------------
# Create a storage location
# ---------------------------------------------

print("CREATE STORAGE")
manager_url = "https://storage.ircamamplify.io/manager/"

response = requests.post(manager_url, headers=headers)
file_id = response.json().get('id')



# ---------------------------------------------
# Upload an audio file via our Storage API
# ---------------------------------------------

print("LOAD MEDIA")

storage_url = "https://storage.ircamamplify.io"
filename = Path(local_file).name
put_url = f"{storage_url}/{file_id}/{filename}"
response = requests.put(
put_url, data=open(local_file, 'rb'), headers=headers)


# ---------------------------------------------
# Process audio content
# ---------------------------------------------


print("PROCESS")

response = requests.get(manager_url + file_id, headers=headers)
ias_url = response.json().get('ias')

# ---------------------------------------------
# Documentation is available here https://docs.ircamamplify.io/api#tag/AI-Detector
# ---------------------------------------------
module_url = "https://api.ircamamplify.io/aidetector/"

payload = {}
payload['audioUrlList'] = [ias_url]


response = requests.post(module_url, headers=headers, json=payload)

print(response.text)

job_id = response.json()["id"]


process_status = None
while process_status not in ["success", "error"]:
    print("Processing...")
    time.sleep(5)
    response = requests.get(module_url + "/" + job_id, headers=headers)
    job_infos = response.json().get('job_infos')
    process_status = job_infos["job_status"]


# ---------------------------------------------
# Get results from the report field of the answer
# ---------------------------------------------
response = requests.get(module_url + "/" + job_id, headers=headers)

job_infos = response.json().get('job_infos')
report = job_infos['report_info']['report']

print(report)


print("Done!")