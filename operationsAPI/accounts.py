import requests
from settings import API_URL


def getAccounts(session):
    # API request to get accounts
    try:
        response = session.get(API_URL + "accounts/")

        if response.status_code == 200:
            return True, response.json()["accounts"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createAccount(session, name, accountNumber, balance):
    # API request to create account
    try:
        data = {
            "accountName": name,
            "accountNumber": accountNumber,
            "accountBalance": balance
        }

        response = session.post(API_URL + "createAccount/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteAccount(session, name):
    # API request to delete account
    try:
        response = session.delete(API_URL + f"deleteAccount/{name}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"