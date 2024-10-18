Custom maatregelen
==================
In aanvulling op de standaard geparametriseerde maatregelen is het ook mogelijk om handmatig extra maatregelen toe te voegen.
Dat kan via de database, of via een eigen routine waarbij op basis van een csv-bestand een lijst maatregelen wordt toegevoegd. In de toekomst wordt dit ook vanuit het dashboard gefaciliteerd. 

Het idee van custom maatregelen is dat het mogelijk wordt om in latere fasen van een project voorkeursalternatieven mee te wegen, of in gevallen waar de standaardmaatregelen incorrect zijn verbeterde resultaten toe te voegen. In onderstaande tabel is een voorbeeld gegeven van een divers aantal custom maatregelen op een dijkvak. We lopen deze stapsgewijs af om de invoer toe te lichten:

* De eerste maatregel is een `Keermuur`. Deze heeft enkel invloed op overslag, kost 500.000 €, en verhoogt de betrouwbaarheidsindex naar 5 in jaar 0 (2025), wat afneemt naar 4,6 in jaar 100 (2125). In dit geval wordt voor andere mechanismen aangenomen dat de veiligheid gelijk blijft. De maatregel is `combinable` wat wel betekent dat deze gecombineerd kan worden (bijvoorbeeld met een pipingmaatregel).
* De tweede maatregel is een combinatie van kruinverbreding en verhoging. Deze maatregel is niet combineerbaar met andere maatregelen (type `full`). Voor overslag is de betrouwbaarheidsindex voor verschillende jaren gegeven, maar voor stabiliteit niet. Dat betekent dat er van uit wordt gegaan dat de stabiliteit constant is in de tijd. 
* De derde maatregel is een `Mangrove`. Deze beïnvloedt de faalkans van de bekleding (invloed op overslag is hier niet meegenomen). Daarom heeft deze als type `revetment`. Ook in dit geval is voor meerdere jaren de betrouwbaarheidsindex gegeven.
* De vierde maatregel is een inkassing van het voorland. Dit is een maatregel die enkel de pipingveiligheid verhoogt, en deze kan worden gecombineerd met andere maatregelen (bijv. een berm). Daarom is deze maatregel `partial`. De betrouwbaarheidsindex is gegeven voor verschillende jaren, maar niet voor het volledige bereik. Voor het opgegeven bereik wordt de betrouwbaarheidsindex geïnterpoleerd. Voor de jaren na het bereik (in dit geval 76 tot 100) wordt de betrouwbaarheid gelijk gehouden aan die van jaar 75, voor de jaren daarvoor (0 tot 11) wordt die van jaar 12 aangehouden.
* De vijfde maatregel is het plaatsen van een kwelscherm in een oude stadsmuur. Op dergelijke locaties zijn de generieke maatregelen uit de VRTOOL niet toepasbaar en bieden custom maatregelen de mogelijkheid toch maatregelen mee te nemen. De ingevoerde maatregel beinvloedt alleen piping en heeft type `full` en kan dus niet gecombineerd worden. De betrouwbaarheidsindex wordt voor alle jaren 7,3 voor piping. 

.. csv-table:: Voorbeeld invoer custom maatregelen
    :file: tables/custom_measure_example.csv
    :widths: 30, 5, 5, 5, 5, 5, 5
    :header-rows: 1

Via het dashboard kunnen ook maatregelen worden verwijderd uit de database. Dit kan ook via de functies `safe_clear_custom_measure` en `brute_clear_custom_measure`. Bij de tweede optie heeft dit wel consequenties voor de resultaten omdat ook maatregelen worden verwijderd die voorkomen in oude optimalisatieberekeningen. Deze kunnen dan mogelijk niet goed meer worden weergegeven. Bij het werken met custom maatregelen is het altijd raadzaam om regelmatig de database te backuppen om dergelijke problemen te voorkomen.
