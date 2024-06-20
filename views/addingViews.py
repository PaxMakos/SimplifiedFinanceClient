from customtkinter import *
import customtkinter
import json


class AddAccount(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createAccount"], font=("Arial", 20))

        self.nameLabel = CTkLabel(self, text=lang["accountName"])
        self.nameEntry = CTkEntry(self)

        self.balanceLabel = CTkLabel(self, text=lang["accountBalance"])
        self.balanceEntry = CTkEntry(self)

        self.numberLabel = CTkLabel(self, text=lang["accountNumber"])
        self.numberEntry = CTkEntry(self)

        self.createButton = CTkButton(self, text=lang["createAccount"], command=self.createFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.nameLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.nameEntry.grid(row=1, column=1, pady=10, padx=10)
        self.balanceLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.balanceEntry.grid(row=2, column=1, pady=10, padx=10)
        self.numberLabel.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.numberEntry.grid(row=3, column=1, pady=10, padx=10)
        self.createButton.grid(row=4, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=4, column=1, pady=10, padx=10)

        #self.pack()


class AddInvoice(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createInvoice"], font=("Arial", 20))

        self.numberLabel = CTkLabel(self, text=lang["invoiceNumber"])
        self.numberEntry = CTkEntry(self)

        self.dateLabel = CTkLabel(self, text=lang["invoiceDate"])
        self.dateEntry = CTkEntry(self)

        self.descriptionLabel = CTkLabel(self, text=lang["invoiceDescription"])
        self.descriptionEntry = CTkEntry(self)

        self.pickFileLabel = CTkLabel(self, text=lang["invoiceFile"])
        self.pickFileButton = CTkButton(self, text=lang["pickFileButton"], command=self.pickFile)

        self.createButton = CTkButton(self, text=lang["createInvoice"], command=self.returnFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.numberLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.numberEntry.grid(row=1, column=1, pady=10, padx=10)
        self.dateLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.dateEntry.grid(row=2, column=1, pady=10, padx=10)
        self.descriptionLabel.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.descriptionEntry.grid(row=3, column=1, pady=10, padx=10)
        self.pickFileLabel.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.pickFileButton.grid(row=4, column=1, pady=10, padx=10)
        self.createButton.grid(row=5, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=5, column=1, pady=10, padx=10)

        #self.pack()

    def pickFile(self):
        self.filePath = filedialog.askopenfilename()
        self.pickFileButton.configure(text=self.filePath.split("/")[-1])

    def returnFunc(self):
        self.createFunc(self.filePath)


class AddProject(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createProject"], font=("Arial", 20))

        self.nameLabel = CTkLabel(self, text=lang["projectName"])
        self.nameEntry = CTkEntry(self)

        self.descriptionLabel = CTkLabel(self, text=lang["projectDescription"])
        self.descriptionEntry = CTkEntry(self)

        self.startLabel = CTkLabel(self, text=lang["projectStart"])
        self.startEntry = CTkEntry(self)

        self.endLabel = CTkLabel(self, text=lang["projectEnd"])
        self.endEntry = CTkEntry(self)

        self.statusLabel = CTkLabel(self, text=lang["projectStatus"])
        self.statusEntry = CTkEntry(self)

        self.createButton = CTkButton(self, text=lang["createProject"], command=self.createFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.nameLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.nameEntry.grid(row=1, column=1, pady=10, padx=10)
        self.descriptionLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.descriptionEntry.grid(row=2, column=1, pady=10, padx=10)
        self.startLabel.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.startEntry.grid(row=3, column=1, pady=10, padx=10)
        self.endLabel.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.endEntry.grid(row=4, column=1, pady=10, padx=10)
        self.statusLabel.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.statusEntry.grid(row=5, column=1, pady=10, padx=10)
        self.createButton.grid(row=6, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=6, column=1, pady=10, padx=10)

        #self.pack()


class AddTransaction(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createTransaction"], font=("Arial", 20))

        self.dateLabel = CTkLabel(self, text=lang["transactionDate"])
        self.dateEntry = CTkEntry(self)

        self.titleLabel = CTkLabel(self, text=lang["transactionTitle"])
        self.titleEntry = CTkEntry(self)

        self.amountLabel = CTkLabel(self, text=lang["transactionAmount"])
        self.amountEntry = CTkEntry(self)

        self.descriptionLabel = CTkLabel(self, text=lang["transactionDescription"])
        self.descriptionEntry = CTkEntry(self)

        self.accountLabel = CTkLabel(self, text=lang["transactionAccount"])
        self.accountEntry = CTkEntry(self)

        self.vendorLabel = CTkLabel(self, text=lang["transactionVendor"])
        self.vendorEntry = CTkEntry(self)

        self.projectLabel = CTkLabel(self, text=lang["transactionProject"])
        self.projectEntry = CTkEntry(self)

        self.invoiceLabel = CTkLabel(self, text=lang["invoiceNumber"])
        self.invoiceEntry = CTkEntry(self)

        self.createButton = CTkButton(self, text=lang["createTransaction"], command=self.createFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.titleLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.titleEntry.grid(row=1, column=1, pady=10, padx=10)
        self.dateLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.dateEntry.grid(row=2, column=1, pady=10, padx=10)
        self.amountLabel.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.amountEntry.grid(row=3, column=1, pady=10, padx=10)
        self.descriptionLabel.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.descriptionEntry.grid(row=4, column=1, pady=10, padx=10)
        self.accountLabel.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.accountEntry.grid(row=5, column=1, pady=10, padx=10)
        self.vendorLabel.grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.vendorEntry.grid(row=6, column=1, pady=10, padx=10)
        self.projectLabel.grid(row=7, column=0, pady=10, padx=10, sticky="w")
        self.projectEntry.grid(row=7, column=1, pady=10, padx=10)
        self.invoiceLabel.grid(row=8, column=0, pady=10, padx=10, sticky="w")
        self.invoiceEntry.grid(row=8, column=1, pady=10, padx=10)
        self.createButton.grid(row=9, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=9, column=1, pady=10, padx=10)

        #self.pack()


class AddVendor(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createVendor"], font=("Arial", 20))

        self.nameLabel = CTkLabel(self, text=lang["vendorName"])
        self.nameEntry = CTkEntry(self)

        self.postcodeLabel = CTkLabel(self, text=lang["vendorPostcode"])
        self.postcodeEntry = CTkEntry(self)

        self.cityLabel = CTkLabel(self, text=lang["vendorCity"])
        self.cityEntry = CTkEntry(self)

        self.streetLabel = CTkLabel(self, text=lang["vendorStreet"])
        self.streetEntry = CTkEntry(self)

        self.nipNumberLabel = CTkLabel(self, text=lang["nip"])
        self.nipNumberEntry = CTkEntry(self)

        self.accountNumberLabel = CTkLabel(self, text=lang["accountNumber"])
        self.accountNumberEntry = CTkEntry(self)

        self.createButton = CTkButton(self, text=lang["createVendor"], command=self.createFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.nameLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.nameEntry.grid(row=1, column=1, pady=10, padx=10)
        self.postcodeLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.postcodeEntry.grid(row=2, column=1, pady=10, padx=10)
        self.cityLabel.grid(row=3, column=0, pady=10, padx=10, sticky="w")
        self.cityEntry.grid(row=3, column=1, pady=10, padx=10)
        self.streetLabel.grid(row=4, column=0, pady=10, padx=10, sticky="w")
        self.streetEntry.grid(row=4, column=1, pady=10, padx=10)
        self.nipNumberLabel.grid(row=5, column=0, pady=10, padx=10, sticky="w")
        self.nipNumberEntry.grid(row=5, column=1, pady=10, padx=10)
        self.accountNumberLabel.grid(row=6, column=0, pady=10, padx=10, sticky="w")
        self.accountNumberEntry.grid(row=6, column=1, pady=10, padx=10)
        self.createButton.grid(row=7, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=7, column=1, pady=10, padx=10)

        #self.pack()


class AddPermission(CTkFrame):
    def __init__(self, master, createFunc, goBackFunc):
        super().__init__(master)
        self.createFunc = createFunc
        self.goBackFunc = goBackFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["createPermission"], font=("Arial", 20))

        self.usernameLabel = CTkLabel(self, text=lang["permissionUsername"])
        self.usernameEntry = CTkEntry(self)

        self.projectLabel = CTkLabel(self, text=lang["permissionProject"])
        self.projectEntry = CTkEntry(self)

        self.createButton = CTkButton(self, text=lang["createPermission"], command=self.createFunc)
        self.cancelButton = CTkButton(self, text=lang["goBackButton"], command=self.goBackFunc)

        self.title.grid(row=0, column=0, columnspan=2, pady=20)
        self.usernameLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")
        self.usernameEntry.grid(row=1, column=1, pady=10, padx=10)
        self.projectLabel.grid(row=2, column=0, pady=10, padx=10, sticky="w")
        self.projectEntry.grid(row=2, column=1, pady=10, padx=10)
        self.createButton.grid(row=3, column=0, pady=10, padx=10)
        self.cancelButton.grid(row=3, column=1, pady=10, padx=10)

        #self.pack()


if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")

    view = AddPermission(root, lambda: print("Invoice created"), lambda: print("Go back"))
    root.mainloop()
