from tkinter import *
import tkinter
from tkinter import messagebox
from configparser import ConfigParser 
import requests

root=tkinter.Tk()
root.geometry("230x230")
root.resizable()
root.title("Weather App")
input_feild=StringVar()

config_file="config.ini"
config=ConfigParser()
config.read(config_file)
api_key=config['gfg']['api']
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


def getwether(city):
    result=requests.get(url.format(city,api_key))

def btn_click():
    pass

mainfram=Frame(root,width=229,height=223, highlightbackground="green",highlightthickness=2)
mainfram.pack()

textarea=Entry(mainfram,width=200,textvariable=input_feild,background="lightblue")
textarea.pack()

button_stb=Button(mainfram,text="search",background="white",foreground="black",command=lambda:btn_click())
button_stb.pack()

root.mainloop()