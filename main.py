import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime
import json
import os

FAVOURITES_FILE = "favourites.json"

WEATHER_CODES = {
    0: "☀️ Clear sky",
    1: "🌤️ Mainly clear",
    2: "⛅ Partly cloudy",
    3: "⛅ Partly cloudy",
    45: "🌫️ Fog",
    48: "🌫️ Rime fog",
    51: "🌦️ Light drizzle",
    53: "🌦️ Drizzle",
    55: "🌧️ Heavy drizzle",
    61: "🌧️ Light rain",
    63: "🌧️ Rain",
    65: "⛈️ Heavy rain",
    71: "🌨️ Light snow",
    73: "🌨️ Snow",
    75: "❄️ Heavy snow",
    80: "🌦️ Rain showers",
    81: "🌧️ Rain showers",
    82: "⛈️ Heavy showers",
    95: "⛈️ Thunderstorm",
}

def load_favourites():
    if os.path.exists(FAVOURITES_FILE):
        with open(FAVOURITES_FILE, "r") as file:
            return json.load(file)
    return []

def save_favourites():
    with open(FAVOURITES_FILE, "w") as file:
        json.dump(favourites, file)

def refresh_favourite_buttons():
    for widget in favourites_frame.winfo_children():
        widget.destroy()

    for location in favourites:
        btn = tk.Button(
            favourites_frame,
            text=location,
            font=("Arial", 12, "bold"),
            bg="#1e293b",
            fg="white",
            relief="flat",
            padx=10,
            pady=5,
            command=lambda loc=location: use_favourite(loc)
        )
        btn.pack(side="left", padx=5, pady=5)

def use_favourite(location):
    entry.delete(0, tk.END)
    entry.insert(0, location)
    get_weather()

def add_favourite():
    location = entry.get().strip()

    if not location:
        messagebox.showwarning("Missing location", "Please enter a location first.")
        return

    if location not in favourites:
        favourites.append(location)
        save_favourites()
        refresh_favourite_buttons()
    else:
        messagebox.showinfo("Already added", "That location is already in favourites.")

def remove_favourite():
    location = entry.get().strip()

    if location in favourites:
        favourites.remove(location)
        save_favourites()
        refresh_favourite_buttons()
    else:
        messagebox.showinfo("Not found", "That location is not in favourites.")

def get_weather():
    location = entry.get().strip()

    if not location:
        messagebox.showwarning("Missing location", "Please enter a location.")
        return

    try:
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
        geo = requests.get(geo_url, timeout=10).json()

        if "results" not in geo:
            location_label.config(text="Location not found")
            return

        place = geo["results"][0]
        lat = place["latitude"]
        lon = place["longitude"]

        weather_url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            "&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m"
            "&daily=weather_code,temperature_2m_max,temperature_2m_min"
            "&forecast_days=7"
        )

        weather = requests.get(weather_url, timeout=10).json()
        current = weather["current"]

        temp_label.config(text=f"{current['temperature_2m']}°C")
        condition_label.config(text=WEATHER_CODES.get(current["weather_code"], "🌈 Weather"))
        feels_label.config(text=f"Feels like\n{current['apparent_temperature']}°C")
        wind_label.config(text=f"Wind\n{current['wind_speed_10m']} km/h")
        humidity_label.config(text=f"Humidity\n{current['relative_humidity_2m']}%")
        location_label.config(text=f"{place['name']}, {place.get('country', '')}")

        for widget in forecast_frame.winfo_children():
            widget.destroy()

        for i in range(7):
            day_name = datetime.strptime(weather["daily"]["time"][i], "%Y-%m-%d").strftime("%a")
            condition = WEATHER_CODES.get(weather["daily"]["weather_code"][i], "Weather")

            card = tk.Label(
                forecast_frame,
                text=f"{day_name}\n{condition}\n{weather['daily']['temperature_2m_min'][i]}° / {weather['daily']['temperature_2m_max'][i]}°",
                font=("Arial", 12, "bold"),
                fg="white",
                bg="#132238",
                width=15,
                height=5
            )
            card.pack(side="left", padx=5)

        updated_label.config(text=f"Updated: {datetime.now().strftime('%I:%M %p')}")

    except Exception as e:
        messagebox.showerror("Error", f"Could not get weather:\n{e}")

