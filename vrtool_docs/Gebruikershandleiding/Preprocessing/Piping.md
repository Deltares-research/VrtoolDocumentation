**NB: Dit gedeelte is niet up-to-date en wordt in de komende weken aangepast**

# Piping

Voor piping bevat de preprocessing maar 1 stap: het invullen van het invoerbestand `Piping_default.csv`. Dit bestand is terug te vinden in: ```.\VRSuiteUtils-main\preprocessing\default_files``` in de folder met de uitgepakte installatie voor de [preprocessing](..\Installaties\VRUtils.md).

Dit bestand heeft de volgende kolommen die ingevuld moeten worden:

| Kolom       	 | 	         | Beschrijving                                                                                                                                                                                 	                                        |
|----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| doorsnede | Verplicht 	 | Naam van het dwarsprofiel. In het geval van de uittredepuntenmethode is dit het ID van het punt                                                                                                                                     	 |
| scenario | Verplicht 	 | Indien er meerdere ondergrondscenario's zijn, dient hier het scenario ID te worden ingevoerd. Deze moet een nummer zijn.                                                                                                              |
| scenariokans | Verplicht | Conditionele kans op het ondergrondscenario [-]                                                                                                                                                                                       |
| mhw      | Verplicht 	 | Maatgevend hoogwater [m+NAP]                                                                                                                                                                                                          |
| polderpeil | Verplicht 	 | Polderpeil [m+NAP]                                                                                                                                                                                                                    |
| d_wvp    | Verplicht 	 | Dikte van het watervoerend pakket [m]	                                                                                                                                                                                                |
| d70      | Verplicht 	 | Zeefmaat die 70% (massa) van de zandkorrels van de zandfractie laat passeren [m]	                                                                                                                                                     |
| d_cover 	 | Verplicht 	 | Dike van de deklaag [m]                                                                                                                                                                                                               |
| h_exit 	 |  Verplicht 	 | Bodemhoogte bij uittredepunt [m+NAP]	                                                                                                                                                                                                 |
| r_exit   | Verplicht 	 | Dempingsfactor bij uittredepunt [-] (afname van stijghoogte in watervoerend pakket ten gevolge van lek door slappelagenpakket)	                                                                                                       |
| l_voor  	 | Verplicht 	 | Leklengte intredepunt tot binnenteen dijk [m]                                                                                                                                                                                         |
| l_achter | Verplicht | Leklengte binnenteen tot uittredepunt [m]	                                                                                                                                                                                            |
| k  	     | Verplicht 	 | Doorlatendheid van het watervoerend pakket [m/s]	                                                                                                                                                                                     |
| gamma_sat | Verplicht 	 | Verzadigd gewicht van de deklaag [kN/m3]	                                                                                                                                                                                             |
| kwelscherm | Verplicht 	 | Aanwezigheid kwelscherm. 0 = kwelscherm afwezig, 1 = kwelscherm aanwezig	                                                                                                                                                             |
| dh_exit 	 | Verplicht 	 | Jaarlijkse bodemdaling van het achterland [m/jaar]	                                                                                                                                                                                   |
| pf_s 	   |  Optioneel | Jaarlijkse faalkans, gegeven het ondergrondscenario [-]. Optioneel, vooral handig als check	                                                                                                                                          |
| m_value  | Verplicht 	 | De M-waarde van het uittredepunt of de doorsnede [m]. Bij uittredepunten kan de m-waarde ook worden berekend, indien x-,y-coordinaten zijn gegeven. 	                                                                                 |
| x_coord  	 | Verplicht | In het geval dat de uittredepuntenmethode is gebruikt, moet hier de x-coordinaat van het punt worden ingevuld (rijksdriehoekscoördinaten)                                                                                             |
| y_coord  | Verplicht | In het geval dat de uittredepuntenmethode is gebruikt, moet hier de y-coordinaat van het punt worden ingevuld (rijksdriehoekscoördinaten)	                                                                                            |

