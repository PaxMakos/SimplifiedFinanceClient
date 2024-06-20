import requests
from requests.exceptions import ConnectionError
from settings import API_URL


def login(username, password):
    # API request to login
    try:
        data = {"username": username, "password": password}
        response = requests.post(API_URL + "login/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            session = requests.Session()
            session.cookies.set("sessionid", response.json()["sessionKey"])

            return True, session
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def logout(session):
    # API request to logout
    try:
        response = session.post(API_URL + "logout/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def register(username, password):
    # API request to register new user
    try:
        data = {"username": username, "password": password}
        response = requests.post(API_URL + "register/", data=data)
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def sessionInfo(session):
    # API request to get session info
    try:
        response = session.get(API_URL + "sessionInfo/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["sessionKey"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getUsers(session):
    # API request to get all users
    try:
        response = session.get(API_URL + "users/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["users"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def isSuperuser(session):
    # API request to check if user is superuser
    try:
        response = session.get(API_URL + "isSuperuser/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getMyPermissions(session):
    # API request to get user permissions
    try:
        response = session.get(API_URL + "permissions/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["permissions"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getAllPermissions(session):
    # API request to get all permissions
    try:
        response = session.get(API_URL + "allPermissions")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["permissions"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def givePermission(session, user, project):
    # API request to give permission to user
    try:
        data = {"user": user, "projectName": project}
        response = session.post(API_URL + 'givePermission/', data=data)
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def removePermission(session, user, project):
    # API request to remove permission from user
    try:
        response = session.get(API_URL + "removePermission/" + user + "/" + project + "/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def checkConnection():
    # Check if API is available
    try:
        response = requests.get(API_URL)
        return True
    except ConnectionError:
        return False
