# Bekledingen

## Stap 1: Excel invoerbestand invullen

De basis voor het genereren van de bekleding berekeningen is het invoerbestand `Bekleding_default.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de ZIP bestand die bij de installatie voor [preprocessing](..\Installaties\VRUtils.md) is gedownload.

Dit bestand heeft de volgende kolommen die ingevul dmoeten worden:

| Kolom       	          | 	           | Beschrijving                                                                                                                                                                                 	 |
|------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vaknaam 	              | Verplicht 	 | De vaknaam zoals beschreven in de Vakindeling.csv                                                                                                                                             |
| signaleringswaarde  	  | Verplicht 	 | Signaleeringswaarde van het traject                                                                                                                                                            |
| ondergrens    	        | Verplicht 	 | Ondergrenswaarde van het traject                                                                                                                                                               |
| faalkansbijdrage       | Verplicht 	 | Bijdrage van bekleding aan het totale traject faalkans                                                                                                                                         |
| lengte_effectfactor	   | Verplicht 	 | Waarde van het lengte-effect (N)                                                                                                                                                               |
| locationid     	       | Verplicht 	 | ID uit HydraRing                                                                                                                                                                               |
| hrdatabase_folder    	 | Verplicht 	 | Naam van HR database                                                                                                                                                                           |
| hrdatabase	            | Verplicht 	 | Naam van HR database                                                                                                                                                                           |
| region    	            | Verplicht 	 | Region van het traject. Te kiezen uit: kust, meren, benedenrivierengebied of bovenrivierengebied                                                                                               |
| gws   	                | Verplicht 	 | Gemiddelde buitenwaterstand                                                                                                                                                                    |
| getij_amplitude	       | Verplicht 	 | Amplitude van het getij                                                                                                                                                                        |
| dwarsprofiel	          | Verplicht 	 | Nummer van het dwarsprofiel                                                                                                                                                                    |
| steentoetsfile     	   | Verplicht 	 | NAam van het steentoetsfile bestand                                                                                                                                                            |
| prfl    	              | Verplicht 	 | Naam van het prfl bestand te gebruiken voor bekleding                                                                                                                                          |
| begin_grasbekleding    | Verplicht 	 | hoogte waarop de grasbekleding begint (dus onderste punt) [m+NAP]                                                                                                                              |
| qvar_p1     	          | Verplicht 	 | Q-variant: overschrijdingskans voor waterstand. Suggestie: 30/ondergrens                                                                                                                       |
| qvar_p2    	           | Verplicht 	 | Q-variant: overschrijdingskans voor waterstand. Suggestie: 1/signaleringswaarde                                                                                                                | 
| qvar_p3  	             | Verplicht 	 | Q-variant: overschrijdingskans voor waterstand. Suggestie: 1/(30 x signaleringswaarde)                                                                                                         |
| qvar_p4  	             | Verplicht 	 | Q-variant: overschrijdingskans voor waterstand: 1/(100 x signaleringswaarde)                                                                                                                   |
| qvar_stap  	           | Verplicht 	 | Stapgrootte voor Q-variant berekeningen                                                                                                                                                        |


## Stap 2: Command-Line Interface voorbereiden

Stap 2 is identiek als de preprocessing van de [vakindeling](Vakindeling.md).

## Stap 3: Script voor bekleding runnen  

Via de **Command Line Interface (CLI)** kan de VR Preprocessing tool worden aangeroepen, zonder dat de gebruiker in de Python code hoeft te werken. Dit werkt als volgt:

```
python -m preprocessing bekleding {input arguments}”
```

Vervang nog "{input arguments}" met behorend inputs van bekleding: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

De inputs van bekleding zijn: 

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                        |
|-------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --input_csv 	       | Verplicht 	 | 	Link naar het excel invoerbestand, bijvoorbeeld: "c:\VRM\test_revetments_cli\Bekleding_default.csv"                                                                                                                                  |
| --database_path     	 | Verplicht 	 | Link naar de map met de database, bijvoorbeeld: "c:\VRM\test_revetments_cli\database"                                                                                                                                                 |
| --steentoets_path    	   | Verplicht 	 | Link naar de map met de steentoets files, bijvoorbeeld: "c:\VRM\test_revetments_cli\steentoets"	                                                                                                                                      |
| --profielen_path    | Verplicht 	 | Link naar de map met alle profielen, bijvoobeeld: "c:\VRM\test_revetments_cli\profielen"                                                                                                                                            	 |
| --figures_gebu    | Verplicht 	 | Link naar map met GEBU figuren, bijvoobeeld: "c:\VRM\test_revetments_cli\figures_GEBU_CLI"                                                                                                                                            |
| --figures_zst    | Verplicht 	 | Link naar map met ZST figuren, bijvoobeeld: "c:\VRM\test_revetments_cli\figures_ZST_CLI"                                                                                                                                              |
| --hring_path    | Verplicht 	 | Path naar Hring, bijvoorbeeld: "c:/Program Files (x86)/BOI/Riskeer 21.1.1.2/Application/Standalone/Deltares/HydraRing-20.1.3.10236"                                                                                                   |
| --bin_dikernel    | Verplicht 	 | Path naar het Dikernel, bijvoobeeld: "c:/VRM/test_revetments_cli/bin_DiKErnel"                                                                                                                                                        |
| --output_path    | Verplicht 	 | Link naar map waar resultaten moeten worden opgeslagen, bijvoobeeld: "c:\VRM\test_revetments_cli\output_CLI"                                                                                                                          |

**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.


Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing bekleding –help ```

### Voorbeeld invoer: 
```
python -m preprocessing bekleding --input_csv "c:\VRM\test_revetments_cli\Bekleding_default.csv" --database_path "c:\VRM\test_revetments_cli\database" --steentoets_path "c:\VRM\test_revetments_cli\steentoets" --profielen_path "c:\VRM\test_revetments_cli\profielen" --figures_gebu "c:\VRM\test_revetments_cli\figures_GEBU_CLI" --figures_zst "c:\VRM\test_revetments_cli\figures_ZST_CLI" --hring_path  "c:/Program Files (x86)/BOI/Riskeer 21.1.1.2/Application/Standalone/Deltares/HydraRing-20.1.3.10236" --bin_dikernel "c:/VRM/test_revetments_cli/bin_DiKErnel" --output_path "c:\VRM\test_revetments_cli\output_CLI"
```

