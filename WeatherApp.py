# Tkinter module is Python's standard library for creating GUIs
import tkinter as tk

# Requests library let's Python app communicate with OpenWeatherMap
import requests

# OpenWeatherMap API
API_KEY = "2457ab7c781c9a65bfc653355bab34cd"

# This function is used when user clicks the Get Weather button
def get_weather():
    city = city_entry.get() # Gets city from user input
    if not city:
        result_label.config(text="Please enter a city.")
        return

    # This URL is calls the OpenWeather API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"
    try:
        # Sends the request and stores the JSON response
        response = requests.get(url)
        data = response.json()
        print(data)  # 🔍 DEBUG LINE

        # Shows message from API to user if the API returns an error
        if data["cod"] != 200:
            result_label.config(text=f"Error: {data.get('message', 'Unknown error')}")
            return

        # Extracts weather data
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        result_label.config(text=f"{city.title()}:\n{temp}°F, {description}")
    except Exception as e:
        result_label.config(text="Error fetching data.")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x200")
root.configure(bg="lightblue")  # or use any color you want

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack()

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), wraplength=280, justify="center")
result_label.pack(pady=10)

root.mainloop()