import tkinter as tk
from tkinter import ttk


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


def mod(n1, n2):
  return n1 % n2


def clear():
  entry.delete(0, tk.END)


def button_click(number):
    current = entry.get()
    if '.' in current and number == '.':
        return
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))


def button_clear():
  entry.delete(0, tk.END)


def button_add():
  first_number = entry.get()
  global f_num
  global math
  math = "addition"
  f_num = float(first_number)
  entry.delete(0, tk.END)


def button_subtract():
  first_number = entry.get()
  global f_num
  global math
  math = "subtraction"
  f_num = float(first_number)
  entry.delete(0, tk.END)


def button_multiply():
  first_number = entry.get()
  global f_num
  global math
  math = "multiplication"
  f_num = float(first_number)
  entry.delete(0, tk.END)


def button_divide():
  first_number = entry.get()
  global f_num
  global math
  math = "division"
  f_num = float(first_number)
  entry.delete(0, tk.END)


def button_mod():
  first_number = entry.get()
  global f_num
  global math
  math = "mod"
  f_num = float(first_number)
  entry.delete(0, tk.END)


def button_equal():
  second_number = entry.get()
  entry.delete(0, tk.END)

  if math == "addition":
    entry.insert(0, add(f_num, float(second_number)))
  elif math == "subtraction":
    entry.insert(0, subtract(f_num, float(second_number)))
  elif math == "multiplication":
    entry.insert(0, multiply(f_num, float(second_number)))
  elif math == "division":
    try:
      entry.insert(0, divide(f_num, float(second_number)))
    except ZeroDivisionError:
      entry.insert(0, "Cannot divide by 0")
  elif math == "mod":
    entry.insert(0, mod(f_num, float(second_number)))


root = tk.Tk()
root.title("Bossman's Calculator")

entry = ttk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_1 = ttk.Button(root, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=0, padx=5, pady=5)

button_2 = ttk.Button(root, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=1, padx=5, pady=5)

button_3 = ttk.Button(root, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=2, padx=5, pady=5)

button_4 = ttk.Button(root, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0, padx=5, pady=5)

button_5 = ttk.Button(root, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1, padx=5, pady=5)

button_6 = ttk.Button(root, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2, padx=5, pady=5)

button_7 = ttk.Button(root, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=0, padx=5, pady=5)

button_8 = ttk.Button(root, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=1, padx=5, pady=5)

button_9 = ttk.Button(root, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=2, padx=5, pady=5)

button_0 = ttk.Button(root, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=0, padx=5, pady=5)

button_decimal = ttk.Button(root, text=".", command=lambda: button_click('.'))
button_decimal.grid(row=4, column=1, padx=5, pady=5)

button_add = ttk.Button(root, text="+", command=button_add)
button_add.grid(row=1, column=3, padx=5, pady=5)

button_subtract = ttk.Button(root, text="-", command=button_subtract)
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_multiply = ttk.Button(root, text="*", command=button_multiply)
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_divide = ttk.Button(root, text="/", command=button_divide)
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_mod = ttk.Button(root, text="%", command=button_mod)
button_mod.grid(row=4, column=2, padx=5, pady=5)

button_equal = ttk.Button(root, text="=", command=button_equal)
button_equal.grid(row=5, column=3, padx=5, pady=5)

button_clear = ttk.Button(root, text="C", command=button_clear)
button_clear.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
