import requests
import re

URL = 'https://27f7-2600-1003-b039-7f53-acf4-491-d49f-91a1.ngrok-free.app/texts'
pattern = r"\('(.*)', \"(.*)\"\)"


def receieveInfo():
    r = requests.get(url = URL)
    
    data = r.text
    
    #data = "(\'Hi\', \'Hi there! How can I help you?\')"
    result = re.findall(pattern, data)
    send_msg = result[0][0]
    reply_msg = result[0][1]
    print(send_msg)
    print(reply_msg)
    return send_msg
    


