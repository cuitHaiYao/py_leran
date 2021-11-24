import requests
import json

url = "http://47.108.75.78/server/control/device/slag_car/"

payload = json.dumps({
  "project_id": "5bfefaaf-6cb6-4bee-a3a9-e7863e8920d1",
  "code": "TESTCAR-02",
  "name": "运渣车",
  "rgsn": "1",
  "model": "2",
  "dev_position": "3"
})
headers = {
  'AUTHENTICATION': 'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiI4NjNkZTk5NS03ZjdlLTQxZDItODViYi0yOGY2M2M3ODBkYzMiLCJyZXNvdXJjZWlkIjoiYTlkNWRkNWEtM2UzYi00NzdkLWI3OTAtMjkzMDIzMDZkNGU3IiwidHlwZSI6MSwiZXhwIjoxOTQwNDY5OTY5fQ.7eR_mjFj6rYhKnUyCiBGlosvwG0qybVPy1NpzJ4-93o',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

a =json.loads(response.text)
print(payload)
print(a.get("msg"))
print(response.text)