import random
import tkinter as tk
from tkinter import messagebox


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please fill in all fields!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email} \nPassword: {password}\n Is this correct?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website},{email},{password}\n")
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)




def initialize_ui():
    global website_entry, email_entry, password_entry
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    canvas = tk.Canvas(width=200, height=200)
    locker_img = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=locker_img)
    canvas.grid(column=1, row=0, columnspan=3)

    tk.Label(text="Website:").grid(column=0, row=1)
    tk.Label(text="Email/Username:").grid(column=0, row=2)
    tk.Label(text="Password:").grid(column=0, row=3)

    website_entry = tk.Entry(width=50)
    website_entry.grid(column=1, row=1, columnspan=3)
    website_entry.focus()
    email_entry = tk.Entry(width=50)
    email_entry.grid(column=1, row=2, columnspan=3)
    email_entry.insert(0, "abc@gmail.com")
    password_entry = tk.Entry(width=33)
    password_entry.grid(column=1, row=3)


    tk.Button(text="Generate Password", command=generate_password).grid(column=3, row=3)
    tk.Button(text="Add", width=45, command=save).grid(column=1, row=4, columnspan=3)

    window.mainloop()


initialize_ui()
