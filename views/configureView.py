from customtkinter import *
import customtkinter
import json


class ConfigView(CTkFrame):
    def __init__(self, master, nextFunc):
        super().__init__(master)
        self.nextFunc = nextFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, minsize=300)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, minsize=320)


        self.title = CTkLabel(self, text=lang["configTitle"], font=("Arial", 20))
        self.title.grid(row=0, column=1, columnspan=2, pady=20)

        self.organisationLabel = CTkLabel(self, text=lang["organisation"])
        self.organisationLabel.grid(row=1, column=0, pady=10, padx=40, sticky="w")

        self.organisationEntry = CTkEntry(self)
        self.organisationEntry.grid(row=1, column=1, pady=10, sticky="ew")

        self.nipLabel = CTkLabel(self, text=lang["nip"])
        self.nipLabel.grid(row=2, column=0, pady=10, padx=40, sticky="w")

        self.nipEntry = CTkEntry(self)
        self.nipEntry.grid(row=2, column=1, pady=10, sticky="ew")

        self.accountNumberLabel = CTkLabel(self, text=lang["accountNumber"])
        self.accountNumberLabel.grid(row=3, column=0, pady=10, padx=40, sticky="w")

        self.accountNumberEntry = CTkEntry(self)
        self.accountNumberEntry.grid(row=3, column=1, pady=10, sticky="ew")

        self.accountBalanceLabel = CTkLabel(self, text=lang["accountBalance"])
        self.accountBalanceLabel.grid(row=4, column=0, pady=10, padx=40, sticky="w")

        self.accountBalanceEntry = CTkEntry(self)
        self.accountBalanceEntry.grid(row=4, column=1, pady=10, sticky="ew")

        self.treasurerLabel = CTkLabel(self, text=lang["treasurer"])
        self.treasurerLabel.grid(row=5, column=0, pady=10, padx=40, sticky="w")

        self.treasurerEntry = CTkEntry(self)
        self.treasurerEntry.grid(row=5, column=1, pady=10, sticky="ew")

        self.streetLabel = CTkLabel(self, text=lang["street"])
        self.streetLabel.grid(row=1, column=2, pady=10, padx=40, sticky="w")

        self.streetEntry = CTkEntry(self)
        self.streetEntry.grid(row=1, column=3, pady=10, padx=10, sticky="ew")

        self.postCodeLabel = CTkLabel(self, text=lang["postCode"])
        self.postCodeLabel.grid(row=2, column=2, pady=10, padx=40, sticky="w")

        self.postCodeEntry = CTkEntry(self)
        self.postCodeEntry.grid(row=2, column=3, pady=10, padx=10, sticky="ew")

        self.cityLabel = CTkLabel(self, text=lang["city"])
        self.cityLabel.grid(row=3, column=2, pady=10, padx=40, sticky="w")

        self.cityEntry = CTkEntry(self)
        self.cityEntry.grid(row=3, column=3, pady=10, padx=10, sticky="ew")

        self.usernameLabel = CTkLabel(self, text=lang["username"])
        self.usernameLabel.grid(row=5, column=2, pady=10, padx=40, sticky="w")

        self.usernameEntry = CTkEntry(self)
        self.usernameEntry.grid(row=5, column=3, pady=10, padx=10, sticky="ew")

        self.passwordLabel = CTkLabel(self, text=lang["password"])
        self.passwordLabel.grid(row=6, column=0, pady=10, padx=40, sticky="w")

        self.passwordEntry = CTkEntry(self, show="*")
        self.passwordEntry.grid(row=6, column=1, pady=10, sticky="ew")

        self.passwordLabel = CTkLabel(self, text=lang["confirmPassword"])
        self.passwordLabel.grid(row=6, column=2, pady=10, padx=40, sticky="w")

        self.passwordConfigEntry = CTkEntry(self, show="*")
        self.passwordConfigEntry.grid(row=6, column=3, pady=10, padx=10, sticky="ew")

        self.nextButton = CTkButton(self, text=lang["nextButton"], command=self.nextFunc)
        self.nextButton.grid(row=7, column=1, pady=10, padx=10, columnspan=2)

        self.pack()


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")

    view = ConfigView(root, lambda: print("Save"))
    root.mainloop()