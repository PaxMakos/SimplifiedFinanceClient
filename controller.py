import customtkinter as ctk
import pandas as pd

import settings
from viewsList import ViewsList
import views
import operationsAPI
import json
from datetime import datetime, timedelta


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

    def changeView(self, view, model=None, data=None):

        if self.currentView is not None:
            self.currentView.destroy()
            self.app.currentUi.clear()

        match view:
            case ViewsList.START:
                self.currentView = views.startView.StartView(self.app,
                                                             lambda: self.changeView(ViewsList.LOGIN),
                                                             lambda: self.changeView(ViewsList.REGISTER),
                                                             lambda: self.changeView(ViewsList.ADD_RETURN))
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
                isSuperUser = operationsAPI.auth.isSuperuser(self.session)[1]
                self.currentView = views.dashboardView.Dashboard(self.app,
                                                                 isSuperUser,
                                                                 self.logout,
                                                                 self.show,
                                                                 self.importData,
                                                                 self.exportData)
            case ViewsList.ADD_RETURN:
                if self.session is None:
                    prev = ViewsList.START
                else:
                    prev = ViewsList.DASHBOARD

                self.currentView = views.addReturnView.AddReturnView(self.app,
                                                                     self.addReturn,
                                                                     lambda: self.changeView(prev))
            case ViewsList.RECORD_LIST:
                if model == "vendors":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "vendors",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsVendor,
                                                                           lambda: self.changeView(ViewsList.ADD_VENDOR))
                elif model == "projects":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "projects",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsProject,
                                                                       lambda: self.changeView(ViewsList.ADD_PROJECT))
                elif model == "returns":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "returns",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsReturn)
                elif model == "accounts":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "accounts",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsAccount,
                                                                       lambda: self.changeView(ViewsList.ADD_ACCOUNT))
                elif model == "transactions":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "transactions",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsTransaction,
                                                                       lambda: self.changeView(ViewsList.ADD_TRANSACTION))
                elif model == "invoices":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "invoices",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           self.detailsInvoice,
                                                                           lambda: self.changeView(ViewsList.ADD_INVOICE))
                elif model == "users":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                           "users",
                                                                           data,
                                                                           lambda: self.changeView(ViewsList.DASHBOARD),
                                                                           lambda: self.changeView(ViewsList.ADD_PERMISSION))
                elif model == "permissions":
                    self.currentView = views.recordListView.RecordView(self.app,
                                                                       "permissions",
                                                                       data,
                                                                       lambda: self.changeView(ViewsList.DASHBOARD),
                                                                       lambda: self.removePermission)
            case ViewsList.ADD_ACCOUNT:
                self.currentView = views.addingViews.AddAccount(self.app,
                                                                self.addAccount,
                                                                lambda: self.changeView(ViewsList.DASHBOARD))
            case ViewsList.ADD_INVOICE:
                self.currentView = views.addingViews.AddInvoice(self.app,
                                                                self.addInvoice,
                                                                lambda: self.changeView(ViewsList.DASHBOARD))
            case ViewsList.ADD_PROJECT:
                self.currentView = views.addingViews.AddProject(self.app,
                                                                self.addProject,
                                                                lambda: self.changeView(ViewsList.DASHBOARD))
            case ViewsList.ADD_TRANSACTION:
                self.currentView = views.addingViews.AddTransaction(self.app,
                                                                      self.addTransaction,
                                                                      lambda: self.changeView(ViewsList.DASHBOARD))
            case ViewsList.ADD_VENDOR:
                self.currentView = views.addingViews.AddVendor(self.app,
                                                               self.addVendor,
                                                               lambda: self.changeView(ViewsList.DASHBOARD))
            case ViewsList.ADD_PERMISSION:
                self.currentView = views.addingViews.AddPermission(self.app,
                                                                   self.givePermission,
                                                                   lambda: self.changeView(ViewsList.DASHBOARD))


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
        if what == "vendors":
            success, response = operationsAPI.vendors.getVendors(self.session)
        elif what == "projects":
            success, response = operationsAPI.projects.getProjects(self.session)
        elif what == "returns":
            success, response = operationsAPI.returns.getReturns(self.session)
        elif what == "accounts":
            success, response = operationsAPI.accounts.getAccounts(self.session)
        elif what == "transactions":
            success, response = operationsAPI.transactions.getTransactions(self.session)
        elif what == "invoices":
            success, response = operationsAPI.invoices.getInvoices(self.session)
        elif what == "users":
            success, response = operationsAPI.auth.getUsers(self.session)
        elif what == "permissions":
            success, response = operationsAPI.auth.getAllPermissions(self.session)

        if not success:
            self.showPopup(response)
            return
        else:
            self.changeView(ViewsList.RECORD_LIST, what, pd.DataFrame(response))

    def importData(self):
        pass

    def exportData(self):
        pass

    def logout(self):
        success, response = operationsAPI.auth.logout(self.session)

        if success:
            self.session = None
            self.changeView(ViewsList.START)
        else:
            self.showPopup(response)

    def addReturn(self, filePath):
        project = self.currentView.projectNameEntry.get()
        title = self.currentView.returnTitleEntry.get()
        date = self.currentView.returnDateEntry.get()
        amount = self.currentView.returnAmountEntry.get()
        description = self.currentView.returnDescriptionEntry.get()
        account = self.currentView.accountToReturnEntry.get()
        file = filePath

        success, response = operationsAPI.returns.createReturn(project, title, date, amount, description, account, file)
        if success:
            self.showPopup(response)

            if self.session is None:
                self.changeView(ViewsList.START)
            else:
                self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsVendor(self, name):
        pass

    def addVendor(self):
        vendorName = self.currentView.vendorNameEntry.get()
        vendorPostCode = self.currentView.vendorPostCodeEntry.get()
        vendorCity = self.currentView.vendorCityEntry.get()
        vendorStreet = self.currentView.vendorStreetEntry.get()
        vendorNIPNumber = self.currentView.vendorNIPNumberEntry.get()
        vendorAccountNumber = self.currentView.vendorAccountNumberEntry.get()

        success, response = operationsAPI.vendors.createVendor(self.session, vendorName, vendorPostCode, vendorCity,
                                                               vendorStreet, vendorNIPNumber, vendorAccountNumber)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsProject(self, name):
        pass

    def addProject(self):
        projectName = self.currentView.nameEntry.get()
        projectDescription = self.currentView.descriptionEntry.get()
        projectStartDate = self.currentView.startEntry.get()
        projectEndDate = self.currentView.endEntry.get()
        projectStatus = self.currentView.statusEntry.get()

        success, response = operationsAPI.projects.createProject(self.session, projectName, projectDescription,
                                                                    projectStartDate, projectEndDate, projectStatus)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsReturn(self, id):
        pass

    def detailsAccount(self, name):
        pass

    def addAccount(self):
        name = self.currentView.nameEntry.get()
        balance = self.currentView.balanceEntry.get()
        number = self.currentView.numberEntry.get()

        success, response = operationsAPI.accounts.createAccount(self.session, name, number, balance)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsTransaction(self, id):
        pass

    def addTransaction(self):
        date = self.currentView.dateEntry.get()
        amount = self.currentView.amountEntry.get()
        description = self.currentView.descriptionEntry.get()
        title = self.currentView.titleEntry.get()
        account = self.currentView.accountEntry.get()
        vendor = self.currentView.vendorEntry.get()
        project = self.currentView.projectEntry.get()
        invoice = self.currentView.invoiceEntry.get()

        success, response = operationsAPI.transactions.createTransaction(self.session, date, title, description,
                                                                         amount, account, vendor, project, invoice)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsInvoice(self, number):
        pass

    def addInvoice(self, filePath):
        number = self.currentView.numberEntry.get()
        date = self.currentView.dateEntry.get()
        description = self.currentView.descriptionEntry.get()
        file = filePath

        success, response = operationsAPI.invoices.createInvoice(self.session, number, date, description, file)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def detailsUser(self, username):
        pass

    def givePermission(self):
        username = self.currentView.usernameEntry.get()
        permission = self.currentView.permissionEntry.get()

        success, response = operationsAPI.auth.givePermission(self.session, username, permission)

        if success:
            self.showPopup(response)
            self.changeView(ViewsList.DASHBOARD)
        else:
            self.showPopup(response)

    def removePermission(self, username):
        pass

