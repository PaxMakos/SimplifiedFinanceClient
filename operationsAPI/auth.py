import requests
import os
from settings import API_URL


def login(username, password):
    data = {"username": username, "password": password}

    response = requests.post(API_URL + "login/", data=data)

    if response.status_code == 200 and response.json()["status"] == "success":
        session = requests.Session()
        session.cookies.set("sessionid", response.json()["sessionKey"])

        return True, session

    return False, response.json()["message"]


def logout(session):
    response = session.post(API_URL + "logout/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, None

    return False, response.json()["message"]


def register(username, password):
    data = {"username": username, "password": password}

    response = requests.post(API_URL + "register/", data=data)

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, None

    return False, response.json()["message"]


def sessionInfo(session):
    response = session.get(API_URL + "sessionInfo/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, response.json()["sessionKey"]

    return False, response.json()["message"]


def getUsers(session):
    response = session.get(API_URL + "users/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, response.json()["users"]

    return False, response.json()["message"]


def isSuperuser(session):
    response = session.get(API_URL + "isSuperuser/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, response.json()["isSuperuser"]

    return False, response.json()["message"]


def getMyPermissions(session):
    response = session.get(API_URL + "permissions/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, response.json()["permissions"]

    return False, response.json()["message"]


def getAllPermissions(session):
    response = session.get(API_URL + "allPermissions")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, response.json()["permissions"]

    return False, response.json()["message"]


def givePermission(session, user, project):
    data = {"user": user, "projectName": project}

    response = session.post(API_URL + 'givePermission/', data=data)

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, None

    return False, response.json()["message"]


def removePermission(session, user, project):
    response = session.get(API_URL + "removePermission/" + user + "/" + project + "/")

    if response.status_code == 200 and response.json()["status"] == "success":
        return True, None

    return False, response.json()["message"]