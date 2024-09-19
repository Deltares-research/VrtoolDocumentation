Overslag
========================

Voor het bepalen van de betrouwbaarheid voor overloop/overslag (gras erosie kruin- en binnentalud) wordt de volgende invoer gebruikt:
- Een relatie tussen kruinhoogte en betrouwbaarheidsindex β in de huidige situatie (2023)
- Een relatie tussen kruinhoogte en betrouwbaarheidsindex β in de toekomst (2100)

Deze relaties worden in de preprocessing bepaald middels Hydra-Ring.

Op basis van een jaartal wordt de betrouwbaarheidsindex van een kruinhoogte geinterpoleerd. Wanneer relevant wordt de kruindaling meegenomen in deze interpolatie.

Voor elke doorsnede wordt een kansverdeling van het kritisch overslagdebiet gekozen. Vervolgens wordt hiermee een probabilistische GEKB-berekening conform WBI-2017 uitgevoerd. De beschikbare kansverdelingen zijn hieronder weergegeven. Aangenomen wordt dat deze kansverdeling hetzelfde blijft in de toekomst.

.. csv-table:: Kritische overslagdebieten
    :file: tables/kritische_overslagdebieten.csv
    :header-rows: 1
    :widths: 40, 10, 10, 10, 20