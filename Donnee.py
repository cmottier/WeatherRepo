#%%
import datetime
import requests
import json
from PIL import Image
from IPython.display import display, Markdown


#%%
# Récupération des données de météo

debut=datetime.date.today()
fin=debut+datetime.timedelta(days=4)
debut=debut.isoformat()
fin=fin.isoformat()

url="https://api.open-meteo.com/v1/meteofrance?latitude=43.6109&longitude=3.8763&daily=weathercode,temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max&timezone=Europe%2FBerlin&start_date="+debut+"&end_date="+fin

reponse = requests.get(url)
donnee = reponse.json()

daily = donnee['daily']
Date = daily['time']
weather = daily['weathercode']
temp_min = daily['temperature_2m_min']
temp_max = daily['temperature_2m_max']
precip=daily['precipitation_sum']
wind=daily['windspeed_10m_max']


# %%
# Correspondances codes météo - images

with open("/home/cmottier/SSD/HAX712X/WeatherRepo/Correspondances.json", "r") as C:
    data = json.load(C)

im=["","","","",""]
j=0
for i in weather :
    im[j]+=data[str(i)]['image']
    j+=1

# Construction tableau

from IPython.display import display, Markdown
display(Markdown("""
| {Date[0]} |{Date[1]} |{Date[2]} |{Date[3]} |{Date[4]} |
|:-----:|:----:|:-------:|:------:|:------:|
| ![]({im[0]}) |![]({im[1]}) |![]({im[2]}) |![]({im[3]}) |![]({im[4]}) |
|{temp_min[0]} |{temp_min[1]} |{temp_min[2]} |{temp_min[3]} |{temp_min[4]} |
|{temp_max[0]} |{temp_max[1]} |{temp_max[2]} |{temp_max[3]} |{temp_max[4]} |
""".format(Date=Date, im=im, temp_min=temp_min, temp_max=temp_max)))





