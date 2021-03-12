import requests
import json
from pprint import pprint

from utils.auth import IntersightAuth, get_authenticated_aci_session
from env import config

auth=IntersightAuth(secret_key_filename=config['INTERSIGHT_CERT'],
                      api_key_id=config['INTERSIGHT_API_KEY'])

BASE_URL='https://www.intersight.com/api/v1'

urlAlarm = f"{BASE_URL}/cond/Alarms"

responseAlarm = requests.get(urlAlarm, auth=auth)

for item in responseAlarm.json()['Results']:
    if 'Description' in item:
        print(item['Description'])


# pprint(responseAlarm.json())



urlSummary = f"{BASE_URL}/compute/PhysicalSummaries"

responseSummary = requests.get(urlSummary, auth=auth)
counter = 1
print("-------------")

for item in responseSummary.json()['Results']:
    print("Summary", counter)
    counter = counter + 1
    if 'ManagementMode' in item:
        print("Management Mode: ", item['ManagementMode'])
    if 'MgmtIpAddress' in item:
        print("Management IP: ", item['MgmtIpAddress'])
    if 'Name' in item:
        print("Name: ", item['Name'])
    if 'CpuCapacity' in item:
        print("CPU Capacity: ", item['CpuCapacity'])
    if 'NumCpuCores' in item:
        print("Number of cores: ", item['NumCpuCores'])
    if 'OperPowerState' in item:
        print("Power State: ", item['OperPowerState'])
    if 'Firmware' in item:
        print("Firmware: ", item['Firmware'])
    if 'Model' in item:
        print("Model: ", item['Model'])
    if 'Serial' in item:
        print("Serial: ", item['Serial'])
    if 'Tags' in item:
        for element in item['Tags']:
            if element['Key'] == "Intersight.LicenseTier":
                print('Lisence Tier: ', element['Value'])
    print("-------------")

# pprint(responseSummary.json())


urlHCL = f"{BASE_URL}/cond/HclStatuses"

responseHCL = requests.get(urlHCL, auth=auth)

counter = 1
print("-------------")

for item in responseHCL.json()['Results']:
    print("HCL", counter)
    counter = counter + 1
    if 'InvOsVendor' in item:
        print("OS Vendor: ", item['InvOsVendor'])
    if 'InvOsVersion' in item:
        print("OS Version: ", item['InvOsVersion'])
    print("-------------")
    
# Kubernetes clusters 
urlKub = f"{BASE_URL}/kubernetes/Clusters"

responseKub = requests.get(urlKub, auth=auth)

counter = 1
print("-------------")

for item in responseKub.json()['Results']:
    print("Cluster", counter)
    counter = counter + 1
    if 'Name' in item:
        print("Name: ", item['Name'])
    print("-------------")
    
    
# Kubertetes deployments
urlKubDep = f"{BASE_URL}/kubernetes/Deployments"

responseKubDep = requests.get(urlKubDep, auth=auth)

counter = 0
print("-------------")

for item in responseKubDep.json()['Results']:
    counter = counter + 1

    
print("Number of deployments: ", counter)
