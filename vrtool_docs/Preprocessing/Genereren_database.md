# Genereren database

Met de workflow ```maak_database``` kan een invoerdatabase voor de VRTOOL worden gegenereerd. Daarbij moeten de met de overige workflows gegenereerde bestanden als invoer worden opgegeven.

## Draaien van de workflow voor het genereren van een database
Via de **Command Line Interface (CLI)** van Anaconda kan de Preprocessing tool worden aangeroepen, zie [werken met de preprocessor](werken_met_preprocessor.md). Voer daarna het volgende commando in:


```
python -m preprocessing maak_database {invoerparameters}
```

Als je deze regel code typt, krijg je een beschrijving van de benodigde invoerparameters:

```
python -m preprocessing maak_database --help
```

Onderstaande tabel beschrijft de verschillende invoerparameters:

| Input naam  	       |           |	Toelichting           |
|----------------------|-----------|-------------|
| --traject_id        | Verplicht |Hier geef je aan om welk traject het gaat. Dit is een string, bijvoorbeeld ‘38-1’.|
| --vakindeling_geojson    | Verplicht | Link naar de GeoJSON met de vakindeling.                                                                                                                             |
| --characteristic_profile_csv | Verplicht | Link naar de map met de CSV’s van de gegenereerde karakteristieke profielen.                                                                                        |
| --building_csv_path    | Verplicht | Link naar het CSV-bestand van de gegenereerde gebouwen.                                                                                                            |
| --output_dir        | Verplicht | Link naar de map waar de resultaten (database-bestand en config.json) terecht moeten komen.                                                                           |
| --output_db_name      | Verplicht | Hier vul je een naam in voor de te creëren database. Belangrijk om “.db” aan het einde toe te voegen. Voorbeeld: --output_db_name “resultaten_trajectX.db”.         |
| --hr_input_csv          | Verplicht | Link naar de ingevulde CSV (HR_default.csv) die gebruikt is voor de HR sommen.                                                                                       |
| --waterlevel_results_path | Verplicht | Link naar de map met de resultaten van de waterstandssommen.                                                                                                         |
| --overflow_results_path	  | Verplicht | Link naar de map met de resultaten van de overslagsommen.                                                                                                         |
| --piping_path	        | Optioneel | Link naar de ingevulde CSV voor piping (Piping_default.csv). Dit is verplichte invoer, indien piping een relevant faalmechanisme is voor dit traject en de CSV is ingevuld.                    |
| --stability_path	    | Optioneel | Link naar de ingevulde CSV voor stabiliteit (Stabiliteit_default.csv). Dit is verplichte invoer, indien stabiliteit een relevant faalmechanisme is voor dit traject en de CSV is ingevuld.     |
| --revetment_path	     | Optioneel          | Link naar de uitvoermap van de bekledingssommen. Dit is alleen verplichte invoer, indien bekleding een relevant faalmechanisme is voor dit traject en er invoer voor bekleding is gegenereerd. |

**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.


### Voorbeeld invoer (zonder bekleding)
Onderstaand is een voorbeeld opgenomen met de paden uit de tabel:
```
python -m preprocessing maak_database --traject_id "53-1" --vakindeling_geojson "c:\VRM\test_database\resultaten\preprocessing_vakindeling\Optie_1\Vakindeling_53-1.geojson" --characteristic_profile_csv "C:\VRM\test_database\resultaten\vakindeling1\selectie_profielen_1\selected_profiles.csv" --building_csv_path "C:\VRM\test_database\resultaten\vakindeling1\building_count_traject53-1.csv" --output_dir "C:\VRM\test_database\Output" --output_db_name "53-1_database.db" --hr_input_csv "C:\VRM\test_database\resultaten\HR_53-1.csv" --waterlevel_results_path "C:\VRM\test_database\resultaten\preprocessing_waterlevel" --overflow_results_path "c:\VRM\test_database\resultaten\preprocessing_overflow" --piping_path "c:\VRM\test_database\resultaten\Piping_53-1.csv" --stability_path "c:\VRM\test_database\resultaten\Stabiliteit_53-1.csv"
```

### Mogelijke foutmeldingen

- Wanneer je ".db" vergeet te schrijven achter de output_db_name, krijg je een foutmelding. Het moet ```53-1_database.db``` en niet ```--output_db_name "53-1_database"```
- Wanneer je opnieuw de workflow uitvoert moet de ```--output_dir``` leeg zijn. Verwijder daaroom eerst de vorige resultaten voordat je de som opnieuw draait.

#### Doorsnedenamen niet ingevuld in geojson
In sommige gevallen wordt gedurende het werkproces eerst een ```geojson``` van de vakindeling gemaakt waarin de doorsnedenamen nog niet zijn opgegeven. Voor het koppelen van de informatie van mechanismen aan de dijkvakken moet deze kolommen gevuld zijn, en moet de ```geojson``` dus opnieuw worden gemaakt, met deze informatie.