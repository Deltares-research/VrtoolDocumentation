# Binnenwaartse macrostabiliteit

Voor binnenwaarste macrostabiliteit kan de betrouwbaarheid bepaald worden op basis van directe invoer of op basis van D-Stability. 

## Directe invoer 
Bij de directe invoer voor binnenwaartse macrostabiliteit moet de betrouwbaarheid β op 1 tijdstip aangegeven worden. Het meenemen van tijdsafhankelijkheid is op dit moment niet ondersteund.

In sommige gevallen zijn verschillende scenario’s mogelijk. In dat geval is het mogelijk zowel de geaggregeerde β over alle scenario’s, als de β per scenario (incl. scenariokans) in te voeren.

## D-Stability
## D-Stability
Wanneer een *.stix file beschikbaar is kan deze worden gebruikt om de stabiliteitsberekening opnieuw te maken/aan te passen. 

Binnen de VRTOOL wordt gebruik gemaakt van D-Stability versie 2022.01.2. De stix files moeten daarmee compatibel zijn. Wanneer deze in een oudere versie van D-Stability zijn gemaakt dan moeten ze in de regel eerst worden geopend in D-Stability, en zonder wijzigingen worden opgeslagen. Dit moet voor elk scenario (indien van toepassing) wat wordt meegenomen in de berekening worden gedaan. 

In de VRTOOL worden parametrisch aanpassingen gedaan om versterkingen door te rekenen:
- Voor grondversterkingen wordt de geometrie aangepast o.b.v. de gewenste kruinverhoging en bermverbreding.
- Voor stabiliteitsschermen wordt een forbidden line toegevoegd bij de teen. Aanname is dat constructie stijf en voldoende sterk is.

Momenteel zijn aanpassingen van de buitenwaterstand en bijbehorend freatisch nog niet mogelijk. De betrouwbaarheid blijft dus, net als bij directe invoer constant in de tijd. 
