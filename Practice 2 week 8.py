from tkinter import *
from tkinter import messagebox  # Import messagebox for displaying alerts

root = Tk()
root.title("HIT 137 week 8")
root.geometry("700x700")

# Create frames to separate different sections
top_frame = Frame(root)
top_frame.pack(side=TOP, fill=X)

button_frame = Frame(root)
button_frame.pack(side=TOP, pady=10)

login_frame = Frame(root)
login_frame.pack(side=TOP, pady=10)

# there is a new line to be commited in the github.
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, fill=X)

# Welcome label at the top
welcome_label = Label(top_frame, text="Welcome to HIT 137 week 8", font=("Arial", 25))
welcome_label.pack(side=TOP, pady=10)

# Function for Button 1
def onClickButton1():
    messagebox.showinfo("Button 1", "You clicked Button 1!")

# Buttons in the button frame using grid
button1 = Button(button_frame, text="Button 1", fg="red", command=onClickButton1)
button2 = Button(button_frame, text="Button 2", fg="blue")     
button3 = Button(button_frame, text="Button 3", fg="green")
button4 = Button(button_frame, text="Button 4", fg="purple")

button1.grid(row=0, column=0, padx=5)
button2.grid(row=0, column=1, padx=5)        
button3.grid(row=0, column=2, padx=5)
button4.grid(row=0, column=3, padx=5)

# Login section using grid within its own frame
def onClickLogin():
    # Get entered username and password
    entered_name = entry_name.get()
    entered_pass = entry_pass.get()
    
    # Check credentials
    if entered_name == "Gyandip" and entered_pass =="1234":
        # Success message
        messagebox.showinfo("Login Status", "Password successful")
        result_label.config(text="Login successful!", fg="green")
        
        # Ask if they like Python Project after successful login
        like_response = messagebox.askyesno("Python Project", "Do you like Python Project?")
        if like_response:
            messagebox.showinfo("Thank You", "Great! We're glad you enjoy the Python Project!")
        else:
            messagebox.showinfo("Feedback", "We appreciate your feedback. We'll work to improve!")
    else:
        # Failure message
        messagebox.showerror("Login Status", "Sorry, try again")
        result_label.config(text="Invalid credentials. Please try again.", fg="red")
    
    # Print to console (for debugging)
    print("Name:", entered_name)
    print("Password:", entered_pass)
    

name_label = Label(login_frame, text="Name")
pass_label = Label(login_frame, text="Password")
entry_name = Entry(login_frame)
entry_pass = Entry(login_frame, show="*")
login_button = Button(login_frame, text="Login", command=onClickLogin)  # Changed button text to "Login"
login_check = Checkbutton(login_frame, text="Keep me logged in")

# Add a label to show login result
result_label = Label(login_frame, text="", font=("Arial", 10))

name_label.grid(row=0, column=0, sticky=E, padx=5, pady=5)
pass_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_pass.grid(row=1, column=1, padx=5, pady=5)
login_button.grid(row=2, column=1, padx=5, pady=5)
login_check.grid(row=3, column=1, padx=5, pady=5)
result_label.grid(row=4, column=0, columnspan=2, pady=5)  # Add result label to the grid

# Three colored labels at the bottom
one_label = Label(bottom_frame, text="One", fg="black", bg="gray", width=20, height=2)
two_label = Label(bottom_frame, text="Two", fg="green", bg="lightgray", width=100, height=2)
three_label = Label(bottom_frame, text="Three", fg="white", bg="black", width=5, height=20)

three_label.pack(side=LEFT, fill=Y)
two_label.pack(fill=X)
one_label.pack(side=BOTTOM, pady=5)

root.mainloop()