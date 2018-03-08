#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-


from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxx"
# Your Account password
password = "xxxxx@."

client = Client(user, password)
rsp = client.SendSMS(mobileNumbers="xxxxxxxxxxx", from_="xxxxxxx", message="hello")

print(rsp)
