# Bekledingen
**NB: Dit gedeelte is niet up-to-date en wordt in de komende weken aangepast**
Vóór het draaien van deze workflow moet eerst een invoerbestand ingevult worden. 

## Stap 1: Excel invoerbestand invullen

De basis voor het genereren van de bekleding berekeningen is het invoerbestand `Bekleding_default.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de ZIP bestand die bij de installatie voor [preprocessing](..\Installaties\VRUtils.md) is gedownload.

Dit bestand heeft de volgende kolommen die ingevuld moeten worden:

| Kolom       	          | 	           | Beschrijving                                                                                                                                                                                 	 |
|------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| doorsnede 	              | Verplicht 	 | De doorsnede zoals beschreven in de Vakindeling.csv                                                                                                                                              |
| naam_hr_locatie    	 | Verplicht 	 | Naam van folder met HLCD, HRD en config database                                                                                                                                               |
| locationid     	       | Verplicht 	 | ID uit HLCD van HydraRing                                                                                                                                                                      |
| region    	            | Verplicht 	 | Region van het traject. Te kiezen uit: kust en meren (m.u.v. Oosterschelde)                                                                                                                    |
| gws   	                | Verplicht 	 | Gemiddelde buitenwaterstand in m+NAP                                                                                                                                                           |
| getij_amplitude	       | Verplicht 	 | Gemiddelde amplitude van het getij in meters                                                                                                                                                   |
| dwarsprofiel	          | Verplicht 	 | Nummer van het dwarsprofiel uit het Steentoetsbestand                                                                                                                                          |
| steentoetsfile     	   | Verplicht 	 | Naam van het steentoetsfile bestand                                                                                                                                                            |
| prfl    	              | Verplicht 	 | Naam van het prfl bestand te gebruiken voor bekleding                                                                                                                                          |
| begin_grasbekleding    | Verplicht 	 | hoogte waarop de grasbekleding begint (dus onderste punt) [m+NAP]                                                                                                                              |
| waterstand_stap  	           | Verplicht 	 | Stapgrootte voor de waterstand in Q-variant berekeningen in meters. Dient voor definiëren van waterstandniveaus onder de waterstand bij de norm                                                                 |


## Stap 2: Draaien van de bekleding workflow 

Via de **Command Line Interface (CLI)** van Anaconda kan de Preprocessing tool worden aangeroepen, zie [werken met de preprocessor](werken_met_preprocessor.md). Voer daarna het volgende commando in:

```
python -m preprocessing bekleding {input arguments}”
```

Vervang nog "{input arguments}" met behorend inputs van bekleding: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

De inputs voor bekledingen zijn: 

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                        |
|-------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --input_csv 	       | Verplicht 	 | 	Link naar het excel invoerbestand, bijvoorbeeld: "c:\VRM\test_revetments_cli\Bekleding_default.csv"                                                                                                                                  |
| --database_path     	 | Verplicht 	 | Link naar de map met de database, bijvoorbeeld: "c:\VRM\test_revetments_cli\database\WBI2017_Oosterschelde_26-3_v02". Deze map moet in ieder geval een HRD, bijbehorende config, hlcd en hlcd_W_2100.sqlite bevatten                                                                                                                                                 |
| --waterlevel_path    | Verplicht 	 | Link naar een map met frequentielijnen voor de waterstand, zolas bepaald in de workflow [Waterstand](Waterstand.md)      |
| --steentoets_path    	   | Verplicht 	 | Link naar de map met de steentoets files, bijvoorbeeld: "c:\VRM\test_revetments_cli\steentoets"	                                                                                                                                      |
| --profielen_path    | Verplicht 	 | Link naar de map met alle profielen, bijvoobeeld: "c:\VRM\test_revetments_cli\profielen"                                                                                                                                            	 |
| --output_path    | Verplicht 	 | Link naar map waar resultaten moeten worden opgeslagen, bijvoobeeld: "c:\VRM\test_revetments_cli\output_CLI"                                                                                                                          |

**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.

Uitgangspunt is dat de workflow wordt gebruikt voor locaties met een steen- en grasbekleding. Andere situaties worden (nog) niet ondersteund.

Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing bekleding –help ```

### Voorbeeld invoer: 
```
python -m preprocessing bekleding --input_csv "c:\VRM\Bekleding_traject_26-3\Bekleding_default.csv" --waterlevel_path "c:\VRM\Waterstand_traject_26-3" --database_path "c:\VRM\Bekleding_traject_26-3\database\WBI2017_Oosterschelde_26-3_v02" --steentoets_path "c:\VRM\Bekleding_traject_26-3\steentoets" --profielen_path "c:\VRM\Bekleding_traject_26-3\profielen" --output_path "c:\VRM\test_revetments_cli\output_CLI"
```

