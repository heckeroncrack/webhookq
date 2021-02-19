# Benchmarks queued discord requests
# Server must be running for it to work
import requests

webhook_url = ""

# Amount of requests that should be sent
requests_total = 100

def send_webhook(number=0):
    data = {
        "content": f"TEST {number}"
    }
    r = requests.post(webhook_url, json=data)
    return r

for i in range(1, requests_total+1):
    r = send_webhook(i)
    data = r.json()
    print(f"Sent request {i}. Status: {data['status']}. Seconds left: {data['secondsLeft']}")