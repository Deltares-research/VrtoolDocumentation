Binnenwaartse macrostabiliteit
==============================

Voor binnenwaartse macrostabiliteit kan de betrouwbaarheid bepaald worden op basis van directe invoer of op basis van D-Stability.

Directe invoer
--------------

Bij de directe invoer voor binnenwaartse macrostabiliteit moet de betrouwbaarheid β of de stabiliteitsfactor uit een semi-probabilistische beoordeling op 1 tijdstip aangegeven worden. Omdat stabiliteitsfactoren vaak redelijk tijdsonafhankelijk zijn is tijdsafhankelijkheid hier (nog) niet geïmplementeerd.

In sommige gevallen zijn verschillende scenario’s van toepassing. In dat geval is het mogelijk zowel de geaggregeerde β over alle scenario’s, als de β per scenario (incl. scenariokans) in te voeren. Voor de berekening maakt dit verder niet uit.

De effecten van maatregelen worden nader toegelicht in de betreffende paragrafen in de sectie `Maatregelen <../Maatregelen/index.html>`_


D-Stability
-----------

Wanneer een \*.stix file beschikbaar is kan deze worden gebruikt om de stabiliteitsberekening opnieuw te maken/aan te passen. De verwijzing naar de stix-files moet via het csv-bestand worden toegevoegd bij het maken van de database. Vervolgens moeten de stix-bestanden in een folder `stix` naast de database worden geplaatst. 

Binnen de VRTOOL wordt gebruik gemaakt van D-Stability versie 2024. De stix files moeten daarmee compatibel zijn. Wanneer deze in een oudere versie van D-Stability zijn gemaakt dan moeten ze in de regel eerst worden geopend in D-Stability, en zonder wijzigingen worden opgeslagen. Dit moet voor elk scenario (indien van toepassing) dat wordt meegenomen in de berekening worden gedaan. Daarnaast moet in de config verwezen worden naar de locatie van D-Stability, specifiek het bestand `D-Stability Console.exe`. Dit kan door een regel toe te voegen in de config file, bijvoorbeeld:

```"externals": "C:/Program Files/D-Stability 2024.01/D-Stability Console.exe"``` 

In de VRTOOL worden parametrisch aanpassingen gedaan om versterkingen door te rekenen: 

* Voor grondversterkingen wordt de geometrie aangepast o.b.v. de gewenste kruinverhoging en bermverbreding. 
* Voor stabiliteitsschermen wordt een forbidden line toegevoegd bij de teen. Aanname is dat constructie stijf en voldoende sterk is.

Momenteel zijn aanpassingen van de buitenwaterstand en bijbehorend freatisch vlak nog niet mogelijk. De betrouwbaarheid blijft dus, net als bij directe invoer, constant in de tijd.