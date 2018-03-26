# All imports here 
import sys
sys.path.append(r'C:\Users\Marie\AppData\Local\Programs\Python\Python36\Lib\site-packages')
from lib import lib
#lib.cfg["token"] = "WcMqRIgjXQQ8iKwfLq67VMifCDMfSb9NwxmSWWwkkytlDLogr80eN7nB5gmF43iq"

#print("Hello")
#print(dir(lib))

# All functions here 

AUTH_STATUS = False
CLIENT_NUMBER = "14039992180" # Client's phone number

def sendText(AUTH_STATUS, people_list):
    
    #assert AUTH_STATUS # errors if no authentication status provided (ie no result yet)
    
    if(AUTH_STATUS == False):
        #abc = lib(token="PZZFz7ANF3W4VwGX6kgS6I2T9PBjjisy0FFPmMJflvtMQqXuYS8C_2OWnv0YtpQ7")

        sms = lib.messagebird.sms["@0.1.3"]
        
        # Sends a text to the customer 
        sms.create(
            recipient=CLIENT_NUMBER, # (required, replace with people_list info)
            body="Bank account security alert - Please contact your bank advisor asap." # (required)
        )
    elif(AUTH_STATUS == True):
        #abc = lib(token="PZZFz7ANF3W4VwGX6kgS6I2T9PBjjisy0FFPmMJflvtMQqXuYS8C_2OWnv0YtpQ7")

        sms = lib.messagebird.sms["@0.1.3"]
        
        # Sends a text to the customer 
        sms.create(
            recipient=CLIENT_NUMBER, # (required)
            body="Authentication successful, transaction in progress" # (required)
        )
    
    return 0; 

sendText(AUTH_STATUS, ["Ayesha"])