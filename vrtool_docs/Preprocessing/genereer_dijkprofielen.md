# Afleiden dijkprofielen en karakteristieke punten

Voor het gegeven traject worden elke x meter dijkprofielen getrokken op basis van het AHN4. Voor elk van deze profielen worden de karakteristieke punten afgeleid: 2 punten op de kruin, en op zowel het buiten- als het binnentalud beide maximaal 3 punten. 

De workflow bevat 3 stappen, die achter elkaar worden doorlopen als de workflow wordt aangeroepen: derive_profiles en derive_characteristic_points. Deze stappen werken als volgt:

1. Command-Line activeren

2. Runnen van de script ```derive_profiles.py```. 

3. Runnen van de script ```derive_characteristic_points.py```. 

De script ```derive_profiles.py``` schrijft profielen, afgeleid uit de AHN4 weg naar csv’s in een nieuw aan te maken map: AHN_profiles. Deze map wordt (automatisch) gemaakt in de uitvoermap (output_dir). In de uitvoermap output_dir  wordt ook een overzicht opgeslagen met informatie over elk profiel (m-waarde, naam CSV-bestand, x- en y-coördinaten van het uiterste punt op het voorland en het achterland): traject_profiles_info.csv.

De script ```derive_characteristic_points.py``` leidt voor elk profiel in de map ahn_profiles het karakteristieke profiel af. Deze worden weggeschreven naar een nieuwe map die wordt aangemaakt in de uitvoermap (output_dir). De naam van deze nieuwe map is characteristic_profiles. Hierin wordt per profiel een figuur (profielnaam.png) weggeschreven met daarin het profiel en het karakteristieke profiel. Er wordt ook een CSV-bestand (profielnaam.csv) weggeschreven met daarin de gevonden karakteristieke punten voor het desbetreffende profiel.

*Let op*: Er is geen input excel bij deze workflow.

## Stap 1: Command-Line Interface voorbereiden

Stap 1 is identiek als de preprocessing van de [vakindeling](Vakindeling.md).

## Stap 2: Script voor het afleiden van profilen runnen  
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

## Stap 3: Script voor het afleiden van karakteristieke punten runnen  

*Hier wordt nog aan gewerkt*