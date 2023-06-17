import urequests as requests
import network
import utime
import ujson
import gzip
import framebuf
from machine import Pin, SPI

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# [CREDENTIALS]
dplname = "yourNameAsUsedOnEasypensum"
dpluser = "yourUserAsUsedOnEasypensum"
dplpassword = "yourPasswordAsUsedOnEasypensum"

# [WIFI]
ssid = "yourSSID"
wifipassword = "yourPassword"

wlan.connect(ssid, wifipassword)
connectiontext = "awaiting connection."
while not wlan.isconnected():
    print(connectiontext)
    connectiontext += "."
    utime.sleep(1)
print(wlan.ifconfig())

def doAPICall():
    url = "https://dpl.easypensum.com/api/filter"

    payload = "{\"name\":\"" + dplname + "\",\"user\":\"" + dpluser + "\",\"password\":\"" + dplpassword + "\"}"
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

    
    response = requests.post(url, headers=headers, data=payload)

    return(response)

print(gzip.decompress(doAPICall().content).decode())
