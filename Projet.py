#%%
import requests

url="https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto"

reponse = requests.get(url)
donnee = reponse.json()

daily = donnee['daily']
time = daily['time']
weather = daily['weathercode']
temp_min = daily['temperature_2m_min']
temp_max = daily['temperature_2m_max']



# %%
