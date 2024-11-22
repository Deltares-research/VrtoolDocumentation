Afleiden dijkprofielen en karakteristieke punten
================================================

Met de workflow ``genereer_dijkprofielen`` worden voor een gegeven traject elke x meter dijkprofielen gegenereerd op basis van het AHN4.
Voor elk van deze profielen worden de karakteristieke punten afgeleid: 2 punten op de kruin, en op zowel het buiten- als het binnentalud beide
maximaal 3 punten. Vervolgens kan met de workflow ``selecteer_profiel`` voor verschillende dijkvakken het meest representatieve profiel worden
geselecteerd. Deze representatieve profielen zijn nodig voor het bepalen van het volume grond bij een kruinverhoging en/of bermverbreding. 

Genereren van dijkprofielen op basis van het AHN4
-------------------------------------------------
Het genereren van profielen kan worden gedaan met het volgende commando:

::

   python -m preprocessing genereer_dijkprofielen --config_file {config_bestand}

De workflow ``genereer dijkprofielen`` bevat 2 stappen, die achter elkaar worden uitgevoerd als de workflow wordt aangeroepen: eerst worden de AHN profielen afgeleid, daarna worden de karakteristieke punten bepaald.

In `output_map_ahn_profielen` worden profielen uit AHN4 weggeschreven naar csv-bestanden. Dit is een submap van `output_map_profielen`. In `output_map_profielen` wordt ook een overzicht opgeslagen met informatie over elk profiel (m-waarde, naam CSV-bestand, x- en y-coördinaten van het uiterste punt op het voorland en het achterland): ``traject_profiles.csv``. 

In `karakteristieke_profielen_map` wordt voor elk AHN-profiel karakteristieke (knik)punten weggeschreven Hierin wordt per profiel een figuur (profielnaam.png) weggeschreven met daarin het profiel en het karakteristieke profiel. Er wordt ook een CSV-bestand (profielnaam.csv) weggeschreven met daarin de gevonden  karakteristieke punten voor het desbetreffende profiel. 

*Let op*: Er is geen invoerbestand bij deze workflow, de gegevens uit het AHN4 worden automatisch opgehaald.

.. topic:: Aandachtspunten 
   
   * Niet voor alle AHN4 profielen kunnen karakteristieke punten worden bepaald. Soms passen deze simpelweg niet op de geometrie. Na het uitvoeren van de workflow is het daarom aan te bevelen om de profielen te controleren. Profielen die niet goed zijn, kunnen worden verwijderd (door de figuur te verwijderen) en worden dan in de volgende stap niet meegenomen. 

   * Met de parameter `dx` in het invoerbestand kan de afstand tussen de profielen worden aangepast. Default is deze 25 meter en het advies is dit niet aan te passen tenzij er duidelijke redenen voor zijn. 

Selecteren van het meest representatieve profiel per dijkvak
------------------------------------------------------------

Op basis van de profielen die met ``genereer_dijkprofielen`` zijn afgeleid kan vervolgens per vak het meest representatieve profiel worden geselecteerd. Daarvoor wordt de eerder afgeleide vakindeling gebruikt. Deze workflow kan worden aangeroepen met het volgende commando:

::

   python -m preprocessing selecteer_profiel --config_file {config_bestand}

Daarbij wordt gekeken welke profielen uit de `karakteristieke_profielen_map` binnen het dijkvak vallen. Vervolgens wordt op basis hiervan een representatief profiel bepaald. Wanneer geen profiel beschikbaar is wordt niks weggeschreven.

De resulterende profielen zoals die moeten worden gebruikt in de database worden weggeschreven in `karakteristieke_profielen_csv`. Dit bestand kan voor sommige vakken geen profielen bevatten. Deze moeten handmatig worden aangevuld. Een makkelijke manier is om het naastgelegen profiel te hanteren.

.. topic:: Aandachtspunten

   * Voor elk vak moet een profiel aanwezig zijn. Wanneer dit niet het geval is, kan geen database worden gegenereerd.

   * De nauwkeurigheid van het profiel heeft maar beperkte invloed op de resultaten van de veiligheidsrendementberekeningen. Het is daarom niet nodig om voor elk vak een zeer nauwkeurig profiel te hebben. Eventuele afwijkingen resulteren vooral in iets verkeerd geschatte grondvolumes voor de versterking, maar meestal is dit van marginale betekenis voor de totale versterkingskosten omdat hierin aanwezige bebouwing rond de dijk en het plaatsen van constructies veel zwaarder meewegen.