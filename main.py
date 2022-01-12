from tkinter import *
from tkinter import messagebox
import pyperclip as pc
import random
BG_COLOR = "#071e26"
RED = "#d4483b"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passgen():
    password_box.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    ltrs = random.randint(4,10)
    smbls= random.randint(2,4)
    nums = random.randint(2,7)
    for char in range(1, ltrs + 1):
        password_list.append(random.choice(letters))

    for char in range(1, smbls + 1):
        password_list += random.choice(symbols)

    for char in range(1, nums + 1):
        password_list += random.choice(numbers)


    random.shuffle(password_list)
    password = "".join(password_list)
    password_box.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_box.get()
    user = username_box.get()
    password = password_box.get()

    if website == "" or user == "" or password == "":
        messagebox.showerror(title="Error",message="Please fill all the info required")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"Infos entered: \nEmail/User: {user},\nPassword: {password}\n Do you want to save them?")
        if is_ok:
            with open("PassTable.txt","a") as file:
                file.write(f"\n{website} | {user} | {password}")
                file.close()
            pc.copy(password)
            website_box.delete(0, END)
            password_box.delete(0, END)
            messagebox.showinfo(title="",message="Information Saved !\nPassword copied to Clipboard")
# ---------------------------- UI SETUP ------------------------------- #

#----------Window Setup-----------
window = Tk()
window.title("Password Master")
window.config(padx=50,pady=50,bg=BG_COLOR)

logo = Canvas(width=200,height=200,bg=BG_COLOR,highlightthickness=0)
photo = PhotoImage(file="logo.png")
logo.create_image(100,100,image=photo)

logo.grid(column=1,row=0)
#-----------Labels Setup------------
website_LBL = Label(text = "Website:",bg=BG_COLOR,foreground=RED)
website_LBL.grid(column=0,row=1)

username_LBL = Label(text = "Email/Username:",bg=BG_COLOR,foreground=RED)
username_LBL.grid(column=0,row=2)

Password_LBL = Label(text = "Password:",bg=BG_COLOR,foreground=RED)
Password_LBL.grid(column=0,row=3)

#-----------Textinput Setup----------
website_box = Entry(width=40,bg=BG_COLOR,borderwidth=0.5,foreground=RED,textvariable=StringVar(),insertbackground=RED)
website_box.grid(column=1,row=1,columnspan=2,sticky="EW")
website_box.focus()

username_box = Entry(width=40,bg=BG_COLOR,borderwidth=0.5,foreground=RED,textvariable=StringVar(),insertbackground=RED)
username_box.grid(column=1,row=2,columnspan=2,sticky="EW")
username_box.insert(0,"myemail@gmail.com")

password_box = Entry(width=32,bg=BG_COLOR,borderwidth=0.5,foreground=RED,textvariable=StringVar(),insertbackground=RED)
password_box.grid(column=1,row=3,sticky="W")

#-----------Buttons Setup------------

add_BTN = Button(text = "Add" ,bg=BG_COLOR,borderwidth=0.5,foreground=RED,activebackground=RED,command=save_password)
add_BTN.grid(column= 1,row=4,sticky="EW",columnspan=2)

generate_BTN = Button(text= "Generate Password",bg=BG_COLOR,borderwidth=0.5,foreground=RED,activebackground=RED,command=passgen)
generate_BTN.grid(column=2,row=3,sticky="E")

window.mainloop()