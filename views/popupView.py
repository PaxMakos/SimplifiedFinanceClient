import customtkinter


class PopupView(customtkinter.CTkToplevel):
    def __init__(self, master, message):
        super().__init__(master)
        self.message = message
        self.geometry("300x100")

        self.createWidgets()
        self.focus()
        self.grab_set()

    def createWidgets(self):
        self.label = customtkinter.CTkLabel(self, text=self.message)
        self.button = customtkinter.CTkButton(self, text="Close", command=self.destroy)

        self.label.grid(row=0, column=0, padx=10, pady=10)
        self.button.grid(row=1, column=0, padx=10, pady=10)

        self.grid_columnconfigure(0, weight=1)



if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")

    view = PopupView(root, "This is a popup view")
    root.mainloop()