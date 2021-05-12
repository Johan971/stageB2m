import tkinter as tk
from tkinter import ttk
import os, speedtest

root=tk.Tk()

style = ttk.Style()
style.map("azeztyZ.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

button=ttk.Button(master=root,text="ee",style="azeztyZ.TButton")
button.place(relx=0.132,rely=0.320)


speedTest=speedtest.Speedtest()
# print(speedTest.download())

print("ere")

download=speedTest.download() #le fait d'executer la méthode rend disponible le ping
upload=speedTest.upload()

# dico=dict(speedTest.results)
print(type(speedTest.results)) #chelou

# print("download",download,"upload",upload)
# print(speedTest.results)
# piiing=speedTest.results.ping

# print("ping:",piiing,"dl:",download,"up",upload,"ville",speedTest.results["name"], "ip") #can't stock ping


root.mainloop()
