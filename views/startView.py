from customtkinter import *
import customtkinter
import json


class StartView(CTkFrame):
    def __init__(self, master, loginFunc, registerFunc, returnFunc):
        super().__init__(master)
        self.loginFunc = loginFunc
        self.registerFunc = registerFunc
        self.returnFunc = returnFunc
        self.createWidgets()

    def createWidgets(self):
        lang = json.load(open("language.json", "r", encoding="utf-8"))

        self.title = CTkLabel(self, text=lang["startTitle"], font=("Arial", 20))
        self.title.pack(pady=20)

        self.loginButton = CTkButton(self, text=lang["loginButton"], command=self.loginFunc, height=100, width=100)
        self.registerButton = CTkButton(self, text=lang["signupButton"], command=self.registerFunc, height=100, width=100)
        self.returnButton = CTkButton(self, text=lang['moneyReturnButton'], command=self.returnFunc, height=100, width=100)

        self.loginButton.pack(side='left', pady=10, padx=10)
        self.registerButton.pack(side='left', pady=10, padx=10)
        self.returnButton.pack(side='left', pady=10, padx=10)

        self.pack()


if __name__ == "__main__":
    root = CTk()
    customtkinter.set_appearance_mode("dark")

    view = StartView(root, lambda: print("Login"), lambda: print("Register"), lambda: print("Return"))
    root.mainloop()