Piping
======
Voor piping is geen aparte workflow nodig. De gegevens die in het invoerbestand worden ingevuld kunnen direct in de database worden weggeschreven.

Structuur van het invoerbestand voor piping
-----------------------------------------------

.. csv-table:: Kolommen in invoerbestand voor piping
  :file: tables/piping_kolommen.csv
  :widths: 15, 15, 50
  :header-rows: 1

In het bestand staan nog enkele kolommen die niet in gebruik zijn. Deze kunnen worden genegeerd en worden bij een toekomstige release verwijderd.

Het vullen van het invoerbestand
-------------------------------
Voor piping wordt uitgegaan van semi-probabilistische Sellmeijer berekeningen. Daarbij is de aanname dat er 1 doorsnede representatief is voor een dijkvak. In sommige beoordelingen is met de uittredepuntenmethode gerekend. In dat geval is het advies om per vak het zwakste uittredpeunt te kiezen, en met de vershcillen tussen uittredepunten rekening te houden bij het maken van de vakindeling.

Voor de parameters `L_voor` en `L_achter` geldt dat `L_achter` beter niet meer dan 30 meter kan zijn: in dat geval hebben bermen geen effect op piping wat tot ongewenste effecten kan leiden bij de maatregelen. Mocht een dergelijke situatie zich toch voordoen, neem dan contact op.