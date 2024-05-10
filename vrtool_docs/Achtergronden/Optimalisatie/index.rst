=============================================
Bepalen van versterkingsmaatregelen
=============================================
Op basis van de resultaten van de eerdere stappen worden 2 versterkingsvarianten bepaald: 

* Een referentievariant op basis van het OI2014, waarbij 50 jaar vooruit en integraal wordt versterkt.
* Een optimalisatie van maatregelen op basis van veiligheidsrendement.

Referentievariant op basis van OI2014
==============================================
De referentievariant heeft als doel de resultaten te vergelijken met een gangbare werkwijze. Daarvoor gaan we uit van de standaardfaalkansbegroting uit het OI2014. 
Daarvoor hanteren we de volgende factoren voor de faalkansruimte, en de lengte-effectfactoren N, a en b:

.. csv-table:: Gebruikte faalkansbegroting voor referentievariant
   :file: faalkansbegroting.csv
   :widths: 20, 15, 20
   :header-rows: 1

Bij bekleding wordt een gecombineerde eis gehanteerd voor falen van de gras- en steenbekleding. De N-waarde voor overloop/overslag wordt in een komende release toegevoegd.

Op basis van alle mogelijke maatregelen wordt vervolgens voor elk dijkvak de maatregel gezocht die voor de komende 50 jaar voldoet aan de eisen van de faalkansbegroting, tegen de laagste kosten.

Als er geen maatregel is die aan alle eisen voldoet, wordt de maatregel gekozen die voor de meeste mechanismen voldoet, en voor de anderen het beste presteert (opnieuw tegen laagste kosten). Dit komt overigens zelden voor, enkel soms bij bekleding. 

Op dit moment zijn de factoren voor de faalkansbegroting niet configureerbaar voor gebruikers.

Optimalisatie van maatregelen op basis van veiligheidsrendement  
==============================================
Bij een optimalisatie op basis van veiligheidsrendement worden helemaal geen eisen gesteld aan de faalkans op mechanisme- of doorsnede-/vakniveau. In plaats daarvan wordt gekeken naar de kosten en baten van maatregelen.


Bepaling van kosten en baten
--------------------------------
Voor de kosten wordt de life-cycle cost (LCC) bepaald, gegeven het investeringsjaar van de maatregel. Dit is configureerbaar vanuit het dashboard, bij een Basisberekening wordt dit standaard op 2025 gezet, en voor grondversterkingen is ook 2045 een optie.

De baten worden bepaald door de risicoreductie van de maatregelen. Dit wordt bepaald door de trajectfaalkans te vermenigvuldigen met de verdisconteerde overstromingsschade. De trajectfaalkans wordt bepaald door de faalkansen van de mechanismen te combineren, en de overstromingsschade wordt bepaald op basis van de kosten uit de :ref:`Factsheets normering primaire waterkeringen<https://www.helpdeskwater.nl/publish/pages/132790/factsheets_compleet19122016.pdf>`.
Voor de baten wordt gebruik gemaakt van de verdisconteerde overstromingsschade. De verdiscontering wordt gedaan met een discontovoet van 3%. Zo is de schade :math:`S` in jaar :math:`t` gelijk aan:

.. math::
   S(t) = S(0) \cdot (1 + r)^t,
waarbij :math:`S(0)` de schade in het basisjaar is (conform de factsheet), en :math:`r` de discontovoet. Dit wordt gedaan voor een horizon van 100 jaar. Risico(reductie) na 100 jaar wordt niet meegenomen.

De kansen worden gecombineerd conform de meest recente assemblageregels uit het BOI: daarbij worden eerst de faalkansen van de vakken gecombineerd. Daarvoor wordt aangenomen dat dijkvakken voor piping en stabiliteit onafhankelijk zijn, conform de volgende formule:

.. math::
   P_{m} = 1 - \prod_{i=1}^{n} (1 - P_{m,i}),

waarbij :math:`P_{m}` de faalkans van het traject is voor mechanisme :math:`m`, en :math:`P_{m,i}` de faalkans van dijkvak :math:`i` voor mechanisme :math:`m`, en :math:`n` het aantal dijkvakken. Voor bekleding en overloop/overslag wordt aangenomen dat de vakken afhankelijk zijn, en wordt de volgende formule gehanteerd:

.. math::
   P_{m} = \max_{i=1}^{n} P_{m,i}.,

