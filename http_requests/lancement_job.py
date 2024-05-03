import json
import requests
# Construct the JSON data
json_data = {
    "name" : "jobtalendgenerate",
    "image" : "alakh1111/jgeneratedata_kube"
}
# Send the request to the Flask application
utf8_encoded_data = json.dumps(json_data, ensure_ascii=False).encode("utf-8")
response = requests.post("http://localhost/runjob", json=json_data, headers={"Content-Type": "application/json"})
print(response.text)  # Print response for debugging
 