# Afleiden dijkprofielen en karakteristieke punten

Met de workflow ```genereer_dijkprofielen``` worden voor een gegeven traject elke x meter dijkprofielen gegenereerd op basis van het AHN4. Voor elk van deze profielen worden de karakteristieke punten afgeleid: 2 punten op de kruin, en op zowel het buiten- als het binnentalud beide maximaal 3 punten. 

De workflow bevat 2 stappen, die achter elkaar worden doorlopen als de workflow wordt aangeroepen: eerst worden de AHN profielen afgeleid, daarna worden de karakteristieke punten bepaald.

In de map AHN_profiles worden profielen uit AHN4 weggeschreven naar csv-bestanden. Deze map wordt (automatisch) gemaakt in de uitvoermap (output_dir). In de uitvoermap output_dir wordt ook een overzicht opgeslagen met informatie over elk profiel (m-waarde, naam CSV-bestand, x- en y-coördinaten van het uiterste punt op het voorland en het achterland): traject_profiles_info.csv.

In de map characteristic_profiles wordt voor elk AHN-profiel karakteristieke (knik)punten weggeschreven Hierin wordt per profiel een figuur (profielnaam.png) weggeschreven met daarin het profiel en het karakteristieke profiel. Er wordt ook een CSV-bestand (profielnaam.csv) weggeschreven met daarin de gevonden karakteristieke punten voor het desbetreffende profiel.

*Let op*: Er is geen input excel bij deze workflow.

## Stap 1: Command-Line Interface voorbereiden

Stap 1 is identiek aan de preprocessing van de [vakindeling](Vakindeling.md).

## Stap 2: Script voor het afleiden van profielen uit AHN  
De gebruiker kan de workflow als volgt aanroepen vanuit de Anaconda Prompt (activeer eerst environment):

```
python -m preprocessing genereer_dijkprofielen
```
De invoer die nodig is voor het afleiden van de karakteristieke profielen, is weergegeven in de tabel hieronder.

| Input naam       	    | 	           | Beschrijving                                                                                                                                                                                 	                                                                          |
|-----------------------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --traject_id	         | Verplicht 	 | 	Hier geef je aan om welk traject het gaat. Dit is een string, bijvoorbeeld '38-1'.                                                                                                                                                                   |
| --output_folder     	 | Verplicht 	 | Het pad naar de map waar de uitvoer naartoe wordt geschreven. Als de map niet bestaat, wordt deze aangemaakt.                                                                                                                                                                                 |
| --traject_shape   	   | Optioneel 	 | Link naar de trajectshapefile. Let op: voer deze alleen in als de gebruikte shapefile afwijkt van de shapefile in het NBPW. Als je deze optie niet gebruikt, wordt de shapefile uit het NBPW gebruikt.                                                                                                                                                                        |
| --flip_traject      | Optioneel 	 | Soms staat de shapefile in het NBPW in de tegenovergestelde richting van je vakindeling. Met andere woorden: de vakindeling begint aan de 'verkeerde' kant van de shapefile. Als dit het geval is, kan de shapefile worden omgedraaid door deze optie op True te zetten. |
| --flip_waterkant                  | Optioneel 	 | Standaard wordt hier aangenomen dat het water aan de rechterkant van het traject loopt als je de nummering van de vakken volgt. Als het water aan de andere linkerkant loopt, moet hier True worden ingevuld. Default is False.                                         |
| --dx        | Optioneel 	 | De afstand tussen de profielen. Optioneel, default is 25 meter.                                                                                                                                                                                                         |
| --voorland_lengte        | Optioneel 	 | De lengte van het voorland. Optioneel, default is 50 meter.                                                                                                                                                                                                             |
| --achterland_lengte       | Optioneel 	 | De lengte van het achterland. Optioneel, default is 75 meter.                                                                                                                                                                                                           |

**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.


Om meer informatie over de code te krijgen, gebruik je: 
```python -m preprocessing genereer_dijkprofielen –help```. 

### Voorbeeld invoer: 

```
python -m preprocessing genereer_dijkprofielen --traject_id=”38-1” --output_folder=”c:\VRM\Gegevens 38-1\dijkinfo2"
```

## Stap 3: Script voor het afleiden van een karakteristiek profiel per dijkvak

*Hier wordt nog aan gewerkt*
