Stabiliteit
===========
Voor stabiliteit binnenwaarts is geen aparte workflow nodig. De gegevens die in het invoerbestand worden ingevuld kunnen direct in de database worden weggeschreven.

Structuur van het invoerbestand voor stabiliteit binnenwaarts
-----------------------------------------------

.. csv-table:: Kolommen in invoerbestand voor stabiliteit
  :file: tables/stbi_kolommen.csv
  :widths: 15, 15, 50
  :header-rows: 1


Het vullen van het invoerbestand
-------------------------------
Voor stabiliteit wordt in principe met een vereenvoudigde relatie gerekend waarmee bermverbreding wordt vertaald naar een toename van de betrouwbaarheid. Het is ook mogelijk met D-Stability te rekenen. Wanneer in de kolom `stixnaam` een bestandsnaam van een D-Stability berekening wordt ingevoegd wordt deze automatisch meegenomen in de database en gebruikt in de VRTOOL. De stix-bestanden moeten dan handmatig in een folder `\stix` in dezelfde directory als de database worden geplaatst. 

Het advies is om altijd een eerste berekening zonder D-Stability uit te voeren, en dan voor de meest relevante vakken dit mee te nemen. Neem contact op met Deltares wanneer dit wenselijk is: met name de verschillende versies van D-Stability leiden makkelijk tot fouten.

