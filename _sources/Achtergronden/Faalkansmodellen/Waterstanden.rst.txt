Bepaling waterstanden
==========================

De waterstanden worden middels Hydra-Ring bepaald in de preprocessor. Hieruit volgen twee frequentielijnen: 

* De frequentielijn van de waterstand in de huidige situatie (2023) 
* De frequentielijn van de waterstand in de toekomst (2100)

Voor de toekomstige situatie kan gekozen worden voor één toekomstscenario (W+ of G+).

In de preprocessor zijn de waterstandsfrequentielijnen invoer voor de berekening van de faalkans van de dijkbekleding (en de relatie tussen bekledingsparameters na versterking en faalkans).
Binnen de VRTOOL worden de waterstandsfrequentielijnen gebruikt voor de faalkansberekening van piping: door bij de gewenste kans de waterstand te bepalen kan een semi-probabilistische pipingberekening worden gemaakt.

De waterstandsfrequentielijnen zijn in de database terug te vinden in de tabel `WaterlevelData` (zie `hier <../../Gebruikershandleiding/Preprocessing/Genereren_database.html#structuur-van-de-database>`_). Hierbij is enige postprocessing gedaan in de zin dat de frequentielijnen die uit Hydra-Ring komen door numerieke instabiliteit in sommige gevallen een kleinere kans op een lagere waterstand kunnen geven. Na het bepalen van de frequentielijnen wordt dit gecorrigeerd. Het oude bestand wordt daarbij opgeslagen met de extensie `.bak` zodat altijd vergeleken kan worden met de originele data.