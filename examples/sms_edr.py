#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-


from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxxxxxxxx"
# Your Account password
password = "xxxxxxxxxxxxxxxx"

client = Client(user, password)

rsp = client.GetMessageStatus(messageId="5a5600d4-295b-6626-8a07-831993fa443c",
                              sendDate="2018-03-05")
print(rsp)
