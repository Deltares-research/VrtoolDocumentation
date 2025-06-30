Installaties
=======================================

Voor alle stappen van de Veiligheidsrendement methode is de installatie van Python middels Anaconda of Miniconda noodzakelijk. Daarna moet voor elk onderdeel nog een aparte Python package gebruikt/geinstalleerd: 

* VRUtils voor de preprocessing van gegevens
* VRTool voor de veiligheidsrendementberekeningen
* VRDashboard voor analyse van de resultaten.

**Miniforge**

Om de installatie goed te doorlopen is het nodig om eerst Miniforge of een alternatief zoals Anaconda of Miniconda te installeren. Miniforge is minimalistisch en licentievrij.

1. Installeer `Miniforge <https://conda-forge.org/miniforge/>`_.

**Download bestanden** 

De bestanden kunnen worden gedownload via de Github pagina's van de verschillende software onderdelen. 

1. Download de meest recente release van de VRTOOL (v1.1.1) door via deze `link <https://github.com/Deltares/Veiligheidsrendement/releases/tag/v1.1.1>`_ het bestand ``vrtool-1.1.1.tar.gz`` te downloaden. 

2. Download de meest recente release van het Dashboard (v1.1.1) door via deze `link <https://github.com/Deltares-research/VrtoolDashboard/releases/tag/v1.1.1>`_ het bestand ``vr_dash-1.1.1.tar.gz`` te downloaden.

3. Download de meest recente release van de preprocessor (v1.2.1) door via deze `link <https://github.com/Deltares/VRSuiteUtils/releases/tag/v1.2.1>`_ het bestand ``vr_preprocessing-1.2.1.tar.gz`` te downloaden.

Merk op dat via de Github pagina's ook oudere of nieuwere versies kunnen worden gedownload. De versies die hierboven zijn genoemd zijn getest en werken goed samen. 

**Installeren van de software**

Volg de onderstaande stappen om de software te installeren en te gebruiken:

4. Open Anaconda Prompt en navigeer naar de gecreerde folder met ``cd "C:\Veiligheidsrendement"``

   *NB: afhankelijk van de gebruikersrechten kan het noodzakelijk zijn om Anaconda Prompt als administrator te starten. Klik daarvoor met de rechtermuisknop en selecteer `Als administrator uitvoeren`.*

5. Maak een lokaal environment aan met het volgende command: ``conda create -p "C:\Veiligheidsrendement\.env" python=3.12``.

   *NB: als hier al een environment staat dan wordt deze automatisch overschreven.*

6. Activeer de environment met ``conda activate "C:\Veiligheidsrendement\.env\"``

7. Run ``pip install vrtool-1.1.1.tar.gz`` om de VRTool te installeren

8. Run ``pip install vr_dash-1.1.2.tar.gz`` om het Dashboard te installeren

9. Run ``pip install vr_preprocessing-1.2.1.tar.gz`` om VRUtils te installeren waarmee we de preprocessing kunnen doen, Deze stap is niet nodig voor de tutorial. 

Alles is nu geïnstalleerd en zowel de VRTool als het Dashboard zijn klaar voor gebruik. Als je VRUtils (stap 9) hebt geïnstalleerd kun je ook de preprocessing doen.

Voor het starten van het dashboard volg je de volgende stappen:

10. Run ``python -m src.index`` om het dashboard te starten. 

11.  In je commandline verschijnt nu een url en wordt het dashboard automatisch geopend in je browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser. Het Dashboard wordt gestart.

.. note::
   De code van de verschillende onderdelen is open beschikbaar vanuit de verschillende repositories:

   * `VRTool <https://github.com/Deltares/Veiligheidsrendement>`_
   * `VRDashboard <https://github.com/Deltares-research/VrtoolDashboard>`_
   * `VRUtils <https://github.com/Deltares/VRSuiteUtils>`_
   
   Daar kan ook de meest recente versie worden gekozen, waarbij wel moet worden opgelet dat de juiste versies samen worden gebruikt. De versies die hierboven zijn genoemd zijn getest en werken goed samen.
