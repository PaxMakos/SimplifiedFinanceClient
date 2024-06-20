import requests
from settings import API_URL


def getReturns(session):
    # API request to get returns
    try:
        response = session.get(API_URL + "returns/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["returns"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createReturn(project, title, date, amount, description, account, file):
    # API request to create return
    try:
        data = {
            "projectName": project,
            "returnTitle": title,
            "returnDate": date,
            "returnAmount": amount,
            "returnDescription": description,
            "accountToReturn": account,
            "invoice": file
        }

        response = requests.post(API_URL + "createReturn/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteReturn(session, id):
    # API request to delete return
    try:
        response = session.delete(API_URL + f"deleteReturn/{id}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"