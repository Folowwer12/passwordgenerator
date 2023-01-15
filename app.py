import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import customtkinter as ct
from PIL import Image

import password as pw


class App(ct.CTk):

    def __init__(self):

        super().__init__()

        self._set_appearance_mode("System")
        self.geometry('460x370')
        self.title("Password Generator")
        self.resizable(False, False)

        self.logo = ct.CTkImage(dark_image=Image.open(
            'src/logo.png'), size=(460, 150))
        self.logo_label = ct.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = ct.CTkFrame(master=self, fg_color='transparent')
        self.password_frame.grid(row=1, column=0, padx=(20, 20), sticky='nsew')

        self.entry_password = ct.CTkEntry(
            master=self.password_frame, width=300)
        self.entry_password.grid(row=0, column=0, padx=(0, 20))

        self.btn_generate = ct.CTkButton(
            master=self.password_frame, text='Generate', width=100, command=self.generate_password)
        self.btn_generate.grid(row=0, column=1)

        self.settings_frame = ct.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(
            20, 0), pady=(20, 0), sticky='nsew')

        self.password_length = ct.CTkSlider(
            master=self.settings_frame, from_=0, to=100, number_of_steps=100, command=self.slider_event)
        self.password_length.grid(
            row=1, column=0, columnspan=3, pady=(20, 20), sticky='ew')

        self.password_length_entry = ct.CTkEntry(
            master=self.settings_frame, width=50)
        self.password_length_entry.grid(
            row=1, column=3, padx=(20, 10), sticky='we')

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = ct.CTkCheckBox(
            master=self.settings_frame, text='0-9', variable=self.cb_digits_var, onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = ct.CTkCheckBox(master=self.settings_frame, text='a-z',
                                       variable=self.cb_lower_var, onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = ct.CTkCheckBox(master=self.settings_frame, text='A-Z',
                                       variable=self.cb_upper_var, onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbols_var = tkinter.StringVar()
        self.cb_symbols = ct.CTkCheckBox(
            master=self.settings_frame, text='@#$%', variable=self.cb_symbols_var, onvalue=punctuation, offvalue="")
        self.cb_symbols.grid(row=2, column=3)

        self.apperance_mode = ct.CTkOptionMenu(master=self.settings_frame, values=[
                                               'Light', 'Dark', 'System'], command=self.change_app_mode)
        self.apperance_mode.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.password_length.set(12)
        self.password_length_entry.insert(0, 12)
        self.apperance_mode.set("System")

    def change_app_mode(self, new_mode):
        ct.set_appearance_mode(new_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_upper_var.get() +
                        self.cb_lower_var.get() + self.cb_symbols_var.get())

        return chars

    def generate_password(self):
        try:
            self.entry_password.delete(0, 'end')
            self.entry_password.insert(0, pw.generate(
                characters=self.get_characters(), length=int(self.password_length.get())))
        except:
            pass

    def slider_event(self, value):
        self.password_length_entry.delete(0, 'end')
        self.password_length_entry.insert(0, int(value))


if __name__ == '__main__':
    app = App()
    app.mainloop()
