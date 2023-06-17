import urequests as requests
import network
import utime
import ujson
import gzip
import framebuf
from epaperDriver import EPD
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

# [Display resolution]
EPD_WIDTH       = 400
EPD_HEIGHT      = 300

RST_PIN         = Pin(12)
DC_PIN          = Pin(8)
CS_PIN          = Pin(9)
BUSY_PIN        = Pin(13)

spi = SPI(1)
spi.init(baudrate=4000_000)

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

epd = EPD(spi, CS_PIN, DC_PIN, RST_PIN, BUSY_PIN)
epd.init()
buf = bytearray(400*300*2 // 4)
fbuf = framebuf.FrameBuffer(buf,400,300,framebuf.GS2_HMSB)
fbuf.fill(0x00)

epd.display_frame(buf)