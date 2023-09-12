# Overslag

Ook voor overslag worden middels Hydra-Ring nieuwe overloop/overslag berekeningen gemaakt. Daarbij wordt voor verschillende kruinhoogtes de faalkans voor overslag bepaald. 
Deze workflow gebruikt hetzelfde invoerbestand als de workflow voor [waterstanden](Waterstand.md).

## Draaien van de workflow voor overslag

Via de **Command Line Interface (CLI)** kan de workflow voor het uitvoeren van waterstandsberekeningen worden aangeroepen. Start daarvoor Anaconda Prompt, activeer het environment en voer het volgende commando in:

```
python -m preprocessing waterlevel {input arguments}”
```

Vervang daarbij "{input arguments}" met de juiste invoerparameters voor waterstand: ```--input_naam1 "input_1" --input_naam2 "input_2" etc.```

| Input naam       	      | 	           | Beschrijving                                                                                                                                                                                 	                                                                                                                                                                              |
|-------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| --file_name    | Verplicht 	 | Link naar de HR_default.csv.                                                                                                                                                     	                                                                                                                                                                                          |
| --database_paths     	 | Verplicht 	 | Link naar de map met de Hydraulische database. Omdat er zowel een map voor de situatie huidig, als voor 2100 is, moet deze optie twee keer worden opgegeven. Dus: "--database_paths <pad naar de database voor huidige situatie> --database_paths <pad naar database voor de 2100 situatie>.                                                                                |
| --profielen_dir     	 | Verplicht 	 | Link naar de map met alle profielen.                                                                      |
| --output_path  	       | Verplicht 	 | 	Dit is de werkmap, waarin je de resultaten van de overslagsommen wilt uitvoeren. Belangrijk is dat deze map voorafgaand aan het runnen van het script al een map met de profielen bevat. Deze map met profielen moet de naam 'prfl' hebben. Naast de profielenmap, moet de map leeg zijn.                                                                                                                                                                                                                                                                                                     |


**Let op:** deze regel is vanuit elke directory te runnen, je hoeft dus niet eerst naar een bepaalde folder te gaan.

Bij deze workflow wordt via Python Hydra-Ring aangeroepen. Daarbij wordt een groot aantal probabilistische berekeningen uitgevoerd wat betekent dat het even kan duren. Wanneer dit niet handig is kan de workflow gedraaid worden op een aparte rekencomputer, of kunnen de berekeningen in delen worden gedraaid, bijvoorbeeld door slechts een deel van de regels in de csv in te vullen.

Om meer informatie over de code te krijgen, gebruik je: 
``` python -m preprocessing overflow --help ```

### Voorbeeld invoer: 
```
python -m preprocessing overflow --file_name “c:\VRM\test_hydraring_workflow_wdod\HR_default.csv” --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2023" --database_paths "c:\VRM\test_hydraring_workflow_wdod\HR\2100" --profielen_dir "c:\VRM\test_hydraring_workflow_wdod\Profielen" --hydraring_path "c:\Program Files (x86)\BOI\Riskeer 21.1.1.2\Application\Standalone\Deltares\HydraRing-20.1.3.10236" --output_path "c:\VRM\test_hydraring_workflow_wdod\overslag"
```