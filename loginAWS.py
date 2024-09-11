import subprocess
import os
from dotenv import load_dotenv


def loginAws():
    load_dotenv()

    
    idKey = os.getenv('CREDENTIALKYID')
    psKey = os.getenv('CREDENTIALKYPSW')
 
    #command = ['aws', 'configure', 'set', 'aws_acess_key_id', idKey] , "aws_secret_acess_key"
    try:
        #send idkey to terminal
        command = ['aws', 'configure', 'set', 'aws_acess_key_id', idKey]
        result = subprocess.run(command , capture_output=True, text=True, check=True)

        #send password key to terminal
        command = ['aws', 'configure', 'set', 'aws_acess_key_id', psKey]
        result = subprocess.run(command , capture_output=True, text=True, check=True)

        #send default region name
        #send default output format
        #need to check if login was successfull
        if (checkLogin() == True):
            print("Login Successfull")
            return "ok"
        else:
            print("Failed to login")
            return "error"

    except subprocess.CalledProcessError as e:
        print(e.stderr)
    #process ends here


import json

def checkLogin():
    load_dotenv()
    arnKey = os.getenv("CREDENTIALARN")
    
    # Running the AWS STS command to get the caller identity
    command = ["aws", "sts", "get-caller-identity"]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    
    # Parse the JSON response
    result_json = json.loads(result.stdout)
    username = result_json["Arn"]
    
    # Compare the UserId from AWS with the idKey from environment variables
    if username == arnKey:
        return True
    else:
        return False


loginAws()
