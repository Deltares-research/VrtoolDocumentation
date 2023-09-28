# Installatie van het Dashboard

Het dashboard draait vooralsnog lokaal. Vaak zal dit zijn via een uitgeleverde zip-file met daarin alle benodigde bestanden.
 Volg de onderstaande stappen om het dashboard te installeren en te gebruiken:

1. Pak het zip-bestand uit in een lokale folder naar keuze.

2. Navigeer naar deze folder, en maak een virtuele omgeving aan (zorg ervoor dat u al [Anaconda](Anaconda.md) geïnstalleerd heeft).
    ```bash
    cd C:\repos\VrtoolDashboard
    conda env create -f .config\environment.yml
    conda activate vrtool_dash
    poetry install
    ```
Als de installatie met poetry niet succesvol is en er foutmeldingen verschijnen, voer dan ```poetry install``` opnieuw uit.

3. Het dashboard is nu geïnstalleerd en klaar voor gebruik. Om het dashboard te starten, voert u de volgende opdracht uit:

   ```bash
   python -m src.index

Het dashboard zou moeten verschijnen in uw standaardbrowser. Als dit niet automatisch gebeurt, navigeer dan naar het http-adres dat in de terminal wordt weergegeven. Als het dashboard al is geïnstalleerd, is alleen de derde stap vereist om het dashboard opnieuw te starten (op voorwaarde dat de virtuele omgeving is geactiveerd, zo niet voer dan conda activate vrtool_dash opnieuw uit). ```