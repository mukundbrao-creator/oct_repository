from tkinter import *
from datetime import date
 
root = Tk()
root.title("Workshop Participant Greeting")
root.geometry("400x300")

heading = Label(text="Workshop Welcome Desk", fg="white", bg="#072F5F", height=1, width=300)

name_label = Label(text="Participant Name", bg="#3895D3")
name_entry = Entry()
 
def display_welcome():

    name = name_entry.get()

    text_box.delete(1.0, END)

    greeting = "Hello " + name + "!\n"
    message = "Welcome to the workshop.\n"
    workshop_date = "Date: " + str(date.today())
 
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)

text_box = Text(height=4, width=40)

welcome_button = Button(text="Check In", command=display_welcome, height=1, bg="#1261A0", fg="white")

heading.pack()
name_label.pack(pady=10)
name_entry.pack()
welcome_button.pack(pady=10)
text_box.pack()

root.mainloop()