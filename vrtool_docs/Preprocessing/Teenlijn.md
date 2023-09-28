# Afleiden teenlijn

De workflow ```genereer_teenlijn``` pakt alle gevonden teenpunten uit de CSV-bestanden in output_dir/characteristic_profiles (zie [Dijkprofielen](Dijkprofielen.md)). Vervolgens worden per profiel de x- en y-coördinaten van de teen bepaald. Dit script gebruikt dus zowel de CSV-bestanden van de afgeleide karakteristieke punten, als de informatie uit traject_profiles_info.csv. Daarom moeten eerst de [dijkprofielen](Dijkprofielen.md) worden bepaald. Daarbij is van belang dat de tussenafstand tussen de profielen klein is (maximaal 25 meter).

De teenlijn wordt als GeoJSON-bestand weggeschreven naar een EPSG:28992, als teenlijn.geojson.

*Let op*: Er is geen input Excel bij deze workflow.

## Stap 1: Script voor het afleiden van de teenlijn runnen  
Via de **Command Line Interface (CLI)** van Anaconda kan de Preprocessing tool worden aangeroepen, zie [werken met de preprocessor](werken_met_preprocessor.md). Voer daarna het volgende commando in:

```
python -m preprocessing genereer_teenlijn {input arguments}
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

## Stap 2: Controleren van de teenlijn

De workflow eindigt hier. Reden hiervoor is dat de gebruiker nu de gelegenheid heeft om plots (figuren) van profielen te checken en bijbehorende teenlijn. Mochten teenpunten niet goed liggen, kan de teenlijn handmatig in GIS worden aangepast (er is nog niet getest of het toevoegen/verwijderen van punten aan het begin/eind/midden van de teenlijn tot problemen leidt in vervolgstappen). Een andere optie is om ‘slechte’ PNG figuren te verwijderen (waar de karakteristieke punten onjuist zijn afgeleid), alvorens deze workflow te draaien. De profielen waarvan de PNG is verwijderd, worden genegeerd. Let daarbij wel op dat grote stukken zonder punten tot een foute teenlijn kunnen leiden omdat aangenomen wordt dat de dijk recht loopt tussen opeenvolgende profielen.
