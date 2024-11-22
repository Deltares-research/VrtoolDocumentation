Overslag
========

Ook voor overslag worden net als voor waterstand middels Hydra-Ring nieuwe overloop/overslag
berekeningen gemaakt voor de jaren 2023 en 2100. Daarbij wordt voor verschillende kruinhoogtes de
faalkans voor overslag bepaald. Vóór het draaien van deze workflow moet
eerst een invoerbestand ingevuld worden. Dit invoerbestand is identiek
aan die voor `waterstanden <Waterstand.html>`_.

Structuur van het invoerbestand van de overslagberekeningen
-----------------------------------------------

De basis voor het genereren van berekeningen voor waterstand en overslag
is het invoerbestand ``HR_default.csv``. Dit bestand is terug te vinden
in: ``C:\Veiligheidsrendement\.env\Lib\site-packages\preprocessing\default_files``.

Doel van de workflow is om voor elk dijkvak de relatie tussen faalkans en kruinhoogte af te leiden voor de jaren 2023 en 2100. 

Het invoerbestand ``HR_default.csv`` heeft de volgende kolommen die ingevuld moeten worden:

.. csv-table:: Kolommen in invoerbestand waterstand & overslag
  :file: tables/hr_kolommen.csv
  :widths: 15, 15, 50
  :header-rows: 1

.. topic:: Aandachtspunten

   * De kolommen ``bovengrens`` en ``ondergrens`` zijn voor de overslagberekeningen niet relevant. 

   * De kolom ``m_value`` is niet meer in gebruik en zal in een toekomstige versie worden verwijderd.

   * De waarden in de kolom ``doorsnede`` moeten overeenkomen met die in de kolom ``overslag`` in de `vakindeling <Vakindeling.html>`__.

Het vullen van het invoerbestand
-------------------------------
Voor het bepalen van de faalkansen voor overslag moet per dijkvak 1 locatie worden opgegeven. In de beoordeling zijn door beheerders vaak waterstands- en overslagberekeningen gemaakt op doorsneden op 100 meter afstand tot elkaar. Dit is voor veiligheidsrendement niet nodig. Het advies is om voor elk vak de maatgevende locatie voor overslag te kiezen, en deze locatie ook te gebruiken voor waterstandsberekeningen.

Voor overslag moet een aantal specifieke parameters worden opgegeven in het invoerbestand. Deze parameters zijn:

* ``prfl_bestand`` verwijst naar een `*.prfl` bestand met de doorsnede van het dijkvak. Dit bestand moet in de map met profielen staan.

* ``orientatie`` verwijst naar de orientatie van de doorsnede. Deze wordt gelezen uit het `*.prfl` bestand en dit is daarom een optionele kolom.

* ``dijkhoogte`` verwijst naar de hoogte van de dijk. Deze wordt gelezen uit het `*.prfl` bestand en dit is daarom een optionele kolom voor deze workflow. Echter, voor het maken van de database is deze wel nodig. Dit wordt in een toekomstige versie aangepast.

* ``zodeklasse`` en ``bovengrens_golfhoogteklasse`` verwijzen naar de zodeklasse van de dijk en de gegeven de hydraulische condities geldende kansverdeling voor het kritisch overslagdebiet. De mogelijke zodeklassen zijn te vinden bij de achtergronden van het `faalkansmodel <../../Achtergronden/Faalkansmodellen/Overslag.html>`_.

Op basis van de invoer wordt voor dijkhoogtes van 1 meter onder tot 2 meter boven de huidige kruinhoogte, met tussenstappen van 25 centimeter de faalkans bepaald. Dit is invoer voor de VRTOOL.

.. topic:: Aandachtspunten 

  * De separator in de csv files moet een komma zijn, en het teken voor decimalen een punt. 

  * Omdat het bestand ``HR_default.csv`` ook gebruikt wordt voor overslagberekeningen is het raadzaam de daarvoor relevante kolommen ook direct te vullen.


Draaien van de workflow voor het bepalen van de faalkans van overslag
--------------------------------

De gebruiker kan de workflow als volgt aanroepen vanuit de Anaconda
Prompt (activeer eerst environment):

::

   python -m preprocessing overflow --config_file {config_bestand}


Daarbij moet ``{config_bestand}`` verwijzen naar de locatie van het ``preprocessing.config`` bestand. 

Voor deze workflow zijn de volgende waarden in dat bestand van belang:

.. list-table::
   :header-rows: 1

   * - Parameter
     - Omschrijving
   * - database_path_HR_current
     - Pad naar de database voor de huidige situatie (2023)
   * - database_path_HR_future
     - Pad naar de database voor de toekomstige situatie (2100)
   * - hr_profielen_dir
     - Pad naar de map met de profielen van de dijkvakken.
   * - hr_input_csv
     - Pad naar het ``HR_default.csv`` bestand. De bestandsnaam moet mogelijk worden aangepast.
   * - output_map_overslag
     - Pad naar de map waar de resultaten van de waterstandsberekeningen worden opgeslagen.


.. topic:: Aandachtspunten 

   * Met het uitvoeren van deze workflow wordt een groot aantal probabilistische berekeningen uitgevoerd met Hydra-Ring. Zeker voor locaties in bijvoorbeeld het benedenrivierengebied zijn deze complex, en kan het doorrekenen enige tijd duren. 

   * Voor de databases moet telkens een drietal bestanden aanwezig zijn: een HRD-bestand met typisch een bestandsnaam als ``WBI2017_Westerschelde_222_223_30-2_31-1_v03.sqlite``, een configuratiebestand met bovengenoemde naam maar extensie ``*.config.sqlite`` en een hlcd-bestand met de naam ``*hlcd*.sqlite`` (NB: de tekens op de plaats van * worden genegeerd).

   * Het is handig om eerst de workflow helemaal te testen voor 1 locatie. Daarvoor kan (tijdelijk) het aantal regels in het ``HR_default.csv`` bestand worden beperkt tot bijv. alleen de eerste locatie. Let wel op dat de boekhouding in orde blijft.

   * De workflow zal crashen wanneer er bestaande resultaten worden gevonden. Deze moeten dan eerst worden verwijderd of verplaatst.

Er wordt enige controle op de uitvoer gedaan door de preprocessor, maar het is raadzaam (al dan niet steekproefsgewijs) de resultaten te controleren. De meeste eenvoudige manier daarvoor is om naar de ``output_map_overslag`` te gaan en voor enkele locaties de resultaten te bekijken in het bestand ``DESIGNTABLE_{locatie}.txt``. Hier staat bij `Value` de kruinhoogte, en daarachter faalkans en betrouwbaarheidsindex bij die kruinhoogte. In de regel moeten de faalkansen dalen met stijgende kruinhoogte. Bij het wegschrijven van de database wordt hiervoor gecorrigeerd, maar wanneer dit nodig is zegt het wel iets over de kwaliteit van de berekening: het kan bijvoorbeeld wijzen op een instabiele probabilistische berekening, of een inconsistentie in de database.