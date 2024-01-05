from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip as pc
import json

#  ---------------------------- SEARCH GENERATOR ------------------------------- #

def search():
    print("Search button clicked")
    website = website_entry.get()
    website = website.lower()

    with open(file="data.json" , mode="r") as file:
        data = json.load(file)
        data_key = [key for key in data]
        data_value = [data[key]["password"] for key in data]
        for i in range(len(data_key)):
            data_key[i] = data_key[i].lower()
            if(data_key[i] == website):
                
                password = data_value[i]
                pc.copy(password)
                password_entry.insert(0,password )
        
        if(len(password_entry.get()) == 0):
            password_entry.insert(0,"Sorry website not found" )
            


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    print("Genrate button clicked")
    all_letters = list(string.ascii_lowercase + string.ascii_uppercase)

    # Create empty lists for symbols and numbers
    symbols = []
    numbers = []

    # Define symbols and numbers
    symbols_string = "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?`~"
    numbers_string = "0123456789"

    # Populate symbols and numbers lists
    for char in symbols_string:
        symbols.append(char)

    for num in numbers_string:
        numbers.append(num)

    passwords = []


    for i in range(5):
        passwords.append(random.choice(all_letters))

    for i in range(3):
        passwords.append(random.choice(numbers))

    for i in range(3):
        passwords.append(random.choice(symbols))

    random.shuffle(passwords)

    result = ""

    for key in passwords:

        result = result + key

    pc.copy(result)

    password_entry.insert(0 , result)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_click():
    print("Add button clicked")

    web = website_entry.get()
    email_address = email_entry.get()
    password_save = password_entry.get()
    new_data = {
        web: {
            "email": email_address,
            "password": password_save,
        }
    }

    if(len(web) == 0 or len(email_address) == 0 or len(password_save) == 0):
        messagebox.showinfo(title="Missing feilds" , message="Please do not leave any feild empty")
    else:
        id_ok = messagebox.askokcancel(title=web , message=f"You have entered {email_address} as your email \nAnd {password_save} as your password\nDo you want to save it?")
        if id_ok:
            try:

                with open(file="data.json" , mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
                
                with open(file="data.json" , mode="w") as data_file:
                    json.dump(data , data_file , indent=4)
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)
            except FileNotFoundError:
                
                with open(file="data.json" , mode="w") as data_file:
                    json.dump(new_data , data_file , indent=4)
                    website_entry.delete(0,END)
                    password_entry.delete(0,END)

                


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50 , padx=50 )
window.title("Password Gen") 
# window.minsize(width=500 , height=500)



canva = Canvas(width=200 , height=200)
logo = PhotoImage(file="logo.png")
canva.create_image(100 , 100 , image = logo)
canva.grid(column=1 , row=0)

website_label = Label(text="Website:")
website_label.grid(row=1 , column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

add = Button(text="Add" , width=36 , command=add_button_click)
add.grid(row=4 , column=1, columnspan=2)
gen = Button(text="Genrate Password" , command=pass_gen)
gen.grid(row=3 ,column=2, columnspan=2)
search = Button(text="Search" ,command=search ,width=10)
search.grid(row = 1 ,column=2, columnspan=2)

website_entry = Entry(width=25)
website_entry.grid(row=1 , column=1 )
website_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0 , "ayushnamin@gmail.com")
email_entry.grid(row=2 ,column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3 , column=1)



window.mainloop()


