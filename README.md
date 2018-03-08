![YellowPush](https://www.identidadsms.net/yellowpush/wp-content/uploads/2018/02/logo-Yellow-Push.png)

# YellowPush SMS Api


## Installation

The easiest way to install the library is from PyPi using pip, a package manager for Python. Simply run this in the terminal:
Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install YellowPushSMS
    
    
### Client Reference  
YellowPush API needs your YellowPush credentials. You can either pass these directly to the constructor.

```python  
class yellowPushSMS.rest.Client(user, password, account_id = None)

```
### Client parameters:	

- user (str) : Your account user
- password (str) : Your account password 
- account_id (str) : Your account id (optional)
   

### Send an SMS

```python

from yellowPushSMS.rest import Client

# Your Account user
user = "XXXXXXXXXXX"
# Your Account password
password  = "XXXXXXXXXXXXXX"


client = Client(user, password)

rsp = client.SendSMS(mobileNumbers="xxxxxxxxxxx", from_="xxxxxxx", message="hello")
print(rsp)

```

### Request SMS EDR

```python

from yellowPushSMS.rest import Client

# Your Account user
user = "xxxxxxxxxx"
# Your Account password
password = "xxxxxxxxxx"

client = Client(user, password)

rsp = client.GetMessageStatus(messageId="5a5600d4-295b-6626-8a07-831993fa443c",
                              sendDate="2018-03-05")
print(rsp)

```

### Send Bulk SMS

```python

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

```
