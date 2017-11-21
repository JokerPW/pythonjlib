import requests
import json

class fromweb:
    def webDL (_self, url, file, mode):
        with open(file, mode) as dl:
            myResponse = requests.get(url)
            dl.write(myResponse.content)

    def callAPI (_self, url):
        myResponse = requests.get(url)

        if (myResponse.status_code == 200):
            jData = json.loads(myResponse.content)
            return json.dumps(jData)

        return ""