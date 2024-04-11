Installaties
=======================================

Voor alle stappen van de Veiligheidsrendement methode is de installatie van Python middels Anaconda of Miniconda noodzakelijk. Daarna moet voor elk onderdeel nog een aparte Python package gebruikt/geinstalleerd: VRUtils voor de preprocessing van gegevens, VRTool voor veiligheidsrendementberekeningen en het Dashboard voor analyse van de resultaten.

**Anaconda**

Om de installatie goed te doorlopen is het nodig om eerst Anaconda of Miniconda te installeren.

1. Installeer `Anaconda <https://www.anaconda.com/download>`_ of `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_

**Download bestanden** 

Download de bestanden via deze `link <https://www.sharpoint.nl>`_. Dit is een zip-file met daarin verschillende bestanden die nodig zijn voor de installatie en het gebruik van de VRTOOL.

2. Pak het zip-bestand uit en zet de ``tar.gz`` bestanden in een lege folder (we gebruiken even ``C:\DashboardFiles`` als voorbeeld)

**VRTool, Dashboard & preproccessing installeren**

Het dashboard draait vooralsnog lokaal. Volg de onderstaande stappen om het dashboard te installeren en te gebruiken:

3. Navigeer in Anaconda Prompt (zorg ervoor dat u Anaconda geïnstalleerd heeft) naar de gecreerde folder met ``cd C:\DashboardFiles``

4. Maak een lokaal environment aan met het volgende command: ``conda create -p c:\DashboardFiles\.env python=3.10``.

   *NB: als hier al een environment staat dan wordt deze automatisch overschreven.*

5. Activeer de environment met ``conda activate C:\DashboardFiles\.env\``

6. Run ``pip install vrtool-0.1.3.tar.gz`` om de VRTool te installeren

   *NB: het versienummer (0.1.3.) van het bestand kan veranderen*

7. Run ``pip install vr_dash-0.3.2.tar.gz`` om het Dashboard te installeren

   *NB: het versienummer (0.3.2.) van het bestand kan veranderen*

8. Run ``pip instal vr_utils-....tar.gz`` om VRUtils te te installeren waarmee we de preprocessing kunnen doen (als je ook preproccessing wilt doen. Deze stap heb je nog niet nodig voor de VRTool & Dashboard Tutorial). 

   *NB: het versienummer (...) van het bestand kan veranderen*

9. Run ``python -m src.index`` om het dashboard te starten. 

10. In je commandline verschijnt nu een url en wordt het Dashboard automatisch geopend in je browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser. Het Dashboard wordt gestart.

Alles is nu geïnstalleerd en zowel de VRTool als het Dashboard zijn klaar voor gebruik. Als je VRUtils (stap 8.) hebt geïnstalleerd kun je ook de preproccessing doen.

