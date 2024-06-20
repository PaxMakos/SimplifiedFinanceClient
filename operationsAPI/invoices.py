import requests
from settings import API_URL


def downloadInvoice(session, invoiceNumber):
    # API request to download invoice
    try:
        response = session.get(API_URL + f"downloadInvoice/{invoiceNumber}/")

        if response.status_code == 200:
            return True, response.content
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def getInvoice(session, invoiceNumber):
    # API request to get invoice
    try:
        response = session.get(API_URL + f"getInvoice/{invoiceNumber}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["invoice"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def getInvoices(session):
    # API request to get invoices
    try:
        response = session.get(API_URL + "invoices/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["invoices"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createInvoice(session, invoiceNumber, invoiceDate, description, filePath):
    # API request to create invoice
    try:
        with open(filePath, "rb") as file:

            data = {
                "invoiceNumber": invoiceNumber,
                "invoiceDate": invoiceDate,
                "invoiceDescription": description,
            }

            files = {"file": file}

            response = session.post(API_URL + "createInvoice/", data=data, files=files)

            if response.status_code == 200 and response.json()["status"] == "success":
                return True, response.json()["message"]
            else:
                return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def updateInvoice(session, invoiceNumber, invoiceDate=None, description=None, filePath=None):
    # API request to update invoice
    try:
        data = {
            "invoiceDate": invoiceDate,
            "invoiceDescription": description,
        }

        if filePath:
            with open(filePath, "rb") as file:
                files = {"file": file}
                response = session.put(API_URL + f"updateInvoice/{invoiceNumber}/", data=data, files=files)
        else:
            response = session.put(API_URL + f"updateInvoice/{invoiceNumber}/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteInvoice(session, invoiceNumber):
    # API request to delete invoice
    try:
        response = session.delete(API_URL + f"deleteInvoice/{invoiceNumber}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def generateInvoice(session, invoiceNumber, sellDate, invoiceDate, paymentDate, vendorName, products):
    # API request to generate invoice
    try:
        data = {
            "invoiceNumber": invoiceNumber,
            "sellDate": sellDate,
            "invoiceDate": invoiceDate,
            "paymentTo": paymentDate,
            "vendorName": vendorName,
            "products": products
        }

        response = session.post(API_URL + "generateInvoice/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"
