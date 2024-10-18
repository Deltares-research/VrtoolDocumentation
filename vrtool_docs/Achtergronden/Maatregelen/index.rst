Maatregelen
=======================================
Binnen de VRTOOL worden twee hoofdtypen maatregelen gebruikt: standaard geparameteriseerde maatregelen (tabel `StandardMeasure` in de database) en custom maatregelen per dijkvak (tabel `CustomMeasureDetail`). Op basis van deze maatregelen bepaalt de optimalisatieroutine van de VRTOOL welke combinatie van maatregelen optimaal is op trajectniveau. Daarbij wordt in de optimalisatie op basis van bepaalde regels niet alleen gerekend met losse maatregelen, maar ook met combinaties van maatregelen. 

Combineren van losse maatregelen
--------------------------------
Bij de maatregelen is van belang dat deze een verschillend `combinable_type` hebben. Er worden in de tool 4 typen onderscheiden:

* `combinable`: Deze maatregelen hebben invloed op piping, overslag en stabiliteit binnenwaarts en kunnen gecombineerd worden met `partial` en `revetment` maatregelen. Een `grondversterking <Versterking in grond.html>`_ is in principe altijd `combinable`.
* `partial`: Deze maatregelen kunnen worden gecombineerd met `combinable` maatregelen. In principe zijn dit maatregelen gericht op het verbeteren van piping (momenteel alleen de `verticale pipingoplossing <Verticale Piping Maatregelen.html>`_.
* `full`: Deze maatregelen staan los, en kunnen alleen gecombineerd worden met een `revetment`. Het gaat hierbij bijvoorbeeld om grondversterkingen in combinatie met een stabiliteitsscherm, losse `stabiliteitsschermen <Stabiliteitsscherm.html>`_ en `zelfkerende constructies <Zelfkerende Constructie.html>`_.
* `revetment`: Deze maatregelen hebben álleen invloed op de `bekleding <Maatregelen_dijkbekleding.html>`_, en kunnen met alle andere (gecombineerde) maatregelen worden gecombineerd.

Omgang met maatregelen in de optimalisatie
------------------------------------------
In de optimalisatie wordt voor elke maatregel een investeringsjaar toegevoegd. Dit is het jaar waarin de maatregel wordt uitgevoerd. De kosten worden verdisconteerd op basis van dat jaar, en voor de faalkans tot dat jaar wordt de originele faalkans aangenomen. 

In de optimalisatie worden de maatregelen verder gecombineerd volgens de regels zoals hierboven, en op de pagina's per maatregel beschreven. In lijn met de `originele implementatie <https://www.sciencedirect.com/science/article/pii/S0951832020308346>`_ worden maatregelen gesplitst in maatregelen gericht op gecorreleerde faalmechanismen (overloop/overslag en bekleding) en ongecorreleerde faalmechanismen (piping en stabiliteit binnenwaarts). Dit betekent ook dat maatregelen t.b.v. overloop/overslag en bekleding geen invloed hebben op de binnenwaartse stabiliteit/piping, en vice versa.

.. toctree:: 
   :caption: Beschikbare maatregelen
   :maxdepth: 1
   
   Versterking in grond
   Stabiliteitsscherm
   Zelfkerende Constructie
   Verticale Piping Maatregelen
   Maatregelen_dijkbekleding
   Custom maatregel