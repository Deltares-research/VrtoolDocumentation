# Afleiden bebouwing


De workflow ```tel_gebouwen``` gebruikt de binnenteen-GeoJSON en de vakindeling-GeoJSON als invoerbestand. Daarnaast is een Geopackage bestand nodig van de BAG (Basis Administratie Gebouwen). Op dit moment is het nog niet mogelijk meer dan 1000 gebouwen rechtstreeks uit de BAG te halen via internet, daar zit een limiet op van max. 1000 objecten. Daarom moet de Geopackage van de BAG direct naar een lokale schijf worden gedownload. Dat kan hier: https://service.pdok.nl/lv/bag/atom/bag.xml (Let er op dat je de Geopackage download). 

*Let op*: Er is geen input excel bij deze workflow.

## Draai van bebouwing workflow

Via de **Command Line Interface (CLI)** van Anaconda kan de Preprocessing tool worden aangeroepen, zie [werken met de preprocessor](werken_met_preprocessor.md). Voer daarna het volgende commando in:

```
python -m preprocessing tel_gebouwen {input arguments}
```
Dit levert een csv bestand met voor 1 tot 50 meter uit de teenlijn het aantal objecten.

De invoerparameters voor de workflow zijn weergegeven in de tabel hieronder.

| Input naam       	    | 	           | Beschrijving                                                                                                                                                                                 	 |
|-----------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --traject_id      | Verplicht 	 | Hier geef je aan om welk traject het gaat. Dit is een string, bijvoorbeeld '38-1'.                                                                                                             |
| --teenlijn_geojson 	 | Verplicht 	 |   Hier geef je het pad naar de GeoJSON van de gegenereerde teenlijn. Deze GeoJSON zou teenlijn.geojson moeten heten, tenzij de gebruiker de naam heeft aangepast.                                                                                                                                                                                             |
| --vakindeling_geojson	   | Verplicht 	 |  Hier geef je het pad naar de GeoJSON van de gegenereerde vakindeling.                                                                                                                                                                                              |
| --uitvoer_map 	 | Verplicht 	 |  Hier geef je de het pad naar de map waar de uitvoer naartoe moet worden geschreven.                                                                                                                                                                                              |
| --gebouwen_geopackage	   | Verplicht 	 | Hier geef je de het pad naar de geopackage van de BAG. Dit bestand is te downloaden via https://service.pdok.nl/lv/bag/atom/bag.xml. Dit is nodig, omdat de BAG het niet toelaat alle objecten vanuit het script te downloaden. Het aantal objecten is gelimiteerd tot 1000.                                                                                                                                                                                               |


Om meer informatie over de code te krijgen, gebruik je: 
```
python -m preprocessing tel_gebouwen --help
```

### Voorbeeld invoer: 

```
python -m preprocessing tel_gebouwen --traject_id="38-1" --teenlijn_geojson="c:\VRM\Gegevens 38-1\profiles\teenlijn\teenlijn.geojson" --vakindeling_geojson="c:\VRM\test_vakindeling_workflow\result\Vakindeling_38-1.geojson" --uitvoer_map="c:\VRM\Gegevens 38-1\profiles\teenlijn" --gebouwen_geopackage="c://GIS//Achtergrond//bag-light.gpkg"
```
