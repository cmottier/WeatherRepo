# %%
import datetime
import requests
import json
import numpy as np
import pandas as pd
from PIL import Image
from IPython.display import display, Markdown


# %%
# Récupération des données de météo pour les n prochains jours


def data(n):
    debut = datetime.date.today()
    fin = debut + datetime.timedelta(days=n - 1)
    debut = debut.isoformat()
    fin = fin.isoformat()
    url = (
        "https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&hourly=windspeed_10m&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max&timezone=Europe%2FBerlin&start_date="
        + debut
        + "&end_date="
        + fin
    )
    reponse = requests.get(url)
    return reponse.json()


n = 5
data = data(n)

# setlocale(LC_ALL, 'fr_FR.UTF8', 'fr_FR','fr','fr','fra','fr_FR@euro');

Date = pd.to_datetime(data["daily"]["time"])
Date = [datetime.datetime.strftime(a, "%A %d/%m") for a in Date]
weather = data["daily"]["weathercode"]
temp_min = data["daily"]["temperature_2m_min"]
temp_max = data["daily"]["temperature_2m_max"]
precip = data["daily"]["precipitation_sum"]
precip = [str(precip[i]).replace("None", "-") for i in range(n)]
wind_max = data["daily"]["windspeed_10m_max"]
wind = data["hourly"]["windspeed_10m"]

# Calcul du vent moyen à 10m pour les n prochains jours


def wind_av(n):
    wind_av = []
    for i in range(n):
        w = np.array(wind[24 * i : 24 * (i + 1)])
        wind_av += [int(w[w != None].mean())]
    return wind_av


wind = wind_av(n)

# %%
# Correspondances codes météo - images

with open("/home/cmottier/SSD/HAX712X/WeatherRepo/Correspondances.json", "r") as C:
    image = json.load(C)

im_weather = []
for i in weather:
    im_weather.append(image[str(i)]["image"])


# Construction tableau


def Table(n):
    D = "|"
    Sep = "|"
    W = "|"
    T = "|"
    Wi = "|"
    P = "|"
    for i in range(n):
        D += f"{Date[i]}|"
        Sep += f":---:|"
        W += f"![]({im_weather[i]})|"
        T += f"{temp_min[i]}°C - {temp_max[i]}°C|"
        Wi += f"{wind[i]} km/h|"
        P += f"{precip[i]} mm|"
    return D + "\n" + Sep + "\n" + W + "\n" + T + "\n" + Wi + "\n" + P


display(Markdown(Table(n)))


# %%
