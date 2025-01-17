Werken met het dashboard
=======================================

Na het rekenen met de VRTOOL kan de database met resultaten worden geimporteerd in het dashboard. Met dit dashboard kunnen resultaten worden weergegeven en geanalyseerd, en kunnen nieuwe optimalisatieberekeningen met nieuwe instellingen worden uitgevoerd. 

Het dashboard kan worden gestart door in Anaconda Prompt ``python -m src.index`` uit te voeren. Het dashboard verschijnt nu automatisch in de browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser.

Wanneer het dashboard wordt geopend verschijnt eerst de startpagina:

.. figure:: img/dashboard_navigatiepagina.png


Van hieruit kan naar 3 pagina's worden genavigeerd:

- `Analyse per traject <WeergevenResultaten.html>`_ waar resultaten van een trajectberekening kunnen worden geanalyseerd.
- `Analyse op gebiedsniveau <ProgrammerenVersterkingen.html>`_ waar versterkingsprojecten op 1 of meerdere trajecten kunnen worden geprogrammeerd.
- `Vergelijken berekeningen <VergelijkenOptimalisatieberekeningen.html>`_ waar twee optimalisatieberekeningen van een traject met elkaar kunnen worden vergeleken.

Daarnaast is het via de pagina `Analyse per traject` mogelijk om berekeningen `aan te sturen via het dashboard <BerekeningenMetDashboard.html>`_.

.. toctree::
   :hidden:   
   :maxdepth: 1

    Weergeven van resultaten op trajectniveau <WeergevenResultaten>
    Berekeningen aansturen via het dashboard <BerekeningenMetDashboard>
    Vergelijken van optimalisatieberekeningen <VergelijkenOptimalisatieberekeningen>
    Analyse op gebiedsniveau <ProgrammerenVersterkingen>
