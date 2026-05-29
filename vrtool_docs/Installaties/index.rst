Installaties
=======================================

Voor alle stappen van de Veiligheidsrendement methode is de installatie van Python middels Anaconda of Miniconda noodzakelijk. Daarna moet voor elk onderdeel nog een aparte Python package gebruikt/geinstalleerd: 

* VRUtils voor de preprocessing van gegevens
* VRTool voor de veiligheidsrendementberekeningen
* VRDashboard voor analyse van de resultaten.

**Miniforge**

Om de installatie goed te doorlopen is het nodig om eerst Miniforge of een alternatief zoals Anaconda of Miniconda te installeren. Miniforge is minimalistisch en licentievrij.

1. Installeer `Miniforge <https://conda-forge.org/miniforge/>`_.

**Creëren van een werkmap**

2. Vervolgens moet er een werkmap gekozen worden. Bijvoorbeeld ``C:\Veiligheidsrendement``. Maak deze map aan op de gewenste locatie.

3. Door een Python environment aan te maken in deze map, kunnen daar alle benodigde packages worden geïnstalleerd en gebruikt. Dit kan vanuit Miniforge Prompt. Open dit, navigeer naar de folder met ``cd "C:\Veiligheidsrendement"`` en maak vervolgens een environment aan met ``python -m venv .venv``.

4. Activeer de environment met ``.venv\Scripts\activate``.

5. Vervolgens kan door de preprocessor te installeren automatisch ook de rest van de pakketten worden geinstalleerd. Doe dit door in de Miniforge Prompt in de werkmap het volgende commando uit te voeren: ``pip install git+https://github.com/Deltares/VRSuiteUtils.git@v1.3.0``. 1.3.0 past bij de laatste gevalideerde combinatie van tools. Uiteraard kan ook een latere versie worden geprobeerd, gebruik daarvoor de betreffende hash of tag vanuit Github.

Alle tools van de veiligheidsrendementmethode zijn nu gereed voor gebruik. Voor het starten van het dashboard volg je de volgende stappen:

10. Run ``python -m src.index`` om het dashboard te starten. 

11.  In je commandline verschijnt nu een url en wordt het dashboard automatisch geopend in je browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser. Het Dashboard wordt gestart.

Het draaien van de preprocessor en de VRTool kan vanuit dezelfde omgeving worden gedaan. Beschrijvingen hiervan zijn in de rest van de documentatie te vinden.

.. note::
   De code van de verschillende onderdelen is open beschikbaar vanuit de verschillende repositories:

   * `VRTool <https://github.com/Deltares/Veiligheidsrendement>`_
   * `VRDashboard <https://github.com/Deltares-research/VrtoolDashboard>`_
   * `VRUtils <https://github.com/Deltares/VRSuiteUtils>`_
   
   Daar kan ook de meest recente versie worden gekozen, waarbij wel moet worden opgelet dat de juiste versies samen worden gebruikt. Door de laatste tag van VRUtils te gebruiken, wordt automatisch de bijpassende versie van de andere onderdelen meegeïnstalleerd. 
