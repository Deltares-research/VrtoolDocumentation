**NB: Dit gedeelte is niet up-to-date en wordt in de komende weken
aangepast**

Genereren database
==================

Met de workflow ``maak_database`` kan een invoerdatabase voor de VRTOOL
worden gegenereerd. Daarbij moeten de met de overige workflows
gegenereerde bestanden als invoer worden opgegeven. Wanneer de voorgaande workflows niet goed zijn uitgevoerd is het niet mogelijk om een goede database te maken. 

De workflow kan worden aangeroepen met het volgende commando:

::

   python -m preprocessing maak_database --config_file {config_bestand}

Een database kan alleen worden aangemaakt als de daarvoor bestemde directory leeg is. Naast een database wordt ook de geojson van de vakindeling weggeschreven, alsmede een config.json bestand voor de VRTOOL.

Structuur van de database
-------------------------
De structuur van de database is onderstaand weergegeven. De database is in SQLite formaat en kan worden geopend met bijvoorbeeld DB Browser for SQLite. Dit is te downloaden via `deze link <https://sqlitebrowser.org/>`_.

<toelichting m.b.t. de tabellen wordt later toegevoegd>

.. image:: img/vrtool_sql_input.drawio.png
    :alt: Diagram van de structuur van de database
    :align: center