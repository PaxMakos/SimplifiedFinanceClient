from ..settings import API_URL


def getVendors(session):
    # API request to get vendors
    try:
        response = session.get(API_URL + "vendors/")

        if response.status_code == 200:
            return True, response.json()["vendors"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createVendor(session, name, postCode, city, street, NIPnumber, accountNumber):
    # API request to create vendor
    try:
        data = {
            "vendorName": name,
            "vendorPostCode": postCode,
            "vendorCity": city,
            "vendorStreet": street,
            "vendorNIP": NIPnumber,
            "vendorAccountNumber": accountNumber
        }

        response = session.post(API_URL + "createVendor/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteVendor(session, name):
    # API request to delete vendor
    try:
        response = session.delete(API_URL + f"deleteVendor/{name}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def updateVendor(session, name, postCode=None, city=None, street=None, NIPnumber=None, accountNumber=None):
    # API request to update vendor
    try:
        data = {
            "vendorPostCode": postCode,
            "vendorCity": city,
            "vendorStreet": street,
            "vendorNIP": NIPnumber,
            "vendorAccountNumber": accountNumber
        }

        response = session.put(API_URL + f"updateVendor/{name}/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"