Vervolgens worden de kansen van de mechanismen als onafhankelijke kansen gecombineerd. Door deze voor elk jaar te vermenigvuldigen met de verdisconteerde overstromingsschade wordt het totale overstromingsrisico bepaald. 

Opzet van het algoritme
--------------------------------
Het gebruikte algoritme is een lokale optimalisatie. Dat betekent dat telkens, gegeven een bepaalde situatie (veiligheid van de dijkvakken en het traject als geheel), de beste maatregel wordt bepaald. Dit wordt gedaan door de kosten en baten van de maatregelen te bepalen, en de maatregel te kiezen met de hoogste baten/kosten-verhouding (BC-ratio).

Daarbij zijn 2 methoden om dit te bepalen:
1. De BC-ratio van elke individuele maatregel. Dit werkt uitstekend voor maatregelen die de faalmechanismen beinvloeden waarvoor vakken als onafhankelijk beschouwd worden. 
2. De BC-ratio van een combinatie van maatregelen. Dit werkt uitstekend voor maatregelen die de faalmechanismen beinvloeden waarvoor vakken als afhankelijk beschouwd worden, dus voor overloop/overslag en bekleding. 

  **Combinaties van maatregelen**
  Voor overloop/overslag en bekleding is het voor een betrouwbaar resultaat noodzakelijk om maatregelen te combineren. Dit valt eenvoudig te illustreren aan de hand van het volgende voorbeeld: een dijktraject met 2 dijkvakken heeft een faalkans van 1/100 voor overslag voor beide dijkvakken, de trajectfaalkans is daarmee ook 1/100. Wanneer op dijkvak A de kruin wordt versterkt (bijv. tot een faalkans van 1/1000), is de faalkans nog steeds 1/100, dijkvak B is immers niet versterkt, en het zwakste vak bepaalt de trajectfaalkans. Binnen de optimalisatie wordt daarom in 100 stappen gezocht naar de beste combinaties van maatregelen, daarbij wordt telkens het zwakste vak versterkt. In dit geval zou alleen kijken naar individuele maatregelen dus zorgen voor een lokaal optimum voor overloop/overslag, omdat er nooit een individuele maatregel wordt gekozen. In onderstaande tabel is een voorbeeld weergegeven waarbij is aangenomen dat om beurten de dijkvakken een factor 10 veiliger worden gemaakt, dit kost 1 miljoen euro per dijkvak. Te zien is dat het risico slechts 1 keer per 2 stappen wordt verlaagd. In dit geval heeft de combinatie van maatregelen waarbij beide vakken een factor 10 veiliger worden de gunstigste kosten-batenverhouding (450).
  
   .. csv-table:: Rekenvoorbeeld voor het combineren van maatregelen
      :file: rekenvoorbeeld_combinatie.csv
      :widths: 10,10,10,10,10,10
      :header-rows: 2

Vervolgens wordt gekeken welke maatregel het gunstigste is. Daarbij wordt eerst gekeken of de kosten-batenverhouding van een combinatie hoger is dan die van een individuele maatregel. Als dat het geval is, wordt de combinatie gekozen. Als dat niet het geval is, wordt de individuele maatregel gekozen. Daarbij wordt de maatregel gekozen op eht dijkvak met de gunstigste maatregel waarvan de kosten-batenverhouding een factor 1.5 gunstiger is dan de beste maatregel op de andere vakken. 

  **Keuze van de individuele maatregel**

  Op vak A heeft een pipingmaatregel een BC-ratio van 10000. Eventueel uitbreiden met een kleine of grotere berm verlaagt de BC-ratio naar 3000 of 1200. Op vak B heeft de gunstigste maatregel een BC-ratio van 1000. In dit geval wordt de op vak A gekozen voor een pipingmaatregel met kleine berm (BC=3000), omdat deze meer dan een factor 1.5 gunstiger is dan de beste maatregel op vak B.

  *NB: de factor 1.5 is configureerbaar door in config.json de waarde van 'f_cautious' aan te passen.*

Als de BC-ratio van de beste maatregel < 0.1 is, of het maximaal aantal iteraties (600) is bereikt, wordt de optimalisatie gestopt. Wanneer dit niet het geval is wordt de beginsituatie voor de volgende optimalisatiestap aangepast met de gekozen maatregel.
