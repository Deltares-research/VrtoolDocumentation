****************************************************
# Installaties
****************************************************

**Anaconda**

Om de installatie goed te doorlopen is het nodig om Anaconda of Miniconda te installeren. Daarnaast hebben we een van deze terminals ook nodig tijdens het gebruik van de VRTOOL. 

1. Installeer [anaconda](https://www.anaconda.com/download) of [miniconda](https://docs.conda.io/en/latest/miniconda.html)

**Download bestanden** 

Download de bestanden via deze [link](sharepoint.nl). Dit is een zip-file met daarin verschillende bestanden die nodig zijn voor de installatie en het gebruik van de VRTOOL .

 2. Pak het zip-bestand uit en zet de ```tar.gz``` bestanden in een lege folder (we gebruiken even C:\Veiligheidsrendement als voorbeeld)

**VRTOOL & Dashboard**

Het dashboard draait vooralsnog lokaal. Volg de onderstaande stappen om het dashboard te installeren en te gebruiken:

 3. Navigeer in Anaconda Prompt (zorg ervoor dat [Anaconda](Anaconda.md) geïnstalleerd is) naar de gecreerde folder met ```cd "C:\Veiligheidsrendement"```

 4. Maak een lokaal environment aan met het volgende command: ```conda create -p "c:\Veiligheidsrendement\.env" python=3.10```.

    *NB: als hier al een environment staat dan wordt deze automatisch overschreven.*

 6. Activeer de environment met ```conda activate "C:\Veiligheidsrendement\.env\"```

7. Run ```pip install vrtool-0.1.3.tar.gz``` om de VRTOOL te installeren

    *NB: het versienummer (0.1.3.) van het bestand kan veranderen*

8. Run ```pip install vr_dash-0.3.2.tar.gz``` om het Dashboard te installeren

    *NB: het versienummer (0.3.2.) van het bestand kan veranderen*

9. Run ```pip install vr_utils-....tar.gz``` om alles te installeren voor preprocessing. Deze stap is niet nodig voor de VRTOOL tutorial.

    *NB: het versienummer (...) van het bestand kan veranderen*

10. Run ```python -m src.index``` om het dashboard te starten. 

11. Kopieer de url (http://127.0.0.1:8050/) die in de commandline verschijnt en open die in je browser. Het dashboard wordt geopend.
