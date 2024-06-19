from controller import Controller
from operationsAPI import auth, config
import os
from settings import SERVER_CONFIG


if __name__ == "__main__":
    app = Controller()
    app.run()