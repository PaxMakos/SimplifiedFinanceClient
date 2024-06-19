import requests
from settings import API_URL


def getProjects(session):
    # API request to get projects
    try:
        response = session.get(API_URL + "projects/")

        if response.status_code == 200:
            return True, response.json()["projects"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def createProject(session, name, description, startDate, endDate, status):
    # API request to create project
    try:
        data = {
            "projectName": name,
            "projectDescription": description,
            "projectStartDate": startDate,
            "projectEndDate": endDate,
            "projectStatus": status
        }

        response = session.post(API_URL + "createProject/", data=data)

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def deleteProject(session, name):
    # API request to delete project
    try:
        response = session.delete(API_URL + f"deleteProject/{name}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"


def endProject(session, name):
    # API request to end project
    try:
        response = session.put(API_URL + f"endProject/{name}/")

        if response.status_code == 200 and response.json()["status"] == "success":
            return True, response.json()["message"]
        else:
            return False, response.json()["message"]
    except ConnectionError:
        return False, "Connection error"