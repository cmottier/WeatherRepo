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

## Méthodologie

Récupération des données :
+ Téléchargées à l'aide du package Request
+ URL de téléchargement modifié à partir de la date du jour

Traitement des données :
+ Séparation des différentes données du .json
+ Calcul de la moyenne journalière des vents à partir des 24 données horaires
+ Affectation d'une icone de météo à partir du code météo (Correspondances obtenues [**ici**](https://gist.github.com/stellasphere/9490c195ed2b53c707087c8c2db4ec0c))

Sortie :
+ Construction d'un tableau markdown 
+ Affichage du tableau à l'aide du package Ipython.display

Projet d'améliorations :
+ Modifier l'affichage des jours et des heures pour afficher des valeurs françaises (la commande locale.setlocale(locale.LC_TIME,'fr_FR.UTF-8') ne fonctionne pas lors du déploiement github)
+ Insérer des logos pour clarifier les données affichées