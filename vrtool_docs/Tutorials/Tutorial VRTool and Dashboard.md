
# Tutorial VRTool and Dashboard


Deze tutorial bevat een introductie om tot de eerste berekeningen met de VRTool te komen. Vervolgens kunnen de resultaten worden bekeken met behulp van het Dashboard.
Voor deze tutorial wordt gebruikt gemaakt van een casus (dijktraject 24-3). 

**Rekenen met VRTool** 

1. Download de bestanden via deze [link](https://www.sharepoint.nl) en sla ze op in de folder ``"C:\Veiligheidsrendement\Tutorial"`` (gebruik hiervoor dezelfde folder die tijdens de [Installaties](../Installaties/index.rst) is gemaakt).

In de map staan nu de volgende bestanden:
- ``config.json``: Met instellingen van de berekening
- ``24-3_database.db``: De invoer en uitvoer van de betreffende berekening
- ``24-3.geojson``: Hiermee kunnen de resultaten op kaart weergegeven worden

 *NB: de preprocessing, het genereren van de juiste bestanden van een traject, gaat vooraf aan het rekenen met de VRTool. In deze tutorial zijn de hierboven gedownloade bestanden een eindresultaat van de preprocessing.*

het bestand `24-3_database.db` is de database welke we gaan vullen door met de VRTool te rekenen. 

2. Open `Anaconda <https://www.anaconda.com/download>`_ en roep de VRTool aan met de volgende commando: 
``python -m vrtool {desired_run} {MODEL_DIRECTORY}``. 

Vervang ``{desired_run}`` met de gewenste berekening. Hierbij kan worden gekozen voor één van de drie stappen van de veiligheidsrendementberekening of alle drie tegelijk:

- ``assessment``: Hiermee wordt alleen de beoordeling/projectie van de huidige veiligheid uitgevoerd.
- ``measures``: Hiermee worden de maatregelen per dijkvak doorgerekend.
- ``optimization``: Hiermee wordt alleen de optimalisatie van maatregelen voor dijktrajecten uitgevoerd.
- ``run_full``: Hiermee worden alle drie de stappen in een keer doorgerekend.

vervang ``{MODEL_DIRECTORY}`` met het path naar de database (.db) en config bestand (.json). (waarschijnlijk  ``"C:\Veiligheidsrendement\Tutorial"``). 

```
Voorbeeld commando: python -m vrtool run_full C:\Veiligheidsrendement\Tutorial
```

*NB: De berekening kan enkele minuten duren afhankelijk van welke desired_run er gekozen is. Het spreekt voor zich dat de run_full het langst duurt.*

**Dashboard gebruiken**

Nu de VRTool verschillende berekeningen heeft gedaan kunnen we de rekenresultaten laten zien met het Dashboard.

3.  In Anaconda, run ``python -m src.index`` om het dashboard te starten. Het dashboard verschijnt nu automatisch in de browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser. (Mocht dit niet werken omdat je nog niet alle packages hebt geinstalleerd, volg dan eerst de [Installaties](../Installaties/index.rst) instructies.)

afhankelijk van de folder waarin je uitpakt moet je de padnamen in het ``config.json`` aanpassen.

4. Open het ``config.json`` bestand in ``Notepad``. Je ziet nu een tekst bestand met bij ``input_directory`` de padnaam (''C:/..../...''). Deze padnaam moet gelijk zijn aan waar het config bestand staat. Kopieer de padnaam (waarschijnlijk ''C:\Veiligheidsrendement\Tutorial'') en pas dit bij input_directory aan. Let op dat je ``/`` gebruikt in plaats van ``\``.
![](config.png)

5. Ga nu naar de browser waar het Dashboard geopend is. Sleep het ``config.json`` bestand naar het vak ''traject selectie''. De resultaten worden nu ingeladen. 
![](Traject_selectie.png)

Uiteindelijk zit je Dashboard er als volgt uit:
![](voorbeeldDashboard.png)

**Oefenvraag:**
```
Welk dijkvak heeft in 2050 voor de beoordeling een Beta van 3.5 voor stabiliteit?

Antwoord: Dijkvak 24
```
In [Werken met het dashboard](../Gebruikershandleiding/Postprocessing/index.rst) volgt een gedetaileerde uitleg van de verschillende tabbladen in het dashboard en hoe er verder mee gewerkt kan worden.

