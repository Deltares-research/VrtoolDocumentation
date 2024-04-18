# Waterstand
Invoer voor de veiligheidsrendementberekening zijn met Hydra-Ring afgeleide waterstandsfrequentielijnen voor het jaar 2023 en 2100. Deze worden afgeleid middels een gestandaardiseerde workflow. Vóór het draaien van deze workflow moet eerst een invoerbestand ingevult worden. 

## Stap 1: Vullen van het invoerbestand

De basis voor het genereren van berekeningen voor waterstand en overslag is het invoerbestand `HR_default.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de folder met de uitgepakte installatie voor de [preprocessing](..\Installaties\VRUtils.md).

Dit bestand heeft de volgende kolommen die ingevuld moeten worden:

| Kolom       	                  | 	           | Beschrijving                                                                                                                                                                                 	                                                                      |
|--------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| doorsnede    	                 | Verplicht 	 | Deze naam moet overeen komen met de kolom `overslag` van `Vakindeling.csv`.                                                                                                                                     	                                                   |
| bovengrens     	               | Verplicht 	 | Bovengrens voor waterstandsberekeningen (bijv. waterstand bij kans 1/30 * signaleringswaarde).	                                                                                                                                                                     |
| ondergrens     	               | Verplicht 	 | Ondergrens voor waterstandsberekeningen (bijv. waterstand bij kans 1/10).                                                                                                                                                                                           |
| prfl_bestand      	            | Verplicht 	 | Naam van het prfl-bestand te gebruiken voor overslag.	                                                                                                                                                                                                              |
| orientatie  	                  | Optioneel 	 | Orientatie van het profiel voor overslagberekeningen. 	                                                                                                                                                |
| dijkhoogte      	              | Verplicht 	 | Hoogte van de dijk.                                                                                                                                                              	                                                                                  |
| zodeklasse      	              | Verplicht 	 | Beschrijving van de graszodekwaliteit. Waarden moeten overeenkomen met de waarden in de standaardtabel.                                                                                                                                                           	 |
| bovengrens_golfhoogteklasse 	  | Verplicht 	 | Bovengrens van de golfhoogteklasse. Bij 0-1 meter dus "1 meter", 1-2 meter wordt "2 meter" etc. 	                                                                                                                                                                   |
| faalkans 	                     | Optioneel 	 | Faalkans uit beoordeling, ter controle.                                                                                                                                        	                                                                                    |
| kruindaling      	             | Verplicht 	 | Jaarlijkse kruindaling in m.                                                                                                                                                                 	                                                                      |
| m_value          	             | Optioneel 	 | Verplicht wanneer berekeningen geografisch moeten worden gekoppeld. Kan worden gevuld met aparte workflow.                                                                                                                                                          |
| hrlocation/hr_koppel	          | Verplicht   | Verwijzing naar de bijbehorende locatie in de hydraulische database. Hrlocation kan worden afgeleid o.b.v. hr_koppel.                                                                                                                                       	       |

Belangrijk: bij het invullen van de gegevens moeten elke regel voor alle verplichte waarden een waarde bevatten anders kunnen de gegevens niet goed worden gelezen. De waarden in de kolom `doorsnede` moeten overeenkomen met die in de kolom `waterstand` in de [vakindeling](Vakindeling.md).
 
## Stap 2: Draaien van de waterstand workflow  

Via de **Command Line Interface (CLI)** van Anaconda kan de Preprocessing tool worden aangeroepen, zie [werken met de preprocessor](werken_met_preprocessor.md). Voer daarna het volgende commando in:

```
python -m preprocessing waterlevel {input arguments}”
```

Vervang daarbij "{input arguments}" met de juiste invoerparameters voor waterstand: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

De inputs van waterstand zijn: 

| Input naam       	     | 	           | Beschrijving                                                                                                                                                                                 	 |
|------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --file_path            | Verplicht 	 | Link naar de HR_default.csv.                                                                                                                                                     	            |
| --database_paths     	 | Verplicht 	 | Link naar de map met de Hydraulische databases, zowel voor de situatie huidig als voor 2100. Dus: "--database_paths <pad naar huidige situatie> --database_paths <pad naar 2100>.             |
| --output_path  	       | Verplicht 	 | 	Werkmap waar de resultaten worden geschreven. Belangrijk is dat deze map leeg is.                                                                                                            |



**Let op:** 
- Deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.
- De map met de Hydraulische databases voor 2100 moet ook de ```.config.sqlite``` en ```.sqlite``` bestanden bevatten. Bijvoorbeeld: ```WBI2017_Benedenrijn_24-3_v04.config.sqlite``` en ```WBI2017_Benedenrijn_24-3_v04.sqlite```.

Om meer informatie over de workflow te krijgen, gebruik je: 
``` python -m preprocessing waterlevel --help ```

Bij deze workflow wordt via Python Hydra-Ring aangeroepen. Daarbij wordt een groot aantal probabilistische berekeningen uitgevoerd wat betekent dat het even kan duren. Wanneer dit niet handig is kan de workflow gedraaid worden op een aparte rekencomputer, of kunnen de berekeningen in delen worden gedraaid, bijvoorbeeld door slechts een deel van de regels in de csv in te vullen.

#### Voorbeeld invoer: 
```
python -m preprocessing waterlevel --file_name “c:\VRM\test_hydraring_workflow_wdod\HR_default.csv” --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2023" --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2100" --output_path "c:\VRM\test_hydraring_workflow_wdod\waterlevel"
```
