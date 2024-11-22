Optimalisatie van maatregelen op basis van veiligheidsrendement  
===============================================================

Bij een optimalisatie op basis van veiligheidsrendement worden helemaal geen eisen gesteld aan de faalkans op mechanisme- of doorsnede-/vakniveau. In plaats daarvan wordt gekeken naar de kosten en baten van maatregelen.


Invoer voor de optimalisatie
--------------------------------
De invoer voor de optimalisatie bestaat uit de faalkansen van de dijkvakken voor de verschillende mechanismen, en de kosten van en betrouwbaarheid na maatregelen. Op basis hiervan worden de kosten en baten van maatregelen bepaald, conform het hoofdstuk `Bepaling van kosten en baten <BepalingKostenBaten.html>`_. 



Opzet van het algoritme
--------------------------------
Binnen een veiligheidsrendementberekening wordt gezocht naar de combinatie van maatregelen met minimale totale kosten (overstromingsrisico & versterkingskosten). Omdat de omvang van het traject, en het aantal beschikbare maatregelen dit optimalisatieprobleem zeer groot maakt, wordt gebruik gemaakt van een benaderingsmethode. Het gebruikte algoritme is een lokale optimalisatie, deze is ontwikkeld en gevalideerd in het `NWO-programma All-Risk <https://www.sciencedirect.com/science/article/pii/S0951832020308346>`_. 

Bij deze rekenmethode wordt steeds, gegeven een bepaalde situatie (veiligheid van de dijkvakken en het traject als geheel), de beste maatregel bepaald. Dit wordt gedaan door de kosten en baten van de maatregelen te bepalen, en de maatregel te kiezen met de hoogste baten/kosten-verhouding (BC-ratio). Door dit stapsgewijs te doen wordt het punt met minimale totale kosten gevonden of in ieder geval zeer goed benaderd.

Daarbij zijn 2 methoden om de kosten-batenverhouding te bepalen:

1. De BC-ratio van elke individuele maatregel. Dit is gericht op maatregelen die de faalmechanismen beïnvloeden waarvoor vakken als onafhankelijk beschouwd worden. 
2. De BC-ratio van een combinatie van maatregelen. Dit is gericht op maatregelen die de faalmechanismen beïnvloeden waarvoor vakken als afhankelijk beschouwd worden, dus voor overloop/overslag en bekleding. 

Vervolgens wordt gekeken welke maatregel het gunstigste is. Daarbij wordt eerst gekeken of de kosten-batenverhouding van een combinatie hoger is dan die van een individuele maatregel. Als dat het geval is, wordt de combinatie gekozen. Als dat niet het geval is, wordt de individuele maatregel gekozen. Daarbij wordt de maatregel gekozen op het dijkvak met de gunstigste maatregel waarvan de kosten-batenverhouding een factor 1,5 gunstiger is dan de beste maatregel op de andere vakken. 

.. tip::
   NB: de factor 1,5 is configureerbaar door in config.json de waarde van 'f_cautious' aan te passen. Echter, in de wetenschappelijke publicatie is deze waarde onderzocht en 1,5 blijkt daarin het beste te werken.


De optimalisatieberekening gaat door tot de BC-ratio van de beste maatregel < 0,1 is, of het maximaal aantal iteraties (600) is bereikt. In het algemeen leidt het stopcriterium er toe dat er een economisch optimum wordt gevonden. Dit economisch optimum betekent niet per definitie dat de norm wordt gehaald, maar meestal is dit wel het geval. Denkbare uitzonderingen zijn trajecten waar de norm voor Lokaal Individueel Risico strenger is dan de MKBA norm. 

Regelmatig komt het zelfs voor dat verder dan de norm versterken economisch aantrekkelijk is. In het dashboard kan er dan voor gekozen worden ofwel te werken met de economisch optimale set maatregelen, ofwel te kiezen voor een oplossing die voldoet aan een bepaalde kans in een gegeven jaar. In feite wordt dan voor een andere doelfunctie gekozen: in plaats van `optimale dijkversterking op basis van totale kosten`, gaat het dan om de `dijkversterking met minimale totale kosten gegeven een specifieke kans in een gegeven jaar`. In het onderliggende `paper <https://www.sciencedirect.com/science/article/pii/S0951832020308346>`_ is onderbouwd dat het optimalisatiepad (de stapsgewijze reeks van maatregelen) ongeveer het Pareto front van de oplossing vormt voor totaal risico en totale kosten. Daarom zullen de dan gekozen maatregelen dicht bij het optimum liggen voor de iets andere doelfunctie.

.. note::
   **Bepaling van de kosten-batenverhouding**
   
   *Combinaties van maatregelen*

   Voor overloop/overslag en bekleding is het voor een betrouwbaar resultaat noodzakelijk om maatregelen te combineren. Dit valt eenvoudig te illustreren aan de hand van het volgende voorbeeld: een dijktraject met 2 dijkvakken heeft een faalkans van 1/100 voor overslag voor beide dijkvakken, de trajectfaalkans is daarmee ook 1/100. Wanneer op dijkvak A de kruin wordt versterkt (bijv. tot een faalkans van 1/1000), is de faalkans nog steeds 1/100, dijkvak B is immers niet versterkt, en het zwakste vak bepaalt de trajectfaalkans. Binnen de optimalisatie wordt daarom in 100 stappen gezocht naar de beste combinaties van maatregelen, daarbij wordt telkens het zwakste vak versterkt. In dit geval zou alleen kijken naar individuele maatregelen dus zorgen voor een lokaal optimum voor overloop/overslag, omdat er nooit een individuele maatregel wordt gekozen. In onderstaande tabel is een voorbeeld weergegeven waarbij is aangenomen dat om beurten de dijkvakken een factor 10 veiliger worden gemaakt, dit kost 1 miljoen euro per dijkvak. Te zien is dat het risico slechts 1 keer per 2 stappen wordt verlaagd. In dit geval heeft de combinatie van maatregelen waarbij beide vakken een factor 10 veiliger worden de gunstigste kosten-batenverhouding (450).

   .. csv-table:: Rekenvoorbeeld voor het combineren van maatregelen
      :file: rekenvoorbeeld_combinatie.csv
      :widths: 10,10,10,10,10,10
      :header-rows: 2


   *Keuze van een individuele maatregel*

   Op vak A heeft een pipingmaatregel een BC-ratio van 10000. Eventueel uitbreiden met een kleine of grotere berm verlaagt de BC-ratio naar 3000 of 1200. Op vak B heeft de gunstigste maatregel een BC-ratio van 1000. In dit geval wordt de op vak A gekozen voor een pipingmaatregel met kleine berm (BC=3000), omdat deze meer dan een factor 1.5 gunstiger is dan de beste maatregel op vak B. In een vervolgstap worden vervolgens gegeven de uitgangssituatie met pipingmaatregel op vak A de BC-ratio's opnieuw bepaald, en wordt opnieuw de beste maatregel gekozen. Zo wordt iteratief de combinatie van maatregelen bepaald die leidt tot minimale totale kosten.



