Berekeningen aansturen via het dashboard
========================================

Vanuit het dashboard kunnen nieuwe berekeningen worden aangestuurd. Daarvoor moet eerst een database met resultaten van een basisberekening worden geïmporteerd. Vervolgens kan met het dashboard een nieuwe berekening worden geconfigureerd. De pagina hiervoor is te benaderen door bovenin bij `paginas` te kiezen voor `Draaien optimalisatieberekeningen`. Zie ook onderstaand screenshot.

.. figure:: img/berekening_dashboard_1.png
    :width: 50%
    :align: center

Aan- en uitzetten van maatregelen
----------------------------------

Via het tabblad `Run Optimize` kan met de knoppen een nieuwe berekening worden geconfigureerd. In onderstaand voorbeeld is bijvoorbeeld aangegeven dat op dijkvak 3 alleen een grondversterking kan worden uitgevoerd, en op dijkvakken 4 t/m 8 geen versterking. Op dijkvak 3 kan ook alleen in het jaar 2030 worden versterkt.

.. figure:: img/instellingen_dashboard_berekening.png
    :width: 100%
    :align: center

De berekening is `Aangepaste optimalisatie v0.1` genoemd. De berekening kan worden gestart door op de knop `Start optimalisatieberekening` te klikken. De berekening wordt nu gestart en de voortgang is te volgen in de live logging. Een berekening kan enige tijd duren, de voortgang wordt gelogd in een pop-up scherm zoals hieronder weergegeven. Hier is bijvoorbeeld te zien dat er in stap 2 van de berekening een maatregel is gekozen met een BC-ratio van 11381.77.

.. figure:: img/live_logging.png
    :width: 50%
    :align: center

.. tip::
    Met name het importeren van alle gegevens kan even tijd kosten. Daardoor kan het soms even duren voordat er logging verschijnt. Dat betekent echter niet dat er niets gebeurt op de achtergrond. Als er linksboven op de pagina `updating...` staat, dan is de berekening bezig.

De duur van de berekening is sterk afhankelijk van de computer waarop deze wordt uitgevoerd, en het aantal maatregelen en dijkvakken dat wordt meegenomen in de berekening. In het algemeen duurt het optimalisatiedeel van de berekeningen wel meer dan 5 minuten per analyse (tot circa 1 uur voor trajecten met veel dijkvakken en maatregelen). Een berekening is klaar als dit wordt aangegeven in het venster, en als er in het tabblad in de browser geen `updating...` meer staat.

.. tip::
    Het draaien van een berekening vanuit het dashboard kan alleen worden uitgevoerd als eerst in ieder geval ``measures`` is doorgerekend omdat er gegevens over de maatregelen beschikbaar moeten zijn. Zie ook `hier <../VRTool/index.html#uitvoeren-van-een-berekening>`_.

Het draaien van aangepaste berekeningen kan handig zijn wanneer:

* Met een specifiek versterkingsjaar moet worden gerekend (voor bepaalde dijkvakken). Het kan dan inzicht geven in de mate waarop de timing van de maatregelen de maatregelen op het betreffende vak of andere vakken beïnvloedt.
* Een specifieke maatregel moet worden uitgezet of afgedwongen. Dit kan bijvoorbeeld zijn omdat een maatregel niet mogelijk is door beperkingen die niet anderszins worden meegenomen, of omdat vanuit omgeving juist een specifiek type maatregel wenselijk is.
* Men wil kijken naar het beperken van de geografische scope door specifieke dijkvakken uit te zetten en daarmee uit te sluiten van versterking.


Werken met custom maatregelen
-----------------------------
Naast het rekenen met de standaard maatregelen is het ook mogelijk om met custom maatregelen te rekenen. Of deze moeten worden meegenomen kan in het tabblad `Run optimize` worden aangevinkt. Dit kan bijvoorbeeld handig zijn wanneer er een specifieke maatregel moet worden meegenomen die niet in de standaard set zit. Denk aan een specifieke maatwerkoplossing op een bepaald dijkvak. Custom maatregelen kunnen worden ingevoerd in het tabblad ``Custom maatregelen``. Hier is een tabel zichtbaar zoals in onderstaande figuur waarin de maatregelen die in de database staan zijn weergegeven. In dit geval staan er 2 custom maatregelen in de database: maatregel `Test 1` op vak 24, en `Test 2` op vak 23.

