import requests

url = ""

r = requests.post(url, data = {
  "content[]" : "value"
})

print(r.text)