app = tk.Tk()
app.title("🐧 Penguin Weather")
app.geometry("1050x720")
app.configure(bg="#07111f")

favourites = load_favourites()

container = tk.Frame(app, bg="#07111f")
container.pack(fill="both", expand=True, padx=40, pady=30)

title = tk.Label(
    container,
    text="🐧 Penguin Weather",
    font=("Arial", 34, "bold"),
    fg="white",
    bg="#07111f"
)
title.pack(anchor="w")

note = tk.Label(
    container,
    text="Type location as: City, Country",
    font=("Arial", 15),
    fg="#94a3b8",
    bg="#07111f"
)
note.pack(anchor="w", pady=(5, 10))

search_frame = tk.Frame(container, bg="#07111f")
search_frame.pack(anchor="w", pady=10)

entry = tk.Entry(
    search_frame,
    font=("Arial", 20),
    width=24,
    bg="#132238",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry.pack(side="left", ipady=8)

search_button = tk.Button(
    search_frame,
    text="Get Weather",
    font=("Arial", 16, "bold"),
    bg="#38bdf8",
    fg="#07111f",
    relief="flat",
    padx=22,
    pady=7,
    command=get_weather
)
search_button.pack(side="left", padx=10)

fav_button = tk.Button(
    search_frame,
    text="Add Favourite",
    font=("Arial", 16, "bold"),
    bg="#22c55e",
    fg="#07111f",
    relief="flat",
    padx=18,
    pady=7,
    command=add_favourite
)
fav_button.pack(side="left", padx=10)

remove_button = tk.Button(
    search_frame,
    text="Remove Favourite",
    font=("Arial", 16, "bold"),
    bg="#ef4444",
    fg="white",
    relief="flat",
    padx=18,
    pady=7,
    command=remove_favourite
)
remove_button.pack(side="left", padx=10)

favourites_title = tk.Label(
    container,
    text="Favourites",
    font=("Arial", 17, "bold"),
    fg="white",
    bg="#07111f"
)
favourites_title.pack(anchor="w", pady=(8, 0))

favourites_frame = tk.Frame(container, bg="#07111f")
favourites_frame.pack(anchor="w")

location_label = tk.Label(
    container,
    text="Enter a location",
    font=("Arial", 26),
    fg="#cbd5e1",
    bg="#07111f"
)
location_label.pack(anchor="w", pady=(10, 0))

temp_label = tk.Label(
    container,
    text="--°C",
    font=("Arial", 74, "bold"),
    fg="white",
    bg="#07111f"
)
temp_label.pack(anchor="w")

condition_label = tk.Label(
    container,
    text="🌦️ Waiting for weather...",
    font=("Arial", 24),
    fg="#bae6fd",
    bg="#07111f"
)
condition_label.pack(anchor="w", pady=(0, 16))

cards = tk.Frame(container, bg="#07111f")
cards.pack(anchor="w", fill="x")

def make_card(parent, text):
    card = tk.Label(
        parent,
        text=text,
        font=("Arial", 18, "bold"),
        fg="white",
        bg="#132238",
        width=14,
        height=4
    )
    card.pack(side="left", padx=8)
    return card

feels_label = make_card(cards, "Feels like\n--°C")
wind_label = make_card(cards, "Wind\n-- km/h")
humidity_label = make_card(cards, "Humidity\n--%")

forecast_title = tk.Label(
    container,
    text="7-Day Forecast",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#07111f"
)
forecast_title.pack(anchor="w", pady=(22, 8))

forecast_frame = tk.Frame(container, bg="#07111f")
forecast_frame.pack(anchor="w")

updated_label = tk.Label(
    container,
    text="",
    font=("Arial", 15),
    fg="#94a3b8",
    bg="#07111f"
)
updated_label.pack(anchor="w", pady=18)

refresh_favourite_buttons()

app.mainloop()
