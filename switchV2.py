import tkinter as tk
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
import pyautogui as ky
import random as rnd
import time

run = False
filePath = ""
progName = ""

def get_string():
    global progname, filePath
    user_input = entry.get()
    
    if(filePath != ""):
        root.iconbitmap(filePath)
        
    if user_input:
        
        progName = user_input
        
        if(user_input != ""):
            root.title(user_input)
            
        popup.destroy()
    else:
        answer = messagebox.askyesno("Empty input", "Are you sure you want your program name to be empty?")
        if answer:
            progName = ""
            root.title("")
            popup.destroy()
        

def quit_program():
    global run
    run = False
    label_status.config(text="Status: not running", fg="red")
    root.destroy()

def switch():
    ky.keyDown('alt')
    
    for i in range(rnd.randint(1,10)):
        ky.press('tab')
        time.sleep(.2)
        
    ky.keyUp('alt')


def paus_program():
    global run
    run = False
    label_status.config(text="Status: not running", fg="red")

def start_program():
    global run
    run = True
    label_status.config(text="Status: running", fg="green")
    
    def switch_periodically():
        if run:
            switch()
            root.after(rnd.randint(30, 90)*1000, switch_periodically) #time: 1000
    
    switch_periodically()

def custom_program():
    global filePath, progName
    filePath = filedialog.askopenfilename(filetypes=[("Icon file", "*.ico")])

    create_popup()
    
def create_popup():
    global popup
    popup = tk.Toplevel(root)
    popup.title("")
    popup.geometry("280x130")
    popup.configure(bg="grey")

    lable_input = tk.Label(popup, text="Enter titel for the program", font = custom_font, bg="grey")
    lable_input.pack(pady=5)

    global entry
    entry = tk.Entry(popup)
    entry.pack(pady=10)

    get_string_button = tk.Button(popup, text="Set Name", command=get_string, font = custom_font, bg="silver")
    get_string_button.pack(pady=5)

backgroundColor = "#C0C0C0"
buttonsColors = "#DDDDDD"

root = tk.Tk()
root.title("Program Runner")
root.geometry("300x320")
root.configure(bg=backgroundColor)

custom_font = font.Font(family="Ariel", size=15, weight="bold")

label = tk.Label(root, text="Switch Program Runner", font = custom_font, bg=backgroundColor)
label.pack(pady=10)

label_status = tk.Label(root, text="Status: not running", font = custom_font, fg="red", bg=backgroundColor)
label_status.pack(pady=10)

start_button = tk.Button(root, text="Start Program", command=start_program, font = custom_font, bg=buttonsColors)
start_button.pack(pady=5)

paus_button = tk.Button(root, text="Paus Program", command=paus_program, font = custom_font, bg=buttonsColors)
paus_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit Program", command=quit_program, font = custom_font, bg=buttonsColors)
quit_button.pack(pady=5)

custom_button = tk.Button(root, text="Custom Program", command=custom_program, font = custom_font, bg=buttonsColors)
custom_button.pack(pady=5)

root.mainloop()
