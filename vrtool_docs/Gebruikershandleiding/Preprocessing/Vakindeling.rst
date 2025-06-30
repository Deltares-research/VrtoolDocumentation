Vakindeling
===========

De basis van een veiligheidsrendementberekening is één vakindeling die voor alle faalmechanismen gebruikt wordt. Als eerste wordt een invoerbestand gevuld, waarna de workflow voor het maken van de vakindeling kan worden gedraaid.

.. admonition:: Aandachtspunten bij het maken van een vakindeling

  Bij het maken van een vakindeling wordt het traject opgedeeld in een aantal relatief homogene dijkvakken. Daarbij is de kern dat de beoordelingsinformatie van de verschillende mechanismen goed wordt gerepresenteerd. In aanvulling daarop is van belang dat wordt gekeken vanuit het perspectief van de versterkingsmaatregelen. Wanneer bijvoorbeeld een deel van een in de beoordeling 'homogeen' vak heel dichtbebouwd is, en een deel niet, kan dit vak beter worden gesplitst. Streef bij het opsplitsen naar ongeveer 40 vakken op het dijktraject, waarbij de vakken niet kleiner dan 300 meter moeten zijn. Dit is een vuistregel, maar in principe geldt dat kleinere vakken niet altijd leiden tot betere resultaten, en zeker wel tot meer rekenwerk (o.a. voor preprocessing en VRTOOL). Focus moet liggen op:

  * Goed onderscheiden van de zwakkere vakken. Dus vakken waar de faalkans voor 1 of meerdere mechanismen hoog is moeten goed onderscheiden worden. Houd de indeling van de vakken voor de dominante mechanismen als basis aan.

  * Goed onderscheiden van de vakken met duidelijk andere maatregelen (bijvoorbeeld bij veel bebouwing), ook als het oordeel relatief homogeen is.

  * Beperken van grote aantallen vakken  waar nauwelijks maatregelen worden verwacht, of waar de maatregelen redelijk homogeen zijn (met name voor de belangrijkste mechanismen). Deze kunnen vaak worden samengevoegd zonder dat de kwaliteit van de berekening er onder lijdt. Een gedeelte van bijv. 10 km dat voor alle mechanismen ruim voldoet kan prima als 1 vak beschouwd worden.

Structuur van het invoerbestand van de vakindeling
-----------------------------------------------

De basis voor het genereren van de vakindeling is het invoerbestand
``Vakindeling.csv``. Doel van deze workflow is een ``geojson`` bestand te creeren met alle dijkvakken. Dit bestand is ook invoer voor andere workflows. Dit bestand wordt in de mappenstructuur weggeschreven in ``intermediate_files\vakindeling\``.

.. tip:: 
  We onderscheiden bij de invoer 3 niveau's van ruimtelijk detail: traject - dijkvak - doorsnede. De vakindeling beschrijft welke dijkvakken onderdeel zijn van het traject, én welke doorsnede-berekeningen daarbij horen. Het kan daarbij voorkomen dat meerdere dijkvakken dezelfde doorsnede hebben voor een bepaald mechanisme.
  
Het invoerbestand ``Vakindeling.csv`` heeft de volgende kolommen die ingevuld moeten worden:

.. csv-table:: Kolommen in invoerbestand vakindeling
  :file: tables/vakindeling_kolommen.csv
  :widths: 10, 10, 70
  :header-rows: 1
  :class: small-table

.. topic:: Aandachtspunten

  * Bij het opgeven van een koppeling in de kolommen ``piping``, ``stabiliteit`` etc. hoeven deze nog niet te zijn ingevuld voor deze workflow. Echter, bij het maken van de database moet het gegenereerde ``geojson`` bestand wel alle benodigde informatie bevatten.

  * Invullen van de kolommen pleistoceendiepte en deklaagdikte is optioneel, maar wanneer deze niet worden ingevuld wordt standaard 25 respectievelijk 7 meter aangehouden. Dit leidt tot relatief zware maatregelen. Voor een nauwkeurige kostenschatting wordt aanbevolen om deze waarden expliciet in te vullen. Daarbij moet geredeneerd worden vanuit een verwachtingswaarde (dus de dikte/diepte die op het grootste deel van het vak aanwezig is).

  * De parameters ``a_piping`` en ``a_stabiliteit`` geven de lengte van het dijkvak dat gevoelig is voor piping/stabiliteit binnenwaarts aan. Daarmee wordt dus het lengte-effect binnen het dijkvak in rekening gebracht. Wanneer deze niet worden ingevuld wordt aangenomen (conservatief) dat 100% van de lengte van het dijkvak gevoelig is voor piping/stabiliteit. Het advies is om, zeker voor de zwakkere vakken, deze waarden goed te bepalen omdat anders de trajectfaalkans zeer hoog kan worden.

Het vullen van het invoerbestand
-------------------------------

In onderstaande figuur is met een voorbeeld voor stabiliteit
geillustreerd hoe de koppeling tussen doorsnedes en de vakindeling moet
worden gelegd. Merk op dat het mogelijk is voor meerdere vakken
dezelfde doorsnede te hanteren (een voorbeeld in de figuur is de
dikgedrukte doorsnede ``ET_VOLDOET``). Deze hoeft dan slechts 1x genoemd
te worden in het STBI invoerbestand, maar kan bij meerdere vakken worden
gebruikt. 

.. figure:: img/Filling_Vakindeling_stbi.PNG
    :alt: Voorbeeld van het vullen van het invoerbestand van de vakindeling
    :align: center

Belangrijk bij het genereren van de vakindeling zijn met name de
``m_start`` en ``m_eind`` parameters. Wanneer de lengte van het traject
(dus de maximale ``m_eind``) teveel afwijkt (grofweg >1 meter) van de
lengte van de shape uit het Nationaal Basisbestand Primaire
Waterkeringen wordt een foutmelding gegeven.

