# Afleiden teenlijn

De workflow bestaat uit het volgende script
- De script ```Get_binnenteenlijn.py``` pakt alle gevonden teenpunten uit de CSV-bestanden in output_dir/characteristic_profiles. Vervolgens wordt per profiel het x-coördinaat en y-coördinaat bepaald, door te kijken waar op de lijn tussen de uiterste punten op het voor- en achterland de teen precies ligt. Dit script gebruikt dus zowel de CSV-bestanden van de afgeleide karakteristieke punten, als de informatie uit traject_profiles_info.csv. De teenlijn wordt als GeoJSON-bestand weggeschreven naar een EPSG:28992, als teenlijn.gjson.

*Let op*: Er is geen input excel bij deze workflow.

## Stap 1: Command-Line Interface voorbereiden

Stap 1 is identiek als de preprocessing van de [vakindeling](Vakindeling.md).

## Stap 2: Script voor het afleiden van de teenlijn runnen  
De gebruiker kan de workflow als volgt aanroepen vanuit de Anaconda Prompt (activeer eerst environment):
```
python -m preprocessing genereer_teenlijn
```
De invoer die nodig is voor het afleiden van de binnenteenlijn, is weergegeven de tabel hieronder.

| Input naam       	    | 	           | Beschrijving                                                                                                                                                                                 	                                                                          |
|-----------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --karakteristieke_profielen_map        | Verplicht 	 | Hier geef je het pad naar de map waar de gegenereerde karakteristieke punten (uit een eerdere stap: 'genereer dijkprofielen') zijn opgeslagen	                                                                                                                                                                  |
| --profiel_info_csv     	 | Verplicht 	 |  Dit is het pad naar de csv met de informatie over de verzamelde profielen (uit een eerdere stap: 'genereer dijkprofielen'). Deze csv zou traject_profiles.csv moeten heten, tenzij de gebruiker de naam heeft aangepast.                                                                                                                                                                              |
| --teenlijn_map	   | Verplicht 	 |   Hier geef je de het pad naar de map waar de teenlijn naartoe moet worden geschreven. De gebruiker mag deze map zelf aanmaken, maar als de map niet bestaat, wordt deze automatisch aangemaakt. Het uitvoerbestand heet 'teenlijn.geojson'.                                                                                                                                                    |


Om meer informatie over de code te krijgen, gebruik je: 
```
python -m preprocessing genereer_teenlijn --help 
```
### Voorbeeld invoer: 

```
python -m preprocessing genereer_teenlijn --karakteristieke_profielen_map="c:\VRM\Gegevens 38-1\dijkinfo\characteristic_profiles" --profiel_info_csv="c:\VRM\Gegevens 38-1\dijkinfo\traject_profiles.csv" --teenlijn_map="c:\VRM\Gegevens 38-1\dijkinfo\teenlijn"
```

## Stap 3: Controleren van Teenlijn

De workflow eindigt hier. Reden hiervoor is dat de gebruiker nu de gelegenheid heeft om plots (figuren) van profielen te checken en bijbehorende teenlijn. Mochten teenpunten niet goed liggen, kan de teenlijn handmatig in GIS worden aangepast (er is nog niet getest of het toevoegen/verwijderen van punten aan het begin/eind/midden van de teenlijn tot problemen leidt in vervolgstappen). Een andere optie is om ‘slechte’ PNG figuren te verwijderen (waar de karakteristieke punten onjuist zijn afgeleid), alvorens deze workflow te draaien. De profielen waarvan de PNG is verwijderd, worden genegeerd.
