from customtkinter import *
import customtkinter
import json

HEIGHT = 100
WIDTH = 200


class Dashboard(CTkFrame):
    def __init__(self, master, isSuperUser, logoutFunc, showFunc, importFunc, exportFunc):
        super().__init__(master)
        self.logoutFunc = logoutFunc
        self.showFunc = showFunc
        self.importFunc = importFunc
        self.exportFunc = exportFunc
        self.isSuperUser = isSuperUser
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["dashboardTitle"], font=("Arial", 20))

        self.transactionButton = CTkButton(self, text=lang["transactionsButton"],
                                           command=lambda: self.showFunc("transactions"),
                                           height=HEIGHT, width=WIDTH)
        self.invoiceButton = CTkButton(self, text=lang["invoicesButton"],
                                       command=lambda: self.showFunc("invoices"),
                                       height=HEIGHT, width=WIDTH)
        self.accountButton = CTkButton(self, text=lang["accountsButton"],
                                       command=lambda: self.showFunc("accounts"),
                                       height=HEIGHT, width=WIDTH)
        self.projectButton = CTkButton(self, text=lang["projectsButton"],
                                       command=lambda: self.showFunc("projects"),
                                       height=HEIGHT, width=WIDTH)
        self.permissionButton = CTkButton(self, text=lang["permissionsButton"],
                                          command=lambda: self.showFunc("permissions"),
                                          height=HEIGHT, width=WIDTH)
        self.vendorsButton = CTkButton(self, text=lang["vendorsButton"],
                                       command=lambda: self.showFunc("vendors"),
                                     height=HEIGHT, width=WIDTH)
        self.returnsButton = CTkButton(self, text=lang["returnsButton"],
                                       command=lambda: self.showFunc("returns"),
                                       height=HEIGHT, width=WIDTH)
        self.logoutButton = CTkButton(self, text=lang["logoutButton"], command=self.logoutFunc)
        self.importButton = CTkButton(self, text=lang["importButton"], command=self.importFunc,
                                      height=HEIGHT, width=WIDTH)
        self.exportButton = CTkButton(self, text=lang["exportButton"], command=self.exportFunc,
                                      height=HEIGHT, width=WIDTH)

        if self.isSuperUser:
            self.title.grid(row=0, column=0, columnspan=3, pady=20)
            self.transactionButton.grid(row=1, column=0, pady=10, padx=10)
            self.invoiceButton.grid(row=1, column=1, pady=10, padx=10)
            self.accountButton.grid(row=1, column=2, pady=10, padx=10)
            self.projectButton.grid(row=2, column=0, pady=10, padx=10)
            self.permissionButton.grid(row=2, column=1, pady=10, padx=10)
            self.vendorsButton.grid(row=2, column=2, pady=10, padx=10)
            self.returnsButton.grid(row=3, column=0, pady=10, padx=10)
            self.importButton.grid(row=3, column=1, pady=10, padx=10)
            self.exportButton.grid(row=3, column=2, pady=10, padx=10)
            self.logoutButton.grid(row=4, column=1, pady=10, padx=10)
        else:
            self.title.grid(row=0, column=0, columnspan=2, pady=20)
            self.transactionButton.grid(row=1, column=0, pady=10, padx=10)
            self.exportButton.grid(row=1, column=1, pady=10, padx=10)
            self.logoutButton.grid(row=3, column=0, pady=10, padx=10, columnspan=2)

        self.pack()


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")

    view = Dashboard(root, True, lambda arg: print("Logout", arg), lambda arg: print("Show", arg), lambda arg: print("Import", arg), lambda arg: print("Export", arg))
    root.mainloop()
