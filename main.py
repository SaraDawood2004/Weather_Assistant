from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        if location is None:
            raise ValueError("Invalid city name")
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        if result is None:
            raise ValueError("Could not find timezone")
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # WEATHER
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3b69e0e41a2c1469d15a4675a922f2cd"
        json_data = requests.get(api).json()
        if json_data['cod'] != 200:
            raise ValueError(json_data['message'])

        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=f"{temp} °C")
        c.config(text=f"{condition} | FEELS LIKE {temp} °C")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description)
        p.config(text=f"{pressure} hPa")
    except Exception as e:
        messagebox.showerror("Weather App", str(e))

# search box
Search_image = PhotoImage(file='Copy of search.png')
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"))
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file='Copy of search_icon.png')
myimage = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage.place(x=400, y=34)

# logo
Logo_image = PhotoImage(file='Copy of logo.png')
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# bottom box
Frame_image = PhotoImage(file='Copy of box.png')
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()