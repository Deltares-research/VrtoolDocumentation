# Genereren database

De input database kan worden gemaakt door de volgende stappen te volgen: 

**Stap 1**: Open de Anaconda Prompt

**Stap 2**:	Ga naar de directory van de preprocessor met behulp van de volgende commandline. Vervang “C:/link_naar_ZIP_file_map” met de locatie van de map waar de ZIP file is uitgepakt:
```
cd C:/link_naar_ZIP_file_map
```

**Stap 3**:	Activeer het environment van de preprocessor (ervan uitgaande dat de environment reeds is geïnstalleerd):
```
conda activate .env
```
**Stap 4**:	Als je deze regel code typt, krijg je een beschrijving van de benodigde invoerparameters:
```
python -m preprocessing maak_database --help
```


De tabel beschrijft een voorbeeld van hoe de paden eruit kunnen zien.


| Parameter     	 | 	Toelichting           |
|---------|-------------|
| --traject_id|Hier geef je aan om welk traject het gaat. Dit is een string, bijvoorbeeld ‘38-1’. Dit is verplichte invoer.|
|--vakindeling_geojson |Link naar de GeoJSON met de vakindeling. Dit is verplichte invoer.|
|--characteristic_profile_csv |Link naar de map met de CSV’s van de gegenereerde karakteristieke profielen. Dit is verplichte invoer.|
|--building_csv_path |Link naar het CSV-bestand van de gegenereerde gebouwen. Dit is verplichte invoer.|
|--output_dir |Link naar de map waar de resultaten (database-bestand en config.json) terecht moeten komen. Dit is verplichte invoer.|
|--output_db_name |Hier vul je een naam in voor de te creëren database. Belangrijk om “.db” aan het einde toe te voegen. Voorbeeld: --output_db_name “resultaten_trajectX.db”. Dit is verplichte invoer.|
|--hr_input_csv |Link naar de ingevulde CSV (HR_default.csv) die gebruikt is voor de HR sommen. Dit is verplichte invoer.|
|--waterlevel_results_path |Link naar de map met de resultaten van de waterstandssommen. Dit is verplichte invoer.|
|--overflow_results_path	|Link naar de map met de resultaten van de overslagsommen. Dit is verplichte invoer.|
|--piping_path	|Link naar de ingevulde CSV voor piping (Piping_default.csv). Dit is verplichte invoer, indien piping een relevant faalmechanisme is voor dit traject en de CSV is ingevuld.|
|--stability_path	|Link naar de ingevulde CSV voor stabiliteit (Stabiliteit_default.csv). Dit is verplichte invoer, indien stabiliteit een relevant faalmechanisme is voor dit traject en de CSV is ingevuld.|
|--revetment_path	|Link naar de uitvoermap van de bekledingssommen. Dit is alleen verplichte invoer, indien bekleding een relevant faalmechanisme is voor dit traject en er invoer voor bekleding is gegenereerd.|



**Stap 5**:	Run de preprocessing voor maak_database, vul de juiste paden op de juiste plek in. Zie hier een voorbeeld waarbij de paden uit de tabel zijn gebruikt:
```
python -m preprocessing maak_database --traject_id "53-1" --vakindeling_geojson "c:\VRM\test_database\resultaten\preprocessing_vakindeling\Optie_1\Vakindeling_53-1.geojson" --characteristic_profile_csv "C:\VRM\test_database\resultaten\vakindeling1\selectie_profielen_1\selected_profiles.csv" --building_csv_path "C:\VRM\test_database\resultaten\vakindeling1\building_count_traject53-1.csv" --output_dir "C:\VRM\test_database\Output" --output_db_name "53-1_database.db" --hr_input_csv "C:\VRM\test_database\resultaten\HR_53-1.csv" --waterlevel_results_path "C:\VRM\test_database\resultaten\preprocessing_waterlevel" --overflow_results_path "c:\VRM\test_database\resultaten\preprocessing_overflow" --piping_path "c:\VRM\test_database\resultaten\Piping_53-1.csv" --stability_path "c:\VRM\test_database\resultaten\Stabiliteit_53-1.csv"
```
