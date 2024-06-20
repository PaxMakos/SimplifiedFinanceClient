from customtkinter import *
import customtkinter
import json


class Register(CTkFrame):
    def __init__(self, master, registerFunc, returnFunc, registerData=None):
        super().__init__(master)
        self.registerFunc = registerFunc
        self.returnFunc = returnFunc
        self.registerData = registerData
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["registerTitle"], font=("Arial", 20))
        self.title.grid(row=0, column=0, columnspan=2, pady=20)

        self.usernameLabel = CTkLabel(self, text=lang["username"])
        self.usernameLabel.grid(row=1, column=0, columnspan=2, pady=10)

        self.usernameEntry = CTkEntry(self)
        self.usernameEntry.grid(row=2, column=0, columnspan=2, pady=10)

        self.passwordLabel = CTkLabel(self, text=lang["password"])
        self.passwordLabel.grid(row=3, column=0, columnspan=2, pady=10)

        self.passwordEntry = CTkEntry(self, show="*")
        self.passwordEntry.grid(row=4, column=0, columnspan=2, pady=10)

        self.passwordLabel = CTkLabel(self, text=lang["confirmPassword"])
        self.passwordLabel.grid(row=5, column=0, columnspan=2, pady=10)

        self.passwordConfirmEntry = CTkEntry(self, show="*")
        self.passwordConfirmEntry.grid(row=6, column=0, columnspan=2, pady=10)

        self.registerButton = CTkButton(self, text=lang["registerButton"], command=self.registerFunc)
        self.registerButton.grid(row=7, column=0, pady=10, padx=10, sticky="e")

        self.returnButton = CTkButton(self, text=lang['returnButton'], command=self.returnFunc)
        self.returnButton.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        self.pack()


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")

    view = Register(root, lambda: print("Register"), lambda: print("Return"))
    root.mainloop()