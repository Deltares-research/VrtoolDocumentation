Installaties
=======================================

Voor alle stappen van de Veiligheidsrendement methode is de installatie van Python middels Anaconda of Miniconda noodzakelijk. Daarna moet voor elk onderdeel nog een aparte Python package gebruikt/geinstalleerd: 
* VRUtils voor de preprocessing van gegevens
* VRTool voor de veiligheidsrendementberekeningen
* VRDashboard voor analyse van de resultaten.

**Anaconda**

Om de installatie goed te doorlopen is het nodig om eerst Anaconda of Miniconda te installeren.

1. Installeer `Anaconda <https://www.anaconda.com/download>`_ of `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_

**Download bestanden** 

2. Download de bestanden via deze `link <https://github.com/Deltares-research/VrtoolDocumentation/raw/main/vrtool_docs/Bestanden/Installatie/Release.zip>`_. In deze zipfile staan de verschillende bestanden die nodig zijn voor de installatie en het gebruik van de VRTOOL, preprocessor en het dashboard.

3. Pak de zip-file uit en zet de ``tar.gz`` bestanden in een lege folder (we gebruiken even ``"C:\Veiligheidsrendement"`` als voorbeeld)

**Installeren van de software**

Volg de onderstaande stappen om de software te installeren en te gebruiken:

4. Open Anaconda Prompt en navigeer naar de gecreerde folder met ``cd "C:\Veiligheidsrendement"``

   *NB: afhankelijk van de gebruikersrechten kan het noodzakelijk zijn om Anaconda Prompt als administrator te starten. Klik daarvoor met de rechtermuisknop en selecteer `Als administrator uitvoeren`.*

5. Maak een lokaal environment aan met het volgende command: ``conda create -p "C:\Veiligheidsrendement\.env" python=3.10``.

   *NB: als hier al een environment staat dan wordt deze automatisch overschreven.*

6. Activeer de environment met ``conda activate "C:\Veiligheidsrendement\.env\"``

7. Run ``pip install vrtool-0.3.2.tar.gz`` om de VRTool te installeren

8. Run ``pip install vr_dash-0.5.0.tar.gz`` om het Dashboard te installeren

9. Run ``pip install VRSuiteUtils-0.3.2.tar.gz`` om VRUtils te te installeren waarmee we de preprocessing kunnen doen, Deze stap is niet nodig voor de tutorial. 

Alles is nu geïnstalleerd en zowel de VRTool als het Dashboard zijn klaar voor gebruik. Als je VRUtils (stap 8.) hebt geïnstalleerd kun je ook de preprocessing doen.

Voor het starten van het dashboard volg je de volgende stappen:

10. Run ``python -m src.index`` om het dashboard te starten. 

11.  In je commandline verschijnt nu een url en wordt het dashboard automatisch geopend in je browser. Mocht dit niet gebeuren, kopieer dan de url (http://127.0.0.1:8050/) en open deze in je browser. Het Dashboard wordt gestart.