.. topic:: Aandachtspunten 

  * De m_eind en m_start van alle vakken moeten op elkaar aansluiten

  * In principe is het beter om vakken niet té klein te maken. Vaak zorgt dit voor onnodig veel rekentijd, en niet voor een beter resultaat. In de regel is het advies geen vakken kleiner dan pakweg 300 meter te maken, tenzij er sprake is van lokale zwakke plekken.

  * Voor een betrouwbare analyse moeten met name de zwakkere vakken en de vakken met verwachte dure maatregelen (bijv. veel bebouwing) goed worden onderscheiden. Als geen maatregelen worden verwacht, of vakken redelijk homogeen zijn (met name voor de belangrijkste mechanismen) kunnen deze samen worden gevoegd zonder dat de kwaliteit van de berekening er onder lijdt.


Draaien van de workflow voor het genereren van een vakindeling
-------------------------------

De gebruiker kan de workflow als volgt aanroepen vanuit de Anaconda
Prompt (activeer eerst environment):

::

   python -m preprocessing vakindeling --config_file {config_bestand}

Daarbij moet ``{config_bestand}`` verwijzen naar de locatie van het ``preprocessing.config`` bestand. 

Voor deze workflow zijn de volgende waarden in het configuratiebestand van belang:

.. list-table::
   :header-rows: 1
   :class: small-table

   * - Parameter
     - Omschrijving
   * - traject_id
     - Naam van het traject
   * - vakindeling_csv
     - Pad naar het invoerbestand van de vakindeling. Deze moet eventueel nog worden aangepast.
   * - output_folder_vakindeling
     - Pad naar de map waar de geojson van de vakindeling moet worden opgeslagen. Hier wordt ook automatisch een kaart van de vakindeling gegenereerd.
   * - traject_shape
     - Default wordt deze niet gebruikt, maar hier kan een pad naar een alternatieve shape van het traject worden ingevoerd. Standaard wordt de shape uit het Nationaal Basisbestand Primaire Waterkeringen gebruikt.
   * - flip_traject
     - In sommige gevallen is de vakindeling in de tegenovergestelde richting van de shapefile gedefinieerd. Door hier ``True`` te kiezen kan deze worden omgedraaid.

Wanneer de workflow succesvol is uitgevoerd wordt in de map output_folder_vakindeling een viertal bestanden weggeschreven:

* ``vakindeling.log``: een logbestand waarin de voortgang van de workflow wordt bijgehouden, en eventuele foutmeldingen worden gerapporteerd.
* ``Vakindeling_{traject_id}.geojson``: het geojson bestand waarin de vakindeling is opgeslagen. Dit bestand wordt gebruikt als invoer voor andere workflows.
* ``Vakindeling_{traject_id}.png``: een kaart van de vakindeling, die kan worden gebruikt om de vakindeling te controleren.
* ``configuratie_maatregelen.csv``: een csv-bestand waarin de configuratie van de maatregelen is opgeslagen. Dit bestand kan worden gebruikt om maatregelen per dijkvak aan of uit te zetten. Dit is verder beschreven bij de workflow `Genereren database <Genereren_database.html>`_.

Na het genereren van de vakindeling is het altijd belangrijk deze goed te controleren: de vakindeling is een belangrijke basis voor de volgende workflows. Dit kan eenvoudig worden gedaan in QGIS of ArcGIS.

Mogelijke foutmeldingen
~~~~~~~~~~~~~~~~~~~~~~~

Uit het logbestand, dat wordt weggeschreven in vakindeling_csv_path (meestal ``intermediate_files\vakindeling\``) worden de meeste foutmeldingen gerapporteerd. Meestal zal dit gaan over bijv. dubbele waarden die uniek moeten zijn, of kolommen die niet compleet zijn. Een belangrijke mogelijke foutmelding is wanneer de lengte van het traject niet overeenkomt met de shape uit het Nationaal Basisbestand Primaire Waterkeringen (NWPB). Dit wordt hieronder verder toegelicht.

.. admonition:: Fouten in de trajectlengte

  Een foutmelding die vaak voorkomt is wanneer de totale lengte van het traject niet overeenkomt met het NWBP. Daarvoor wordt gekeken naar de hoogste M-waarde, en de lengte van de shape uit het Nationaal Basisbestand Primaire Waterkeringen. Deze moeten ongeveer (op de meter nauwkeurig) overeenkomen. 

  *Let op* de totale trajectlengte moet afgerond op 5 significante cijfers (dus bij een lengte van >10000 meter afgerond op 1 meter) niet korter zijn dan de verwachte trajectlengte, maar mag zeker niet langer zijn. Dus rond altijd de verwachte lengte af naar beneden. Onderstaand is een voorbeeld van een foutmelding weergegeven wanneer de lengte in vakindeling.csv te kort is. Wanneer er een klein verschil is in trajectlengte is het advies om de waarde op basis van de foutmelding in het csv-bestand aan te passen: een meter meer of minder heeft geen invloed op de resultaten. Bij grote verschillen is wel raadzaam om de ligging van de vakken op basis van het NBPW en de shape die als bron voor de M-waarden is gebruikt te vergelijken. Dit kan bijvoorbeeld worden gedaan door beide in QGIS of ArcGIS weer te geven. Het komt bijvoorbeeld in sommige gevallen voor dat de referentielijn van de legger van de beheerder bij kunstwerken niet helemaal overeenkomt met de referentielijn van het NBPW. In dat geval moet de metriering worden aangepast, of de shape van de legger als invoer worden gegeven (via traject_shape).

  .. figure:: img/te_kort_traject.PNG
      :alt: Foutmelding bij een te kort traject
      :align: center