import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('400x400')
root.title('Weather App (GUI)')
cit = StringVar()
Label(root, text='Weather for today', font='arial', fg="blue").grid(row=1, column=3)
Label(root, text='Enter City:', fg="green").grid(row=2, column=1)
Entry(root, width=15, textvariable=cit, border="5px").grid(row=2, column=2)

api_key = "c1ced8243a109e9b580be349c2c8b0b0"


def proceed():
    city = cit.get()
    if city == '':
        return messagebox.showerror('Error', 'Enter City Name')
    elif api_key == 'your api key':
        return messagebox.showerror('Error', 'Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url) 
        x = response.json()  
        if x["cod"] != "404": 
  
            y = x["main"] 
            current_temp = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]

            z = x["weather"] 
            weather_description = z[0]["description"]  
            Label(root, text='Temperature: '+str(round(current_temp-272.15))+' degree celsius').place(x=2, y=90)
            Label(root, text='Atmospheric Pressure: '+str(current_pressure)+' hPa').place(x=2, y=120)
            Label(root, text='Humidity: '+str(current_humidity)).place(x=2, y=150)
            Label(root, text='Description: '+str(weather_description)).place(x=2, y=180)
        else: 
            return messagebox.showerror('Error', 'No City Found')


# button for proceed
Button(root, text='Proceed', command=proceed, bg="red", foreground="blue", border="5px").grid(row=3, column=3)


root.mainloop()
