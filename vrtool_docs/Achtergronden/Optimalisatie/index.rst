=============================================
Optimaliseren van versterkingsmaatregelen
=============================================
Op basis van de resultaten van de eerdere stappen worden vervolgens 2 versterkingsvarianten bepaald: 

* Een referentievariant op basis van het OI2014, waarbij 50 jaar vooruit en integraal wordt versterkt.
* Een optimalisatie van maatregelen op basis van veiligheidsrendement.

Referentievariant op basis van OI2014
==============================================
De referentievariant heeft als doel de resultaten te vergelijken met een gangbare werkwijze. Daarvoor gaan we uit van de standaardfaalkansbegroting uit het OI2014. 
Daarvoor hanteren we de volgende factoren voor de faalkansruimte, en de lengte-effectfactoren N, a en b:

.. list-table:: faalkansbegroting
   :widths: 30 20
   :header-rows: 1

   * - Mechanisme
     - Faalkansruimte
     - Lengte-effectfactoren
   * - Piping
       - 24%
       - a = 0.5 of 0.9 en b = 300 m
   * - Macrostabiliteit
         - 4%
         - a = 0.033 en b = 50 m
   * - Overloop/overslag
         - 24%
         - N = 1
   * - Bekleding
         - 10%
         - N = 3

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

Vervolgens worden de kansen van de mechanismen als onafhankelijke kansen gecombineerd. Door deze voor elk jaar te vermenigvuldigen met de trajectfaalkans wordt het totale overstromingsrisico bepaald. 

Opzet van het algoritme
--------------------------------
- Er wordt stapsgewijs bepaald welke maatregel het beste is. Daarvoor worden achtereenvolgens:
  - De kosten van de maatregelen bepaald
  - Het risico door falen door overslag/geotechnische mechanismen ná uitvoering van een individuele maatregel
  - Vervolgens wordt de BC-ratio op 2 manieren bepaald:
    1.	De BC-ratio (kosten/baten) van elke individuele maatregel
    2.	Vervolgens wordt apart voor overslag gekeken naar de optimale combinatie van maatregelen voor overslag en voor bekleding. Omdat voor overslag en bekleding geldt dat het zwakste vak de faalkans bepaalt kan het voorkomen dat bijvoorbeeld het verhogen van de kruin van 1 vak een zeer lage BC-ratio heeft, maar van 2 vakken juist een hoge (bijv. als 2 vakken nagenoeg dezelfde β hebben).
  - Tot slot wordt vergeleken of een individuele maatregel (1) of een combinatie (2) de hoogste BC-ratio heeft. Deze maatregel wordt dan uitgevoerd, en de beginsituatie voor de volgende optimalisatiestap wordt aangepast met deze maatregel.
- Wanneer het max aantal iteraties (600) is bereikt, of de BC-ratio van de beste maatregel < 0.1 stopt de optimalisatie.


.. toctree::
   :maxdepth: 1

   .. Bepaling van optimale maatregelen
   .. Optimalisatiealgoritme

