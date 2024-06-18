import requests
from requests.exceptions import ConnectionError
import os
from settings import API_URL


def login(username, password):
    try:
        data = {"username": username, "password": password}
        response = requests.post(API_URL + "login/", data=data)
        if response.status_code == 200 and response.json()["status"] == "success":
            session = requests.Session()
            session.cookies.set("sessionid", response.json()["sessionKey"])

            return True, session
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def logout(session):
    try:
        response = session.post(API_URL + "logout/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, None
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def register(username, password):
    try:
        data = {"username": username, "password": password}
        response = requests.post(API_URL + "register/", data=data)
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, None
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def sessionInfo(session):
    try:
        response = session.get(API_URL + "sessionInfo/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["sessionKey"]
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getUsers(session):
    try:
        response = session.get(API_URL + "users/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["users"]
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def isSuperuser(session):
    try:
        response = session.get(API_URL + "isSuperuser/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["isSuperuser"]
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getMyPermissions(session):
    try:
        response = session.get(API_URL + "permissions/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["permissions"]
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def getAllPermissions(session):
    try:
        response = session.get(API_URL + "allPermissions")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["permissions"]
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def givePermission(session, user, project):
    try:
        data = {"user": user, "projectName": project}
        response = session.post(API_URL + 'givePermission/', data=data)
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, None
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def removePermission(session, user, project):
    try:
        response = session.get(API_URL + "removePermission/" + user + "/" + project + "/")
        if response.status_code == 200 and response.json()["status"] == "success":
            return True, None
        return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection Error"


def checkConnection():
    try:
        response = requests.get(API_URL)
        return True
    except ConnectionError:
        return False
