from customtkinter import *
import customtkinter
import json

class AddReturnView(CTkFrame):
    def __init__(self, master, returnFunc, backFunc):
        super().__init__(master)
        self.returnFunc = returnFunc
        self.backFunc = backFunc
        self.filePath = None
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))
        self.grid_columnconfigure(1, minsize=300)

        self.title = CTkLabel(self, text=lang["addReturnTitle"], font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        CTkLabel(self, text=lang["projectName"]).grid(row=1, column=0, padx=40, pady=10, sticky="w")
        self.projectNameEntry = CTkEntry(self)
        self.projectNameEntry.grid(row=1, column=1, pady=10)

        CTkLabel(self, text=lang["returnTitle"]).grid(row=2, column=0, padx=40, pady=10, sticky="w")
        self.returnTitleEntry = CTkEntry(self)
        self.returnTitleEntry.grid(row=2, column=1, pady=10)

        CTkLabel(self, text=lang["returnDate"]).grid(row=3, column=0, padx=40, pady=10, sticky="w")
        self.returnDateEntry = CTkEntry(self)
        self.returnDateEntry.grid(row=3, column=1, pady=10)

        CTkLabel(self, text=lang["returnAmount"]).grid(row=4, column=0, padx=40, pady=10, sticky="w")
        self.returnAmountEntry = CTkEntry(self)
        self.returnAmountEntry.grid(row=4, column=1, pady=10)

        CTkLabel(self, text=lang["returnDescription"]).grid(row=5, column=0, padx=40, pady=10, sticky="w")
        self.returnDescriptionEntry = CTkEntry(self)
        self.returnDescriptionEntry.grid(row=5, column=1, pady=10)

        CTkLabel(self, text=lang["accountToReturn"]).grid(row=6, column=0, padx=40, pady=10, sticky="w")
        self.accountToReturnEntry = CTkEntry(self)
        self.accountToReturnEntry.grid(row=6, column=1, pady=10)

        CTkLabel(self, text=lang["invoiceFile"]).grid(row=7, column=0, padx=40, pady=10, sticky="w")
        self.pickFileButton = CTkButton(self, text=lang["pickFileButton"], command=self.pickFile)
        self.pickFileButton.grid(row=7, column=1, pady=10)

        self.returnButton = CTkButton(self, text=lang["addReturnButton"], command=self.sendReturn)
        self.returnButton.grid(row=8, column=1, pady=20)

        self.backButton = CTkButton(self, text=lang["goBackButton"], command=self.backFunc)
        self.backButton.grid(row=8, column=0, pady=20)

    def pickFile(self):
        self.filePath = filedialog.askopenfilename()
        self.pickFileButton.configure(text=self.filePath.split("/")[-1])

    def sendReturn(self):
        self.returnFunc(self.filePath)


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")

    view = AddReturnView(root, lambda: print("Return"), lambda: print("Back"))
    root.mainloop()