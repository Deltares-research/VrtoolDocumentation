Afleiden bebouwing
==================

De workflow ``tel_gebouwen`` gebruikt de binnenteen-GeoJSON en de vakindeling-GeoJSON als invoerbestand. Daarnaast is een Geopackage bestand nodig van de BAG (Basis Administratie Gebouwen). Op dit moment is het nog niet mogelijk meer dan 1000 gebouwen rechtstreeks uit de BAG te halen via internet. Daarom moet de Geopackage van de BAG direct naar een lokale schijf worden gedownload. Dat kan hier: https://service.pdok.nl/lv/bag/atom/bag.xml (Let er op dat je de Geopackage download). Deze moet worden geplaatst in `bag_gebouwen_geopackage`

De workflow kan worden gestart met het volgende commando:

::

   python -m preprocessing tel_gebouwen --config_file {config_bestand}

Met deze workflow worden de gebouwen geteld die aan de dijkvakken grenzen. Voor buffers van 1, 2 tot en met 50 meter uit de teen wordt het aantal panden uit de BasisAdministratie Gebouwen geteld. Bij deze workflow is het van belang dat de teenlijn correct is afgeleid en dat de instelling `flip_traject` goed staat in het config-bestand: wanneer deze omgekeerd wordt, wordt de buffer aan de verkeerde kant van de dijk geplaatst. Het is aan te bevelen na het uitvoeren van de workflow de resultaten (steekproefsgewijs) te controleren. De resultaten worden weggeschreven in `gebouwen_csv`.