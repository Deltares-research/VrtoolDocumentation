# Rekenen met de VRTOOL

De VRTool kan op twee manieren worden gedraaid:
* Via het environment van de [preprocessor](../Installaties/VRUtils.md). Deze bevat altijd de laatste VRTOOL release, zie hiervoor de pagina over [werken met de preprocessor](../Preprocessing/werken_met_preprocessor.md).
* Door de [VRTOOL](../Installaties/VRTool.md) als aparte package te installeren.
    
In beide gevallen kan de VRTool daarna worden aangeroepen met de CLI van Anaconda en de volgende commando: 
```
python -m vrtool {desired_run} {MODEL_DIRECTORY}
```

Vervang ```{desired_run}``` met de gewenste berekening. Hierbij kan worden gekozen voor één van de drie stappen van de [veiligheidsrendementberekning](Opzet%20van%20een%20berekening.md) of alle drie tegelijk: 
- ```assessment```: hiermee wordt alleen de beoordeling/projectie van de huidige veiligheid uitgevoerd
- ```measures```: hiermee worden de maatregelen per dijkvak doorgerekend
- ```optimization```: hiermee wordt alleen de optimalisatie van maatregelen voor dijktrajecten uitgevoerd
- ```run_full```: hiermee worden alle drie de stappen doorgerekend

Vervang ```{MODEL_DIRECTORY}``` met het path naar de database (.db) en config bestand (.json) uit de preprocessor, zie foto hieronder. Beide bestanden worden automatisch gegenereerd via de preprocessor, zie [Genereren database](../Preprocessing/Genereren_database.md). 

![](TweeBestanden_Preprocessing.PNG)

# Belangrijke instellingen 
* Dit aanvullen na afronding van issue VRTOOL-261.*

# Advies werkwijze

* Draai eerst assessment workflow en controleer de invoer voor de beoordeling + projectie.
* Draai daarna de run_full workflow: dan wordt het hele traject doorgerekend met maatregelen in 2025 (en 2045 (nog bekijken voor v0.1)).
* Laad de database met resultaten in het [dashboard](../Postprocessing/WeergevenResultaten.md) en werk hierin verder. Met het dashboard kunnen (vanaf versie 0.1) [nieuwe optimalisaties worden uitgevoerd](../Postprocessing/BerekeningenMetDashboard.md).

# Beoordelen van resultaten
Vullen we later aan:
    * Hoe herken je een lokaal optimum? (a.d.h.v. investeringspad wat 'blijft hangen')
    * Is de betrouwbaarheid van maatregelen realistisch?
    


