from tkinter import *
import tkinter

root=tkinter.Tk()
root.geometry("230x230")
root.resizable()
root.title("Weather App")
input_feild=StringVar()

def btn_click():
    pass

mainfram=Frame(root,width=229,height=223, highlightbackground="green",highlightthickness=2)
mainfram.pack()

textarea=Entry(mainfram,width=200,textvariable=input_feild,background="lightblue")
textarea.pack()

button_stb=Button(mainfram,text="search",background="white",foreground="black",command=lambda:btn_click())
button_stb.pack()

root.mainloop()