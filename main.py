from tkinter import messagebox
from tkinter import*
from random import  randint,shuffle,choice
import pyperclip
import json
window=Tk()
window.config(padx=50,pady=50)
Image=PhotoImage(file="logo.png")

def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list=[]

    password_letters=[choice(letters) for char in range(nr_letters)]
    password_symbols=[choice(symbols) for sym in range(nr_symbols)]
    password_numbers=[choice(numbers) for i in range(nr_numbers)]
    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password ="".join(password_list)
    pass_space.insert(0,password)
    pyperclip.copy(password)




def save():
    website_name=web_space.get()
    mail=email_space.get()
    pw=pass_space.get()
    new_data={
        website_name:{
        "email":mail,
        "password":pw
        }
    }

    if len(website_name)==0 or len(pw)==0 :
        messagebox.showinfo(title="oops",message="please fill all blanks")
    else:

       try:
             with open("data.json","r") as f1:
                 load_data = json.load(f1)


       except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as f1:
                json.dump(new_data,f1,indent=4)
       else:
           load_data.update(new_data)
           with open("data.json", "w") as f1:
               json.dump(load_data,f1,indent=4)
       finally:
           web_space.delete(0,END)
           pass_space.delete(0,END)

def search_method():
    website=web_space.get()
    try:
        with open("data.json","r") as f1:
            data_dic=json.load(f1)
    except FileNotFoundError:
        messagebox.showinfo(title="error",message="NO file is found")
    else:

        if website in data_dic:
            email=data_dic[website]["email"]
            password=data_dic[website]["password"]
            messagebox.showinfo(title="website",message=f"email:{email}\npassword:{password}")
        else:
            messagebox.showinfo(title="oops",message="please enter another")



canvas=Canvas(width=189,height=200)
canvas.create_image(90,100,image=Image)
canvas.grid(row=0,column=1)

web_label=Label(text="Website:")
web_label.grid(row=1,column=0)


web_space=Entry(width=21)
web_space.grid(row=1,column=1)

search_button=Button(text="Search",command=search_method)
search_button.grid(row=1,column=2)


email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)


email_space=Entry(width=35)
email_space.grid(row=2,column=1,columnspan=2)
email_space.insert(0,"23b81a6748@cvr.ac.in")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

pass_space=Entry(width=21)
pass_space.grid(row=3,column=1)

g_button=Button(text="generate",command=pass_generator)
g_button.grid(row=3,column=2)

add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #