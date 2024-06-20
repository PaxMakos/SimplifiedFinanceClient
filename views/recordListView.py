from customtkinter import *
import customtkinter
import json
import pandas as pd


class RecordView(CTkFrame):
    def __init__(self, master, recordType, recordData, goBack, action, createRecord=None):
        super().__init__(master)

        self.recordType = recordType
        self.recordData = recordData
        self.goBack = goBack
        self.createRecord = createRecord
        self.action = action
        self.lang = json.load(open("../language.json", "r", encoding="utf-8"))
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight() - 50

        self.createWidgets()

    def createWidgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1, minsize=20)
        self.grid_rowconfigure(1, weight=1, minsize=20)
        self.grid_rowconfigure(3, weight=1, minsize=self.height - 60)

        self.title = CTkLabel(self, text="Title", font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        self.goBackButton = CTkButton(self, text=self.lang["goBackButton"], command=self.goBack)
        self.newButton = CTkButton(self, text='', command=self.createRecord)

        if self.createRecord is not None:
            self.newButton.grid(row=1, column=0, pady=20, padx=20)
            self.goBackButton.grid(row=1, column=1, pady=20, padx=20)
        else:
            self.goBackButton.grid(row=1, column=0, pady=20, padx=20, columnspan=2)

        self.columnsTitle = CTkFrame(self)
        self.columnsTitle.grid(row=2, column=0, pady=20, padx=20, columnspan=2, sticky="nsew")

        if self.recordType == "projects":
            self.createProjectWidgets()
        elif self.recordType == "accounts":
            self.createAccountWidgets()
        elif self.recordType == "invoices":
            self.createInvoiceWidgets()
        elif self.recordType == "vendors":
            self.createVendorWidgets()
        elif self.recordType == "transactions":
            self.createTransactionWidgets()
        elif self.recordType == "permissions":
            self.createPermissionWidgets()
        elif self.recordType == "users":
            self.createUserWidgets()
        else:
            self.goBack()

    def createProjectWidgets(self):
        self.title.configure(text=self.lang["projectView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createProject"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 5)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 5)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 5)
        self.columnsTitle.grid_columnconfigure(3, weight=1, minsize=self.width / 5)
        self.columnsTitle.grid_columnconfigure(4, weight=1, minsize=self.width / 5)

        self.nameTitle = CTkLabel(self.columnsTitle, text=self.lang["projectName"])
        self.nameTitle.grid(row=0, column=0)

        self.startDateTitle = CTkLabel(self.columnsTitle, text=self.lang["startDate"])
        self.startDateTitle.grid(row=0, column=1)

        self.endDateTitle = CTkLabel(self.columnsTitle, text=self.lang["endDate"])
        self.endDateTitle.grid(row=0, column=2)

        self.statusTitle = CTkLabel(self.columnsTitle, text=self.lang["status"])
        self.statusTitle.grid(row=0, column=3)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=4)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 5)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 5)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 5)
            self.recordFrame.grid_columnconfigure(3, weight=1, minsize=self.width / 5)
            self.recordFrame.grid_columnconfigure(4, weight=1, minsize=self.width / 5)

            self.nameLabel = CTkLabel(self.recordFrame, text=record.get("name"))
            self.nameLabel.grid(row=0, column=0)

            self.startDateLabel = CTkLabel(self.recordFrame, text=record.get("startDate"))
            self.startDateLabel.grid(row=0, column=1)

            self.endDateLabel = CTkLabel(self.recordFrame, text=record.get("endDate"))
            self.endDateLabel.grid(row=0, column=2)

            self.statusLabel = CTkLabel(self.recordFrame, text=record.get("status"))
            self.statusLabel.grid(row=0, column=3)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["details"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=4)

        self.pack(fill=BOTH, expand=1)

    def createAccountWidgets(self):
        self.title.configure(text=self.lang["accountView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createAccount"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 4)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 4)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 4)
        self.columnsTitle.grid_columnconfigure(3, weight=1, minsize=self.width / 4)

        self.nameTitle = CTkLabel(self.columnsTitle, text=self.lang["accountName"])
        self.nameTitle.grid(row=0, column=0)

        self.balanceTitle = CTkLabel(self.columnsTitle, text=self.lang["balance"])
        self.balanceTitle.grid(row=0, column=1)

        self.numberTitle = CTkLabel(self.columnsTitle, text=self.lang["accountNumber"])
        self.numberTitle.grid(row=0, column=2)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=3)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 4)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 4)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 4)
            self.recordFrame.grid_columnconfigure(3, weight=1, minsize=self.width / 4)

            self.nameLabel = CTkLabel(self.recordFrame, text=record.get("name"))
            self.nameLabel.grid(row=0, column=0)

            self.balanceLabel = CTkLabel(self.recordFrame, text=record.get("balance"))
            self.balanceLabel.grid(row=0, column=1)

            self.numberLabel = CTkLabel(self.recordFrame, text=record.get("accountNumber"))
            self.numberLabel.grid(row=0, column=2)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["details"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=3)

        self.pack(fill=BOTH, expand=1)

    def createInvoiceWidgets(self):
        self.title.configure(text=self.lang["invoiceView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createInvoice"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

        self.numberTitle = CTkLabel(self.columnsTitle, text=self.lang["invoiceNumber"])
        self.numberTitle.grid(row=0, column=0)

        self.dateTitle = CTkLabel(self.columnsTitle, text=self.lang["invoiceDate"])
        self.dateTitle.grid(row=0, column=1)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=2)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

            self.numberLabel = CTkLabel(self.recordFrame, text=record.get("number"))
            self.numberLabel.grid(row=0, column=0)

            self.dateLabel = CTkLabel(self.recordFrame, text=record.get("date"))
            self.dateLabel.grid(row=0, column=1)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["details"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=2)

        self.pack(fill=BOTH, expand=1)

    def createVendorWidgets(self):
        self.title.configure(text=self.lang["vendorView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createVendor"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(3, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(4, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(5, weight=1, minsize=self.width / 7)
        self.columnsTitle.grid_columnconfigure(6, weight=1, minsize=self.width / 7)

        self.nameTitle = CTkLabel(self.columnsTitle, text=self.lang["vendorName"])
        self.nameTitle.grid(row=0, column=0)

        self.postCodeTitle = CTkLabel(self.columnsTitle, text=self.lang["postCode"])
        self.postCodeTitle.grid(row=0, column=1)

        self.cityTitle = CTkLabel(self.columnsTitle, text=self.lang["city"])
        self.cityTitle.grid(row=0, column=2)

        self.streetTitle = CTkLabel(self.columnsTitle, text=self.lang["street"])
        self.streetTitle.grid(row=0, column=3)

        self.nipTitle = CTkLabel(self.columnsTitle, text=self.lang["nip"])
        self.nipTitle.grid(row=0, column=4)

        self.accountTitle = CTkLabel(self.columnsTitle, text=self.lang["accountNumber"])
        self.accountTitle.grid(row=0, column=5)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=6)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(3, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(4, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(5, weight=1, minsize=self.width / 7)
            self.recordFrame.grid_columnconfigure(6, weight=1, minsize=self.width / 7)

            self.nameLabel = CTkLabel(self.recordFrame, text=record.get("name"))
            self.nameLabel.grid(row=0, column=0)

            self.postCodeLabel = CTkLabel(self.recordFrame, text=record.get("postCode"))
            self.postCodeLabel.grid(row=0, column=1)

            self.cityLabel = CTkLabel(self.recordFrame, text=record.get("city"))
            self.cityLabel.grid(row=0, column=2)

            self.streetLabel = CTkLabel(self.recordFrame, text=record.get("street"))
            self.streetLabel.grid(row=0, column=3)

            self.nipLabel = CTkLabel(self.recordFrame, text=record.get("nip"))
            self.nipLabel.grid(row=0, column=4)

            self.accountLabel = CTkLabel(self.recordFrame, text=record.get("accountNumber"))
            self.accountLabel.grid(row=0, column=5)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["details"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=6)

        self.pack(fill=BOTH, expand=1)

    def createTransactionWidgets(self):
        self.title.configure(text=self.lang["transactionView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createTransaction"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 6)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 6)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 6)
        self.columnsTitle.grid_columnconfigure(3, weight=1, minsize=self.width / 6)
        self.columnsTitle.grid_columnconfigure(4, weight=1, minsize=self.width / 6)
        self.columnsTitle.grid_columnconfigure(5, weight=1, minsize=self.width / 6)

        self.idTitle = CTkLabel(self.columnsTitle, text="Id")
        self.idTitle.grid(row=0, column=0)

        self.dateTitle = CTkLabel(self.columnsTitle, text=self.lang["transactionDate"])
        self.dateTitle.grid(row=0, column=1)

        self.titleTitle = CTkLabel(self.columnsTitle, text=self.lang["transactionTitle"])
        self.titleTitle.grid(row=0, column=2)

        self.amountTitle = CTkLabel(self.columnsTitle, text=self.lang["transactionAmount"])
        self.amountTitle.grid(row=0, column=3)

        self.projectTitle = CTkLabel(self.columnsTitle, text=self.lang["transactionProject"])
        self.projectTitle.grid(row=0, column=4)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=5)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 6)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 6)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 6)
            self.recordFrame.grid_columnconfigure(3, weight=1, minsize=self.width / 6)
            self.recordFrame.grid_columnconfigure(4, weight=1, minsize=self.width / 6)
            self.recordFrame.grid_columnconfigure(5, weight=1, minsize=self.width / 6)

            self.idLabel = CTkLabel(self.recordFrame, text=record.get("id"))
            self.idLabel.grid(row=0, column=0)

            self.dateLabel = CTkLabel(self.recordFrame, text=record.get("date"))
            self.dateLabel.grid(row=0, column=1)

            self.titleLabel = CTkLabel(self.recordFrame, text=record.get("title"))
            self.titleLabel.grid(row=0, column=2)

            self.amountLabel = CTkLabel(self.recordFrame, text=record.get("amount"))
            self.amountLabel.grid(row=0, column=3)

            self.projectLabel = CTkLabel(self.recordFrame, text=record.get("project"))
            self.projectLabel.grid(row=0, column=4)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["details"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=5)

        self.pack(fill=BOTH, expand=1)

    def createPermissionWidgets(self):
        self.title.configure(text=self.lang["permissionView"])
        if self.createRecord is not None:
            self.newButton.configure(text=self.lang["createPermission"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

        self.userTitle = CTkLabel(self.columnsTitle, text=self.lang["userName"])
        self.userTitle.grid(row=0, column=0)

        self.projectTitle = CTkLabel(self.columnsTitle, text=self.lang["project"])
        self.projectTitle.grid(row=0, column=1)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=2)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

            self.userLabel = CTkLabel(self.recordFrame, text=record.get("user"))
            self.userLabel.grid(row=0, column=0)

            self.projectLabel = CTkLabel(self.recordFrame, text=record.get("project"))
            self.projectLabel.grid(row=0, column=1)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["delete"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=2)

        self.pack(fill=BOTH, expand=1)

    def createUserWidgets(self):
        self.title.configure(text=self.lang["userView"])

        self.columnsTitle.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
        self.columnsTitle.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

        self.usernameTitle = CTkLabel(self.columnsTitle, text=self.lang["username"])
        self.usernameTitle.grid(row=0, column=0)

        self.isSuperuserTitle = CTkLabel(self.columnsTitle, text=self.lang["isSuperuser"])
        self.isSuperuserTitle.grid(row=0, column=1)

        self.actionsTitle = CTkLabel(self.columnsTitle, text=self.lang["actions"])
        self.actionsTitle.grid(row=0, column=2)

        self.innerFrame = CTkScrollableFrame(self)
        self.innerFrame.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.innerFrame.grid_columnconfigure(0, weight=1)

        for i, record in self.recordData.iterrows():
            self.recordFrame = CTkFrame(self.innerFrame)
            self.recordFrame.grid(row=i, column=0, pady=10, padx=10, sticky="nsew")
            self.recordFrame.grid_columnconfigure(0, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(1, weight=1, minsize=self.width / 3)
            self.recordFrame.grid_columnconfigure(2, weight=1, minsize=self.width / 3)

            self.usernameLabel = CTkLabel(self.recordFrame, text=record.get("username"))
            self.usernameLabel.grid(row=0, column=0)

            self.isSuperuserLabel = CTkLabel(self.recordFrame, text=record.get("isSuperuser"))
            self.isSuperuserLabel.grid(row=0, column=1)

            self.editButton = CTkButton(self.recordFrame, text=self.lang["givePermission"], command=lambda: self.action(record))
            self.editButton.grid(row=0, column=2)

        self.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
    root.grid_columnconfigure(0, weight=1, minsize=root.winfo_screenwidth())
    root.grid_rowconfigure(0, weight=1)

    data = pd.read_csv("projects.csv")

    view = RecordView(root, "user", data, lambda: print("Go back"), lambda: print("Create record"), lambda: print("Details"))
    view.grid(row=0, column=0, sticky="nsew")
    root.mainloop()