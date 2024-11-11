Referentievariant op basis van OI2014
==============================================
De referentievariant heeft als doel de resultaten te vergelijken met een gangbare werkwijze. Daarvoor gaan we uit van de standaardfaalkansbegroting en lengte-effectfactoren uit het OI2014. 
Daarvoor hanteren we de volgende factoren voor de faalkansruimte, en de lengte-effectfactoren N, a en b:

.. csv-table:: Gebruikte faalkansbegroting voor referentievariant
   :file: faalkansbegroting.csv
   :widths: 20, 15, 20
   :header-rows: 1

Bij bekleding wordt een gecombineerde eis gehanteerd voor falen van de gras- en steenbekleding. Voor het lengte-effect wordt daar standaard een factor 3 gehanteerd, wat enigszins afwijkt van het OI2014. Opgemerkt moet worden dat deze factoren niet worden gebruikt bij de opschaling: dan wordt aangenomen dat het zwakste vak de trajectfaalkans bepaalt.

Op basis van alle mogelijke maatregelen wordt vervolgens voor elk dijkvak de maatregel gezocht die voor de komende 50 jaar voldoet aan de eisen conform de faalkansbegroting, tegen de laagste kosten.

Als er geen maatregel is die aan alle eisen voldoet, wordt de maatregel gekozen die voor de meeste mechanismen voldoet, en voor de anderen het beste presteert (opnieuw tegen laagste kosten). Dit komt overigens zelden voor, enkel soms bij bekleding. 

Op dit moment zijn de factoren voor de faalkansbegroting enkel te configureren door deze handmatig aan te passen in de database, specifiek in tabel DikeTrajectInfo.

Opgemerkt moet worden dat bij het bepalen van de trajectfaalkans aangenomen wordt dat de doorsnedekansen niet worden opgeschaald binnen de vakken. Daardoor kan het voorkomen dat de resulterende trajectfaalkans een stuk lager is dan de trajectfaalkans. Tegelijkertijd moet worden opgemerkt dat wanneer dit wanneer wel zou worden opgeschaald van doorsnede naar vakniveau het afhankelijk is van de precieze mate van opschaling wat de resulterende trajectfaalkans wordt, waarbij geen garantie is dat de trajectfaalkans in het jaar 2075 daadwerkelijk kleiner is dan de norm.