.. figure:: img/custom_measure_interface.png
    :width: 80%
    :align: center

Voor beide maatregelen zijn kosten & betrouwbaarheid ingevoerd. Voor de kosten geldt dat bij `Test 1` 2 verschillende bedragen zijn ingevoerd. In dat geval neemt de VRTOOL het eerste bedrag uit de tabel ``CustomMeasureDetail`` in de database. De betrouwbaarheid van de maatregel wordt ingevoerd voor verschillende jaren en mechanismen. Daarbij worden de getallen in de tabel geinterpreteerd als in onderstaande figuur. Wanneer niets wordt ingevoerd wordt aangenomen dat de betrouwbaarheid gelijk blijft. Custom maatregelen worden niet gecombineerd met andere maatregelen.

.. warning::
    Het advies is om goed te controleren of de kosten van de maatregel goed zijn ingevoerd: wanneer er verschillende bedragen zijn ingevoerd, wordt alleen het eerste bedrag meegenomen in de berekening. Dit kan leiden tot onjuiste resultaten.

.. figure:: img/custom_measure_concept.png
    :width: 80%
    :align: center

Het invoeren van custom maatregelen gaat via een csv-bestand. Dit csv-bestand moet de volgende kolommen bevatten:

* Maatregel: de naam van de maatregel. Op basis hiervan worden verschillende regels voor dezelfde maatregel aan elkaar gekoppeld in de database.
* Dijkvaknaam: het dijkvak waarop de maatregel van toepassing is. Dit moet overeenkomen met de naam van een dijkvak in de database.
* Mechanisme: het mechanisme waarop de regel van de maatregel van toepassing is. Toegestane waarden zijn: Stabiliteit, Piping, Overslag en Bekleding.
* Tijd: het tijdstip waarop de regel van toepassing is. Dit moet een waarde tussen 0 en 100 zijn.
* Kosten: de kosten van de maatregel. Dit moet een positief getal zijn. Let op dat alle kosten voor dezelfde maatregel gelijk zijn. Alleen de eerste waarde wordt meegenomen in de berekening.
* Betrouwbaarheidsindex: de betrouwbaarheidsindex van de maatregel.

Na het vullen van het csv-bestand kan deze worden geupload via het blok in de interface. Daarna worden alle maatregelen in de database weergegeven in de tabel. De wijze waarop deze in de database zijn opgeslagen is terug te vinden door de SQLite te openen in een database viewer. In de tabel ``CustomMeasureDetail`` zijn de ingevoerde waarden te zien. In de tabellen ``MeasureResultMechanism`` en ``MeasureResultSection`` is te zien hoe de betrouwbaarheidsindex en kosten zijn geinterpreteerd.

.. figure:: img/custom_measure_sqlite.png
    :width: 80%
    :align: center

.. admonition:: Basisregels bij het toevoegen van maatregelen

    1. Bij het toevoegen van nieuwe custom maatregelen wordt altijd een backup van de database gemaakt. Deze is terug te vinden in de folder van de originele database.
    2. Als de naam van een maatregel al bestaat wordt deze niet opnieuw toegevoegd. Dus ook als een deel van de invoer (bijv. de kosten) wordt aangepast wordt dit niet aangepast.
    3. De kosten van de maatregel moeten gelijk zijn voor alle regels. Als dit niet zo is wordt alleen de eerste waarde meegenomen in de berekening.
    4. Als een deel van de maatregel(namen) al bestaat worden deze maatregelen niet toegevoegd, de andere maatregelen in de csv wel.
    5. Met de knop ``Verwijder alle custom maatregelen uit database`` kunnen custom maatregelen worden verwijderd. Dit is een ``safe`` verwijdering: alle maatregelen die zijn gebruikt in een berekening blijven bestaan. Onder de knop wordt weergegeven hoeveel maatregelen er zijn verwijderd. Wanneer er daadwerkelijk foute maatregelen zijn toegevoegd kan de database worden hersteld vanuit de automatisch gemaakte backup. 

.. tip::
    Het is ook mogelijk om de maatregelen handmatig uit de database te verwijderen. Open daarvoor de SQLite browser, en verwijder de maatregelen in de tabel ``Measure``. Het kan wel zijn dat oude rekenresultaten dan niet goed worden weergegeven. In dat geval moeten ook alle resultaten worden verwijderd, bijvoorbeeld door een nieuwe berekening te starten met `run_full` of `measures`.