import requests
from settings import API_URL


def importer(session, file, model):
    # API request to import data to server (projects, vendors, subAccounts, transactions)
    try:
        data = {"file": file}

        if model == "projects":
            response = session.post(API_URL + "importProjects/", data=data)
        elif model == "vendors":
            response = session.post(API_URL + "importVendors/", data=data)
        elif model == "subAccounts":
            response = session.post(API_URL + "importSubAccounts/", data=data)
        elif model == "transactions":
            response = session.post(API_URL + "importTransactions/", data=data)
        else:
            return False, "Invalid model"

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def exporter(session, model):
    # API request to export data from server (projects, vendors, subAccounts)
    try:
        if model == "projects":
            response = session.get(API_URL + "exportProjects/")
        elif model == "vendors":
            response = session.get(API_URL + "exportVendors/")
        elif model == "subAccounts":
            response = session.get(API_URL + "exportSubAccounts/")
        else:
            return False, "Invalid model"

        if response.status_code == 200:
            return True, response.content
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def exportTransactions(session, fromDate=None, toDate=None):
    # API request to export transactions from server
    try:
        data = {"fromDate": fromDate, "toDate": toDate}
        response = session.get(API_URL + "exportTransactions/", params=data)

        if response.status_code == 200:
            return True, response.content
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"