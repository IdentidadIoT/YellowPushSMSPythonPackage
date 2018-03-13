![YellowPush](https://www.identidadsms.net/yellowpush/wp-content/uploads/2018/02/logo-Yellow-Push.png)

# YellowPush SMS Api


## Installation

The easiest way to install the library is from PyPi using pip, a package manager for Python. Simply run this in the terminal:
Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install YellowPushSMS
    
    
### Client Reference  
YellowPush API needs your YellowPush credentials. You can either pass these directly to the constructor.

**NOTE:** For better performance you can pass credentials and the account Identifier directly to the constructor (see the code below)

```python  
class yellowPushSMS.rest.Client(user, password, account_id = None)

```

### Client parameters:	

- user (str) : Your account user
- password (str) : Your account password 
- account_id (str) : Your account id (optional)
   

### Send an SMS

Sends a text message to one or more mobile numbers

```python

from yellowPushSMS.rest import Client

# Your Account user
user = "XXXXXXXXXXX"
# Your Account password
password  = "XXXXXXXXXXXXXX"
# Your Account Identifier
account_id  = "XXXXXXXXXXXXXX"

client = Client(user, password, account_id)

rsp = client.SendSMS(mobileNumbers="xxxxxxxxxxx,xxxxxxxxxxx", from_="xxxxxxx", message="hello")
print(rsp)

```
### Send Bulk SMS

Sends single, bulk text messages

```python

from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxxxxxx"
# Your Account password
password = "xxxxxxxxxxxxx"
# Your Account Identifier
account_id  = "XXXXXXXXXXXXXX"

client = Client(user, password, account_id)

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

```

### Get Message Status

Gets the messages satatus

```python

from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxxxxx"
# Your Account password
password = "xxxxxxxxxx"
# Your Account Identifier
account_id  = "XXXXXXXXXXXXXX"

client = Client(user, password, account_id)

rsp = client.GetMessageStatus(messageId="5a5600d4-295b-6626-8a07-831993fa443c",
                              sendDate="2018-03-05")
print(rsp)

```
