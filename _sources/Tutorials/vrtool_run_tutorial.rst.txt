VRTOOL - uitvoeren van berekeningen
===================================

1. Download de bestanden via deze `link <https://github.com/Deltares-research/VrtoolDocumentation/raw/main/vrtool_docs/Bestanden/Tutorial/24-3.zip>`_ en pak ze uit in de folder ``"C:\Veiligheidsrendement\Tutorial"`` (gebruik hiervoor dezelfde folder die tijdens de `installatie <../Installaties/index.rst>`_ is gemaakt).

   In de map staan nu de volgende bestanden:

   - ``config.json``: Dit bestand bevat instellingen voor de berekening met de VRTOOL
   - ``24-3_database.db``: De invoer en uitvoer van de betreffende berekening
   - ``24-3.geojson``: Hiermee kunnen de resultaten op kaart weergegeven worden

2. Open Anaconda Prompt, activeer het environment, en roep de VRTool aan met het volgende commando::

       python -m vrtool {desired_run} {config_file}

   Vervang ``{desired_run}`` met de gewenste berekening. Hierbij kan worden gekozen voor één van de drie stappen van de veiligheidsrendementberekening of alle drie tegelijk:

   - ``assessment``: Hiermee wordt alleen de beoordeling/projectie van de huidige veiligheid uitgevoerd.
   - ``measures``: Hiermee worden de maatregelen per dijkvak doorgerekend.
   - ``optimization``: Hiermee wordt alleen de optimalisatie van maatregelen voor dijktrajecten uitgevoerd.
   - ``run_full``: Hiermee worden alle drie de stappen in een keer doorgerekend.

   Vervang ``{config_file}`` met het pad naar het gewenste config bestand (.json). (waarschijnlijk ``"C:\Veiligheidsrendement\Tutorial\config.json"``).

   Bijvoorbeeld