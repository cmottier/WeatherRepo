# Projet personnel de prévisions météo

Affichage des prévisions météo pour les 5 prochains jours à Montpellier, faisant apparaître : 
+ une icone de météo
+ les températures minimales et maximales
+ le vent moyen
+ les précipitations. 
  
Site mis à jour automatiquement tous les jours à partir des données de [**open-meteo.com**](https://open-meteo.com/en/docs/meteofrance-api).

## Site internet

Le site est accessible à partir de l'URL suivant :

<https://cmottier.github.io/WeatherRepo/>

## Auteure

Camille MOTTIER 

## Méthodologie

Récupération des données :
+ Téléchargées à l'aide du package Request
+ URL de téléchargement modifié automatiquement tous les jours

Traitement des données :
+ Séparation des différentes données du .json
+ Calcul de la moyenne journalière des vents à partir des 24 données horaires (en omettant les valeurs manquantes)
+ À partir des codes météo, affectation d'icones issues de <http://openweathermap.org>. Le fichier Correspondances.json donnant les correspondances codes-images est adapté de celui de [stellasphere](https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c).

Sortie et affichage :
+ Construction d'un tableau markdown et affichage du tableau à l'aide du package Ipython.display. Cela a pour avantage de s'adapter aux différents supports et formats d'écran.
+ Le tableau généré étant en Markdown et non une image, les icônes utilisées sont conservées au format initial (png).

Projet d'améliorations :
+ Modifier l'affichage des jours et des heures pour afficher des valeurs françaises (la commande locale.setlocale(locale.LC_TIME,'fr_FR.UTF-8') qui fonctionne en local ne fonctionne pas lors du déploiement github)
+ Insérer des logos pour clarifier les données affichées (températures, vent moyen, précipitations)