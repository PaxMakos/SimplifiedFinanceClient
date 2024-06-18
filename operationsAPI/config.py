import requests
from requests.exceptions import ConnectionError
from settings import API_URL
from auth import login


def isConfigured():
    try:
        response = requests.get(API_URL + "isConfigured/")

        return response.status_code == 200 and response.json()["configured"]

    except ConnectionError:
        return False


def configure(organisation, postCode, city, street, NIP, accountNumber,
              accountBalance, treasurerName, treasurerLogin, treasurerPassword):
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

        if response.status_code == 200 and "error" not in response.json():
            loginResponse = login(treasurerLogin, treasurerPassword)
            session = requests.Session()
            session.cookies.set("sessionid", loginResponse.json()["sessionKey"])

            return True, None

        return False, response.json()["error"]
    except ConnectionError:
        return False, "Connection error"


def getConfig():
    try:
        response = requests.get(API_URL + "config/")

        if response.status_code == 200:
            return True, response.json()

        return False, response.json()["error"]
    except ConnectionError:
        return False, "Connection error"