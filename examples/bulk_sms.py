#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-


from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxxxxxx"
# Your Account password
password = "xxxxxxxxxxxxx"

client = Client(user, password)

list_messages = [
    {
        "from": "xxxx",
        "to": "xxxxxxxxxxxx",
        "message": "hola1"
    },
    {
        "from": "xxxx",
        "to": "xxxxxxxxxxxx",
        "message": "hola2"
    },
]

rsp = client.BulkSendSMS(listMessages=list_messages)
print(rsp)
