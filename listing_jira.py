
import requests
from requests.auth import HTTPBasicAuth
import json
#url to get jira projects
url = "https://navyadubbaka9.atlassian.net/rest/api/3/project"
#token is one created in jira software and use here
API_TOKEN="mytoken"
#email associated with jira account
auth = HTTPBasicAuth("email", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
#get the name of first project in the list
name = output[0]["name"]

print(name)