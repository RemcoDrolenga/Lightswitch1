from cgitb import text
import tkinter as tk
from turtle import bgcolor
window = tk.Tk()

# schijf hier tussen je code
window.title("Lichtknopje")

def lichtknopje():
    if button.config("text")[-1]=="Switch light on":
        button.config(text="Switch light off")
        window.config(bg= "yellow")
        print("Light is on")
    else:
        button.config(text="Switch light on")
        window.config(bg="black")
        print("light is off")

button = tk.Button(text='Switch light off', bg="white", fg="black", command= lichtknopje)
button.pack(pady = 150, padx = 200)

window.config(bg= lichtknopje())
# schijf hier tussen je code

window.mainloop()