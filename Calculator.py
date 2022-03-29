from tkinter import messagebox
from tkinter import *
gui = Tk() # Create the root (base) window 
gui.geometry("300x340")
gui.resizable(True, True)
gui.title("Calculator")
w = Label(gui, text="CALCULATOR", font="arial 20") # Create a label with words
w.grid(row=0,column=0,columnspan=4) # Put the label into the window
# Creating Menubar
menubar = Menu(gui)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Exit', menu = file)
file.add_command(label ='Exit', command = gui.destroy)

def mess():
    messagebox.showinfo("About", "Created By : Mayank Raj\nClass : XI-F")

help = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="Help", menu=help)
help.add_command(label="About", command = mess)

gui.config(menu = menubar)

expression = ""

def press(num):
    global expression
    # concatenation of string
    expression = expression + str(num)
    # update the expression by using set method
    equation.set(expression)
 
# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
        equation.set(total)
        # initialize the expression variable
        # by empty string
        expression = ""
    except:
        messagebox.showerror("Error", "You entered wrong expression")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = StringVar()
# create the text entry box for
# showing the expression .
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=80)

button1 = Button(gui, text=' 1 ', fg='black',width=4,command=lambda: press(1), font = "arial 20")
button1.grid(row=2, column=0)
button2 = Button(gui, text=' 2 ', fg='black',width=4,command=lambda: press(2), font = "arial 20")
button2.grid(row=2, column=1)
button3 = Button(gui, text=' 3 ', fg='black',width=4,command=lambda: press(3), font = "arial 20")
button3.grid(row=2, column=2)
button4 = Button(gui, text=' 4 ', fg='black',width=4,command=lambda: press(4), font = "arial 20")
button4.grid(row=3, column=0)
button5 = Button(gui, text=' 5 ', fg='black',width=4,command=lambda: press(5), font = "arial 20")
button5.grid(row=3, column=1)
button6 = Button(gui, text=' 6 ', fg='black',width=4,command=lambda: press(6), font = "arial 20")
button6.grid(row=3, column=2)
button7 = Button(gui, text=' 7 ', fg='black',width=4,command=lambda: press(7), font = "arial 20")
button7.grid(row=4, column=0)
button8 = Button(gui, text=' 8 ', fg='black',width=4,command=lambda: press(8), font = "arial 20")
button8.grid(row=4, column=1)
button9 = Button(gui, text=' 9 ', fg='black',width=4,command=lambda: press(9), font = "arial 20")
button9.grid(row=4, column=2)
button0 = Button(gui, text=' 0 ', fg='black',width=4,command=lambda: press(0), font = "arial 20")
button0.grid(row=5, column=0)
plus = Button(gui, text=' + ', fg='black',width=4,command=lambda: press("+"), font = "arial 20")
plus.grid(row=2, column=3)
minus = Button(gui, text=' - ', fg='black',width=4,command=lambda: press("-"), font = "arial 20")
minus.grid(row=3, column=3)
multiply = Button(gui, text=' × ', fg='black',width=4,command=lambda: press("*"), font = "arial 20")
multiply.grid(row=4, column=3)
divide = Button(gui, text=' ÷ ', fg='black',width=4,command=lambda: press("/"), font = "arial 20")
divide.grid(row=5, column=3)
equal = Button(gui, text=' = ', fg='black',width=4,command=equalpress, font = "arial 20")
equal.grid(row=5, column=2)
clear = Button(gui, text='Clear', fg='black',width=4,command=clear, font = "arial 20")
clear.grid(row=5, column='1')
Decimal= Button(gui, text='.', fg='black',width=4,command=lambda: press('.'), font = "arial 20")
Decimal.grid(row=6, column=0)

gui.mainloop()# Start the event loop