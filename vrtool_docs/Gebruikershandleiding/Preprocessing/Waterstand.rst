Waterstandsberekeningen
==========

Invoer voor de veiligheidsrendementberekening zijn met Hydra-Ring
afgeleide waterstandsfrequentielijnen voor het jaar 2023 en 2100. Deze
worden afgeleid middels een gestandaardiseerde workflow. Vóór het
draaien van deze workflow moet eerst een invoerbestand ingevult worden.

Structuur van het invoerbestand van de waterstandsberekeningen
-----------------------------------------------

De basis voor het genereren van berekeningen voor waterstand en overslag
is het invoerbestand ``HR_default.csv``. Dit bestand is terug te vinden
in: ``C:\Veiligheidsrendement\.env\Lib\site-packages\preprocessing\default_files``.

Doel van de workflow is om voor elk dijkvak een waterstandsfrequentielijn af te leiden voor de jaren 2023 en 2100. 

Het invoerbestand ``HR_default.csv`` heeft de volgende kolommen die ingevuld moeten worden:

.. csv-table:: Kolommen in invoerbestand waterstand & overslag
  :file: tables/HR_kolommen.csv
  :widths: 15, 15, 50
  :header-rows: 1

.. topic:: Aandachtspunten

   * Voor het bepalen van waterstanden worden de kolommen ``prfl_bestand``, ``orientatie``, ``dijkhoogte``, ``zodeklasse`` en ``bovengrens_golfhoogteklasse`` niet gebruikt. Deze zijn enkel van toepassing op overslag.

   * De kolom ``m_value`` is niet meer in gebruik en zal in een toekomstige versie worden verwijderd.

   * De waarden in de kolom ``doorsnede`` moeten overeenkomen met die in de kolom ``waterstand`` in de `vakindeling <Vakindeling.html>`__.

Het vullen van het invoerbestand
-------------------------------
Voor het doorrekenen van de waterstandsfrequentielijnen moet per dijkvak 1 locatie worden opgegeven. Deze locatie moet tevens hetzelfde zijn als voor overslag. In de beoordeling zijn door beheerders vaak waterstands- en overslagberekeningen gemaakt op doorsneden op 100 meter afstand tot elkaar. Dit is voor veiligheidsrendement niet nodig. Het advies is om voor elk vak de maatgevende locatie voor overslag te kiezen, en deze locatie ook te gebruiken voor waterstandsberekeningen.

De kolommen ``bovengrens`` en ``ondergrens`` moeten worden ingevuld met een voldoende hoge en lage waterstand. Vervolgens wordt hier door de preprocessor een grid van gemaakt. Deze waarden zijn doorgaans beschikbaar vanuit de beoordeling. 

.. topic:: Aandachtspunten 

  * De separator in de csv files moet een komma zijn, en het teken voor decimalen een punt. 

  * Omdat het bestand ``HR_default.csv`` ook gebruikt wordt voor overslagberekeningen is het raadzaam de daarvoor relevante kolommen ook direct te vullen.


Draaien van de workflow voor het afleiden van waterstandsfrequentielijnen
-------------------------------

De gebruiker kan de workflow als volgt aanroepen vanuit de Anaconda
Prompt (activeer eerst environment):

::

   python -m preprocessing waterlevel --config_file {config_bestand}


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
   * - hr_input_csv
     - Pad naar het ``HR_default.csv`` bestand. De bestandsnaam moet mogelijk worden aangepast.
   * - output_map_waterstand
     - Pad naar de map waar de resultaten van de waterstandsberekeningen worden opgeslagen.


.. topic:: Aandachtspunten 

   * Met het uitvoeren van deze workflow wordt een groot aantal probabilistische berekeningen uitgevoerd met Hydra-Ring. Zeker voor locaties in bijvoorbeeld het benedenrivierengebied zijn deze complex, en kan het doorrekenen enige tijd duren. 

   * Voor de databases moet telkens een drietal bestanden aanwezig zijn: een HRD-bestand met typisch een bestandsnaam als ``WBI2017_Westerschelde_222_223_30-2_31-1_v03.sqlite``, een configuratiebestand met bovengenoemde naam maar extensie ``*.config.sqlite`` en een hlcd-bestand met de naam ``*hlcd*.sqlite`` (NB: de tekens op de plaats van * worden genegeerd).

   * Het is handig om eerst de workflow helemaal te testen voor 1 locatie. Daarvoor kan (tijdelijk) het aantal regels in het ``HR_default.csv`` bestand worden beperkt tot bijv. alleen de eerste locatie. Let wel op dat de boekhouding in orde blijft.

   * De workflow zal crashen wanneer er bestaande resultaten worden gevonden. Deze moeten dan eerst worden verwijderd of verplaatst.

Er wordt enige controle op de uitvoer gedaan door de preprocessor, maar het is raadzaam (al dan niet steekproefsgewijs) de resultaten te controleren. De meeste envoudige manier daarvoor is om naar de ``output_map_waterstand`` te gaan en voor enkele locaties de resultaten te bekijken in het bestand ``DESIGNTABLE_{locatie}.txt``. Een voorbeeld is hieronder weergegeven.

.. image:: img/DesignTableWaterstand.png
   :width: 60%
   :align: center

Belangrijke waarden om te controleren zijn in het algemeen de terugkeertijden bij de verschillende waterstanden, maar ook de kansen bij de laagste en hoogste waterstand. In de regel zou het bereik van kansen grofwel tussen 1/10 en 1 of 2 orde groottes kleiner dan de signaleringswaarde moeten liggen.
