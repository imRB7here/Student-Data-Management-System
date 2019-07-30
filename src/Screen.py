from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Utilities import GUIPicker


class Screen(ttk.Frame):
    def __init__(self, root, callback):
        # Configure the Parent Window
        self._master = root
        super().__init__(self._master)

        self._gui_picker = GUIPicker(self)
        self._data_return_callback = callback

    def draw(self):
        # Draws the widgets
        self.place(relx=0, rely=0, relwidth=1, relheight=1)

    def screenActionHandler(self, action_code):
        pass

    def hide(self):
        self.pack_forget()

    def clean(self):
        self.destroy()


class MainmenuScreen(Screen):
    # Path for Images
    main_logo_path = 'assets\images\main_icon.png'
    search_icon_path = 'assets\images\search_icon.png'
    add_icon_normal_path = 'assets\images\\add_icon_normal.png'
    add_icon_mouseover_path = 'assets\images\\add_icon_mouseover.png'
    modify_icon_normal_path = 'assets\images\modify_icon_normal.png'
    modify_icon_mouseover_path = 'assets\images\modify_icon_mouseover.png'
    delete_icon_normal_path = 'assets\images\delete_icon_normal.png'
    delete_icon_mouseover_path = 'assets\images\delete_icon_mouseover.png'
    exit_icon_normal_path = 'assets\images\exit_icon_normal.png'
    exit_icon_mouseover_path = 'assets\images\exit_icon_mouseover.png'

    # Useful Values Tuples
    search_type_combobox_values = (
        'Roll Number', 'Name', 'Year of Joining')
    onscreen_actions = ('SEARCH', 'ADD', 'MODIFY', 'DELETE', 'EXIT')

    def __init__(self, root, callback):
        super().__init__(root, callback)

        # Main Logo
        self.__main_logo_image = self._gui_picker.pickImage(
            MainmenuScreen.main_logo_path)
        self.__main_logo_label = self._gui_picker.pickImageLabel(
            self.__main_logo_image)

        # Search Entry
        self.__search_entry_textvar = StringVar(None,'Enter Roll No here')
        self.__search_entry = self._gui_picker.pickEntry(
            self.__search_entry_textvar)
        self.__search_entry.configure(
            font=("Helvetica", "12", "bold"), textvariable=self.__search_entry_textvar, justify=CENTER)

        def searchEntryCallback():
            self.__search_entry_textvar.set('')
            self.__search_entry.configure(foreground='black')
        self.__search_entry.bind(
            "<Button-1>", lambda e: searchEntryCallback())

        # Search Type Combobox
        self.__search_type_textvar = StringVar(
            None, MainmenuScreen.search_type_combobox_values[0])
        self.__search_type_combobox = self._gui_picker.pickCombobox(
            MainmenuScreen.search_type_combobox_values, self.__search_type_textvar)
        self.__search_type_combobox.configure(background='#660066', foreground='black', font=(
            "Helvetica", "10", "bold"), justify=CENTER)
        def searchtypeComboboxSelectedCallback():
            self.__search_entry_textvar.set(
                'Enter '+self.__search_type_textvar.get()+' here')
            self.__search_entry.configure(foreground='grey')
        self.__search_type_combobox.bind(
            '<<ComboboxSelected>>', lambda e: searchtypeComboboxSelectedCallback() )

        # Search Button
        self.__search_button_image = self._gui_picker.pickImage(
            MainmenuScreen.search_icon_path)
        self.__search_button = self._gui_picker.pickImageButton(
            self.__search_button_image)
        self.__search_button.bind(
            '<Button-1>', lambda e: self.screenActionHandler(MainmenuScreen.onscreen_actions[0]))

        # Add Button
        self.__add_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.add_icon_normal_path)
        self.__add_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.add_icon_mouseover_path)
        self.__add_button = self._gui_picker.pickImageButton(
            self.__add_button_image_normal)
        self.__add_button.bind('<Enter>', lambda e: self.__add_button.configure(
            image=self.__add_button_image_mouseover))
        self.__add_button.bind('<Leave>', lambda e: self.__add_button.configure(
            image=self.__add_button_image_normal))
        self.__add_button.bind(
            '<Button-1>', lambda e: self.screenActionHandler(MainmenuScreen.onscreen_actions[1]))

        # Modify Button
        self.__modify_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.modify_icon_normal_path)
        self.__modify_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.modify_icon_mouseover_path)
        self.__modify_button = self._gui_picker.pickImageButton(
            self.__modify_button_image_normal)
        self.__modify_button.bind('<Enter>', lambda e: self.__modify_button.configure(
            image=self.__modify_button_image_mouseover))
        self.__modify_button.bind('<Leave>', lambda e: self.__modify_button.configure(
            image=self.__modify_button_image_normal))
        self.__modify_button.bind(
            '<Button-1>', lambda e: self.screenActionHandler(MainmenuScreen.onscreen_actions[2]))

        # Delete Button
        self.__delete_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.delete_icon_normal_path)
        self.__delete_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.delete_icon_mouseover_path)
        self.__delete_button = self._gui_picker.pickImageButton(
            self.__delete_button_image_normal)
        self.__delete_button.bind('<Enter>', lambda e: self.__delete_button.configure(
            image=self.__delete_button_image_mouseover))
        self.__delete_button.bind('<Leave>', lambda e: self.__delete_button.configure(
            image=self.__delete_button_image_normal))
        self.__delete_button.bind(
            '<Button-1>', lambda e: self.screenActionHandler(MainmenuScreen.onscreen_actions[3]))

        # Exit Button
        self.__exit_button_image_normal = self._gui_picker.pickImage(
            MainmenuScreen.exit_icon_normal_path)
        self.__exit_button_image_mouseover = self._gui_picker.pickImage(
            MainmenuScreen.exit_icon_mouseover_path)
        self.__exit_button = self._gui_picker.pickImageButton(
            self.__exit_button_image_normal)
        self.__exit_button.bind('<Enter>', lambda e: self.__exit_button.configure(
            image=self.__exit_button_image_mouseover))
        self.__exit_button.bind('<Leave>', lambda e: self.__exit_button.configure(
            image=self.__exit_button_image_normal))
        self.__exit_button.bind(
            '<Button-1>', lambda e: self.screenActionHandler(MainmenuScreen.onscreen_actions[4]))

    def screenActionHandler(self, action_code):
        data_to_send = ['MAINMENU_SCREEN']
        if action_code is MainmenuScreen.onscreen_actions[0]:
            data_to_send.append('SEARCH')
            search_type=self.__search_type_textvar.get()
            search_entry=self.__search_entry_textvar.get()
            if search_entry is not '':
                if search_type in MainmenuScreen.search_type_combobox_values:
                    if search_type == MainmenuScreen.search_type_combobox_values[0] or search_type == MainmenuScreen.search_type_combobox_values[2]:
                        try:
                            temp_var=int(search_entry)
                        except ValueError:
                            messagebox.showerror(
                                'Invalid '+search_type, search_type+' must be in Digits only')
                            return None
                    data_to_send.append((search_type,search_entry))
                    self._data_return_callback(data_to_send)
                else:
                    messagebox.showerror('Invalid Query','Search type is not valid')
        elif action_code is MainmenuScreen.onscreen_actions[1]:
            data_to_send.append('ADD')
            self._data_return_callback(data_to_send)
        elif action_code is MainmenuScreen.onscreen_actions[2]:
            data_to_send.append('MODIFY')
            self._data_return_callback(data_to_send)
        elif action_code is MainmenuScreen.onscreen_actions[3]:
            data_to_send.append('DELETE')
            self._data_return_callback(data_to_send)
        elif action_code is MainmenuScreen.onscreen_actions[4]:
            data_to_send.append('EXIT')
            self._data_return_callback(data_to_send)

        

    def draw(self):
        # Main Logo
        self.__main_logo_label.place(
            relx=0.3, rely=0.02, relheight=0.45, relwidth=.5)

        # Search Type Spinbox
        self.__search_type_combobox.place(
            relx=0.16, rely=0.55, relheight=0.06, relwidth=0.16)

        # Search Entry
        self.__search_entry.place(
            relx=0.33, rely=0.55, relheight=0.06, relwidth=.44)

        # Search Button
        self.__search_button.place(
            relx=0.77, rely=0.55, relheight=0.06, relwidth=0.05)

        # Add Button
        self.__add_button.place(relx=0.05, rely=0.7,
                                relheight=0.193, relwidth=.13)

        # Modify Button
        self.__modify_button.place(
            relx=0.3, rely=0.7, relheight=0.193, relwidth=.13)

        # Delete Button
        self.__delete_button.place(
            relx=0.57, rely=0.7, relheight=0.193, relwidth=.13)

        # Exit Button
        self.__exit_button.place(relx=0.81, rely=0.7,
                                 relheight=0.193, relwidth=.13)

        super().draw()

