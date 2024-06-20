from settings import API_URL


def getTransactions(session, fromDate=None, toDate=None):
    # API request to get transactions
    try:
        data = {"fromDate": fromDate, "toDate": toDate}
        response = session.get(API_URL + f"transactions/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["transactions"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createTransaction(session, transactionDate, title, description, amount, account, vendor, project, invoice):
    # API request to create transaction
    try:
        data = {
            "transactionDate": transactionDate,
            "transactionTitle": title,
            "transactionDescription": description,
            "transactionAmount": amount,
            "accountName": account,
            "vendorName": vendor,
            "projectNAme": project,
            "invoiceNumber": invoice
        }

        response = session.post(API_URL + "createTransactionBasic/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createTransactionAndInvoice(session, transactionDate, title, description, amount, account, vendor, project,
                                invoiceNumber, invoiceDate, invoiceDescription, file):
    # API request to create transaction and invoice
    try:
        data = {
            "transactionDate": transactionDate,
            "transactionTitle": title,
            "transactionDescription": description,
            "transactionAmount": amount,
            "accountName": account,
            "vendorName": vendor,
            "projectNAme": project,
            "invoiceNumber": invoiceNumber,
            "invoiceDate": invoiceDate,
            "invoiceDescription": invoiceDescription,
            "file": file
        }

        response = session.post(API_URL + "createTransactionInvoice/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createTransactionAndVendor(session, transactionDate, title, description, amount, account, vendor, project,
                               vendorPostCode, vendorCity, vendorStreet, vendorNIPNumber, vendorBankAccount):
    # API request to create transaction and vendor
    try:
        data = {
            "transactionDate": transactionDate,
            "transactionTitle": title,
            "transactionDescription": description,
            "transactionAmount": amount,
            "accountName": account,
            "vendorName": vendor,
            "projectNAme": project,
            "vendorPostCode": vendorPostCode,
            "vendorCity": vendorCity,
            "vendorStreet": vendorStreet,
            "vendorNIPNumber": vendorNIPNumber,
            "vendorAccountNumber": vendorBankAccount
        }

        response = session.post(API_URL + "createTransactionNewVendor/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createTransactionFull(session, transactionDate, title, description, amount, account, vendor, project,
                          invoiceNumber, invoiceDate, invoiceDescription, file,
                          vendorPostCode, vendorCity, vendorStreet, vendorNIPNumber, vendorBankAccount):
    # API request to create transaction full
    try:
        data = {
            "transactionDate": transactionDate,
            "transactionTitle": title,
            "transactionDescription": description,
            "transactionAmount": amount,
            "accountName": account,
            "vendorName": vendor,
            "projectNAme": project,
            "invoiceNumber": invoiceNumber,
            "invoiceDate": invoiceDate,
            "invoiceDescription": invoiceDescription,
            "file": file,
            "vendorPostCode": vendorPostCode,
            "vendorCity": vendorCity,
            "vendorStreet": vendorStreet,
            "vendorNIPNumber": vendorNIPNumber,
            "vendorAccountNumber": vendorBankAccount
        }

        response = session.post(API_URL + "createTransactionFull/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def updateTransaction(session, transactionID, transactionDate=None, title=None, description=None, amount=None,
                      account=None, vendor=None, project=None):
    # API request to update transaction
    try:
        data = {
            "transactionDate": transactionDate,
            "transactionTitle": title,
            "transactionDescription": description,
            "transactionAmount": amount,
            "accountName": account,
            "vendorName": vendor,
            "projectNAme": project
        }

        response = session.put(API_URL + f"updateTransaction/{transactionID}/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteTransaction(session, transactionID):
    # API request to delete transaction
    try:
        response = session.delete(API_URL + f"deleteTransaction/{transactionID}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"
