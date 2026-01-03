
import requests
from requests.auth import HTTPBasicAuth
import json
#url to create jira issue
url = "https://navyadubbaka9.atlassian.net/rest/api/3/issue"
#token is one created in jira software and use here
API_TOKEN = "yourtoken"
#email associated with jira account
auth = HTTPBasicAuth("email", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}
#declare the payload to create jira issue
payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "FIR"
    },
    "issuetype": {
      "id": "10006"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))