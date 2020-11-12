import requests
from requests.structures import CaseInsensitiveDict
import json
from time import sleep as wait
h = CaseInsensitiveDict()
namepls = str(input("Enter the name to be GC's title: "))
token = str(input("Enter your token: "))
channelid = int(input("Enter the group ID: "))
cookie = str(input("Enter your cookie: "))
jsonshit = {"name":namepls}
h['method'] = "PATCH"
h['path'] = '/api/v8/channels/{}'.format(channelid)
h['authorization'] = token
h['content-length'] = "{}".format(len(json.dumps(jsonshit)))
h['content-type'] = 'application/json'
h['cookie'] = '{}'.format(cookie)
h['origin'] = 'https://discordapp.com'
h['referer'] = 'https://discordapp.com/channels/@me/{}'.format(channelid)
h['x-super-properties'] = 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjAuMC4zMDgiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MSIsIm9zX2FyY2giOiJ4NjQiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo3MTQ0NywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='
num = 0
increase = True
while True:
    wait(.5)
    if num <= len(namepls) and increase == True:
        num = num +1
    elif num > len(namepls) and increase == True:
        increase = False
        num = len(namepls)
    if num >= 0 and increase == False:
        num = num -1
    elif num < 0 and increase == False:
        increase = True
        num = 0
    jsonshit['name'] = namepls[:num]
    lol = requests.patch(url='https://discordapp.com/api/v8/channels/{}'.format(channelid),headers=h,json=jsonshit)