import tkinter

#window
window = tkinter.Tk()
window.title("Python Tkinter")
window.minsize(500,500)
#label
myLabel = tkinter.Label(text="this is a label",font=('Arial', 30, 'normal'))
# myLabel.config(bg="black",fg="white")
# myLabel.pack()
# myLabel.place(x=0, y=0)
myLabel.grid(row=0,column=0)
def click_button():
   user_input = my_entry.get()
   print(user_input)

#button
myButton = tkinter.Button(text="this is a button",command=click_button)
# myButton.pack()
# myButton.update()
# myButton.winfo_height()
# myButton.place(x=100,y=100)
myButton.grid(row=1,column=1)

#entry
my_entry = tkinter.Entry(width=20)
# my_entry.pack()
my_entry.grid(row=0,column=2)


window.mainloop()