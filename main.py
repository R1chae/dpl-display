import urequests as requests
import config.py

def doAPICall():
    url = "https://dpl.easypensum.com/api/filter"

    payload = "{\"name\":\"" + config.name + "\",\"user\":\"" + config.user + "\",\"password\":\"" + config.password + "\"}"
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
      'Accept': '*/*',
      'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/json; charset=utf-8',
      'Referer': 'https://dpl.easypensum.com/',
      'Origin': 'https://dpl.easypensum.com',
      'DNT': '1',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'Connection': 'keep-alive'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(response)

print(doAPICall().text)