from tkinter import *

root = Tk()
root.title("Sarah's pink calculator that nobody asked for")
root.geometry("300x450")
root.config(bg="#F2B2CD")
title = Label(root, text="welcome to my useless calculator gal", font=("Arial", 12), bg= "#F2B2CD" , fg="#563C5C")
title.pack()
inputs = Entry(
	root, width=25, borderwidth=10, font=("Arial", 14), bg="#563C5C", fg="#FFFFFF", justify='left'
)
inputs.pack(pady=10) #adding some space below the input box 
def click(button_value): #this function is used to insert the clicked button value into the input box
    if button_value == "=":
        try:
            result = eval(inputs.get())
            inputs.delete(0, END)
            inputs.insert(0, str(result))
        except Exception:
            inputs.delete(0, END)
            inputs.insert(0, "Error")
    else:
        current = inputs.get()            # Get the current input
        inputs.delete(0, END)             # Clear the entry box
        inputs.insert(0, current + str(button_value))  #insert the value in the display box

    #time to create the buttons: to do so we create a function that halp us create and position and color and fill a button
def new_button(value, row, column):
    button = Button(
        button_frame, text=value, padx=20, pady=20, bg="#FFD1DC", fg="#563C5C", font=("Arial", 14),
        command=lambda: click(value)  #for now just remember lambda as a way to do a shortcut to a fuction call - delay switch
    )
    button.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)

button_frame = Frame(root)
button_frame.pack()

#now we create the buttons
# First row
new_button("7", 0, 0)
new_button("8", 0, 1)
new_button("9", 0, 2)
new_button("/", 0, 3)

# Second row
new_button("4", 1, 0)
new_button("5", 1, 1)
new_button("6", 1, 2)
new_button("*", 1, 3)

# Third row
new_button("1", 2, 0)
new_button("2", 2, 1)
new_button("3", 2, 2)
new_button("-", 2, 3)

# Fourth row
new_button("0", 3, 0)
new_button(".", 3, 1)
new_button("=", 3, 2)
new_button("+", 3, 3)




root.mainloop()