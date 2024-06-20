import customtkinter as ctk
import settings
from viewsList import ViewsList
import views
import operationsAPI
import json


class Controller:
    def __init__(self):
        self.app = views.app.App()
        self.session = None
        self.currentView = None
        self.language = json.load(open("language.json", "r", encoding="utf-8"))
        ctk.set_appearance_mode(settings.MODE)

    def run(self):
        if operationsAPI.config.isConfigured()[1]:
            self.changeView(ViewsList.START)
        else:
            self.changeView(ViewsList.CONFIGURE)

        self.app.mainloop()

    def changeView(self, view, model=None):

        if self.currentView is not None:
            self.currentView.destroy()
            self.app.currentUi.clear()

        match view:
            case ViewsList.START:
                self.currentView = views.startView.StartView(self.app,
                                                             lambda: self.changeView(ViewsList.LOGIN),
                                                             lambda: self.changeView(ViewsList.REGISTER),
                                                             lambda: self.changeView(ViewsList.START))
            case ViewsList.LOGIN:
                self.currentView = views.loginView.Login(self.app,
                                                         self.login,
                                                         lambda: self.changeView(ViewsList.START),
                                                         lambda: self.changeView(ViewsList.REGISTER))
            case ViewsList.REGISTER:
                self.currentView = views.registerView.Register(self.app,
                                                               self.register,
                                                               lambda: self.changeView(ViewsList.START))
            case ViewsList.CONFIGURE:
                self.currentView = views.configureView.ConfigView(self.app,
                                                                  self.configure)
            case ViewsList.DASHBOARD:
                isSuperUser = operationsAPI.auth.isSuperUser(self.session)
                self.currentView = views.dashboardView.Dashboard(self.app,
                                                                 isSuperUser,
                                                                 self.changeView(ViewsList.START),
                                                                 self.show,
                                                                 self.importData,
                                                                 self.exportData)

        self.currentView.pack()
        self.currentView.grid(row=0, column=0)
        self.app.currentUi.append(self.currentView)

    def showPopup(self, message):
        popup = views.popupView.PopupView(self.app, message)

    def login(self):
        username = self.currentView.usernameEntry.get()
        password = self.currentView.passwordEntry.get()

        success, response = operationsAPI.auth.login(username, password)
        if success:
            self.session = response
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def register(self):
        username = self.currentView.usernameEntry.get()
        password = self.currentView.passwordEntry.get()
        passwordConfirm = self.currentView.passwordConfirmEntry.get()

        if password != passwordConfirm:
            self.showPopup(self.language["passwordMismatch"])
            return

        success, response = operationsAPI.auth.register(username, password)
        if success:
            self.showPopup(response)
            self.changeView(ViewsList.LOGIN)
        else:
            self.showPopup(response)

    def configure(self):
        organisation = self.currentView.organisationEntry.get()
        nip = self.currentView.nipEntry.get()
        accountNumber = self.currentView.accountNumberEntry.get()
        treasurer = self.currentView.treasurerEntry.get()
        street = self.currentView.streetEntry.get()
        postCode = self.currentView.postCodeEntry.get()
        city = self.currentView.cityEntry.get()
        treasurerLogin = self.currentView.usernameEntry.get()
        treasurerPassword = self.currentView.passwordEntry.get()
        passwordConfig = self.currentView.passwordConfigEntry.get()

        if treasurerPassword != passwordConfig:
            self.showPopup(self.language["passwordMismatch"])
            return

        success, response = operationsAPI.config.configure(organisation, postCode, city, street, nip, accountNumber,
                                                           0, treasurer, treasurerLogin, treasurerPassword)
        if success:
            self.showPopup(response)
            self.changeView(ViewsList.START)
        else:
            self.showPopup(response)

    def show(self, what):
