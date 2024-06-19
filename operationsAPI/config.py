import requests
from requests.exceptions import ConnectionError
from settings import API_URL
from auth import login


def isConfigured():
    # API request to check if the app is configured
    try:
        response = requests.get(API_URL + "isConfigured/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["configured"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False


def configure(organisation, postCode, city, street, NIP, accountNumber,
              accountBalance, treasurerName, treasurerLogin, treasurerPassword):
    # API request to configure the app and login treasurer
    try:
        data = {
            "organisation": organisation,
            "postCode": postCode,
            "city": city,
            "street": street,
            "NIP": NIP,
            "accountNumber": accountNumber,
            "accountBalance": accountBalance,
            "treasurerName": treasurerName,
            "treasurerLogin": treasurerLogin,
            "treasurerPassword": treasurerPassword
        }

        response = requests.post(API_URL + "configure/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            loginResponse = login(treasurerLogin, treasurerPassword)

            if loginResponse[0]:
                return True, response.json()["message"]
            else:
                return False, loginResponse[1]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def getConfig():
    # API request to get config
    try:
        response = requests.get(API_URL + "config/")

        if response.status_code == 200:
            return True, response.json()["configuration"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"
