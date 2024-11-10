from tkinter import *
# import tkinter as tk
# import pandas as pd
# import requests
# import numpy as np
from tkcalendar import *

'''Create A Date Picker Calendar - Python Tkinter GUI Tutorial #72
https://www.youtube.com/watch?v=fqfy-3IoVvs'''

'''Adding a Pop-Up Calendar to a Python Tkinter Form using TkCalendar to pick Dates
https://www.youtube.com/watch?v=jU-LVFjBD3g'''



root = Tk()
root.geometry("600x400")

cal = Calendar(root, selectmode = "day", year = 2020, month=5, day=22)
cal.pack()

def grab_date():
    my_label.config(text="Hoy es " + cal.get_date())

my_button = Button(root, text="Obtener fecha", command = grab_date)
my_button.pack()

my_label = Label(root, text="")
my_label.pack()


root.mainloop()



