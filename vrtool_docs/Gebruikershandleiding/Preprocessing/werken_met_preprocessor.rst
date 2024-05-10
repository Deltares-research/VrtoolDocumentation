================================
Werken met de preprocessor
================================

Opstarten van de preprocessor
=============================

Alle workflows (de blauwe rechthoeken in de overzichtsfiguur) gebruiken dezelfde stappen. Om workflows uit te voeren moet eerst Anaconda Prompt worden opgestart en het environment worden geactiveerd.
Het activeren van een environment kan door het volgende command in Anaconda in te voeren. 

.. code-block:: bash

    conda activate C:/Veiligheidsrendement/.env/

.. note::
    **Let op:**
    Vervang ``"C:/Veiligheidsrendement"`` met de locatie van de map waar de verschillende bestanden zijn neergezet.
    
    Als je het environment een andere naam hebt gegeven, vervang ``".env"`` dan door de naam die je aan het environment gegeven hebt.


Aanmaken van een mappenstructuur
================================

De tweede stap is om een werkmap te maken voor de preprocessor. Dat gebeurt met een aparte workflow ``maak_project``. Hierin wordt automatisch een complete mappenstructuur aangemaakt waarmee de preprocessor uit de voeten kan. Dit is te doen via het volgende commando:

.. code-block:: bash

    python -m preprocessing maak_project --project_folder {projectfolder} --traject_id {traject_id}

Bij ``{projectfolder}`` moet de locatie van de map worden ingevuld waar de mappenstructuur moet worden aangemaakt, bijvoorbeeld ``"C:/Veiligheidsrendement/preprocessor_werkmap"``. Bij ``{traject_id}`` moet het traject worden ingevuld, bijvoorbeeld ``"24-3"``.

.. note::
    **Tip** 
    Voor de verschillende workflows kan met ``python -m preprocessing workflow_naam --help`` een overzicht van de invoerparameters worden opgevraagd.

De mappenstructuur die wordt aangemaakt ziet er als volgt uit:

.. figure:: img/Mappenstructuur.png
   :alt: Mappenstructuur
   :align: center

   Mappenstructuur t.b.v. de preprocessor

De structuur van de werkmap
___________________________

In de map ``input_files`` zijn 5 submappen aangemaakt:

* ``bag_gebouwen``: hierin kan een geopackage van de Basisadministratie Adressen en Gebouwen (BAG) worden geplaatst. Deze is te downloaden vanaf de website van `PDOK<https://service.pdok.nl/lv/bag/atom/downloads/bag-light.gpkg>`_. Let op: dit is een zeer groot bestand (ca. 7 GB), dus het kan even duren.
* ``default_files``: hierin kunnen de standaardinvoerbestanden (ingevuld) worden neergezet.
* ``HR_databases``: hier kunnen de hydraulische databases worden geplaatst voor 2023 (WBI) en 2100 (ontwerpdatabases). Deze zijn `hier<https://fbwvl.stackstorage.com/s/cQJwECwRv88jqsc/nl>`_ te downloaden. Elke map moet 1 database bevatten (combinatie van HRD, HLCD-bestand en .config bestand zoals aangeboden op de website).
* ``prfl``: hier kunnen de `*.prfl`-bestanden worden geplaatst ten behoeve van de workflows voor overloop/overslag en bekleding.
* ``steentoets``: indien van toepassing kunnen hier de Steentoetsbestanden uit de beoordeling worden geplaatst.

In de map ``intermediate_results`` worden de resultaten van de workflows opgeslagen. Hierin zijn 6 submappen aangemaakt. De inhoud hiervan wordt bij de betreffende workflows nader toegelicht.

In de map ``vrtool_database`` wordt de database weggeschreven die nodig is voor de VRTool. 

In totaal zijn er 8 workflows, meer informatie over de invoerparameters per workflow is te vinden via onderstaande links: 

- `Vakindeling <Vakindeling.rst>`_
- `Overslag <Overtopping.rst>`_
- `Waterstand <Waterstand.rst>`_
- `Bekleding <Bekleding.rst>`_
- `Bebouwing <Bebouwing.rst>`_
- `Dijkprofielen <Dijkprofielen.rst>`_
- `Teenlijn <Teenlijn.rst>`_
- `Genereren database <Genereren_database.rst>`_