class AddDataScreen(Screen):
    # Images path
    submit_icon_normal_path='assets\images\submit_icon_normal.png'
    reset_icon_normal_path='assets\images\\reset_icon_normal.png'
    cancel_icon_normal_path = 'assets\images\cancel_icon_normal.png'

    def __init__(self, root, callback):
        super().__init__(root, callback)

        # Cancel Button
        self.__cancel_button_image_normal=self._gui_picker.pickImage(AddDataScreen.cancel_icon_normal_path)
        self.__cancel_button=self._gui_picker.pickImageButton(self.__cancel_button_image_normal)

        # Submit  Button
        self.__submit_button_image_normal = self._gui_picker.pickImage(
            AddDataScreen.submit_icon_normal_path)
        self.__submit_button = self._gui_picker.pickImageButton(
            self.__submit_button_image_normal)

        # Reset Button
        self.__reset_button_image_normal = self._gui_picker.pickImage(
            AddDataScreen.reset_icon_normal_path)
        self.__reset_button = self._gui_picker.pickImageButton(
            self.__reset_button_image_normal)

    def draw(self):
        # Cancel Button
        self.__cancel_button.place(relx=0.2,rely=0.01,relwidth=0.07,relheight=0.09)

        # Submit Button
        self.__submit_button.place(relx=0.8-0.07,rely=0.01,relwidth=0.07,relheight=0.09)

        # Reset Button
        self.__reset_button.place(
            relx=0.465, rely=0.01, relwidth=0.07, relheight=0.09)

        super().draw()    

if __name__ == "__main__":
    print('Performing Test in Screen Module\n')

    temp_window = Tk()
    temp_window.geometry('800x600')
    temp_window.resizable(False, False)

    def tempcall(data):
        print(data)

    test_screen = AddDataScreen(temp_window, tempcall)
    test_screen.draw()
    temp_window.mainloop()
