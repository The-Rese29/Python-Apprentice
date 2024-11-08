"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.


Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk 

# Create a window object
window = Tk()

# Hide the window, hint: use the withdraw method
window.withdraw()

# Ask the user for the first number   
a = simpledialog.askinteger("First Number", "What's Number 1?")

# Ask the user for the second number
b = simpledialog.askinteger("Second Number", "What's Number 2?")

# Ask the user for the math operation
c = simpledialog.askstring("Operation", "What's the Operation?")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.

if c == "addition":
    print(a+b)

elif c == "subtraction":
    print(a-b)

if c == "division":
   print(a/b)

if c == "multiplication":
    print(a*b)


# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
messagebox.showerror()

# Keep the window open
window.mainloop()