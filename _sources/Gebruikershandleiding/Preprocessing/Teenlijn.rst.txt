**NB: Dit gedeelte is niet up-to-date en wordt in de komende weken
aangepast**

Afleiden teenlijn
=================
Met de workflow ``genereer_teenlijn`` wordt de binnenteenlijn van een dijktraject bepaald. Dit is belangrijke invoer voor de bepaling van de bebouwing. De teenlijn wordt weggeschreven naar `teenlijn_geojson`.

De workflow kan worden gestart met het volgende commando:

::

   python -m preprocessing genereer_teenlijn --config_file {config_bestand}

De teenlijn wordt gebaseerd op de locaties van de binnentenen van alle profielen in `karakteristieke_profielen_map`. Tussen de teenpunten wordt een rechte lijn getrokken. Vaak resulteert dit op sommige plekken in een wat kartelige teenlijn. Het is daarom aan te bevelen om na het draaien van de workflow de teenlijn te controleren in ArcGIS of QGIS en handmatig aan te passen waar nodig.

.. tip:: 
   Bij het genereren en selecteren van de profielen is onderdeel van de workflow om handmatig de profielen te controleren en slechte profielen te verwijderen. Het is aan te bevelen om dit te doen voordat de teenlijn wordt afgeleid zodat hier minder onnauwkeurigheid in optreedt.