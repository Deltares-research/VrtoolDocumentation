Piping
======================

De betrouwbaarheid voor piping kan op twee manieren worden ingevoerd: via een semi-probabilitische Sellmeijer berekening of door de betrouwbaarheidsindex direct in te voeren. 

Semi-probabilistische Sellmeijer berekening
------------------------------------------------

De meest gangbare methode bij veiligheidsrendementanalyses is om een semi-probabilitische Sellmeijer berekening uit te voeren. De relevante formules zijn terug te vinden in de betreffende technische leidraden/schematiseringshandleiding. Deze berekening is ingebouwd in de VRTOOL.

Belangrijk om op te merken is dat er in de VRTOOL een paar extra parameters worden gehanteerd:

* Voor de kwelweglengte worden 2 lengtes gehanteerd: :math:`L_{voor}` en :math:`L_{achter}`. Deze geven de kwelweglengte van intredepunt tot binnenteen respectievelijk binnenteen tot uittredepunt.

* Met de parameter :math:`dh_{exit}` wordt de jaarlijkse bodemdaling van het achterland ingevoerd. Deze parameter wordt gebruikt om de bodemhoogte bij het uittredepunt te verlagen wat resulteert in een hogere stijghoogte en daarmee een hogere kans op piping.

* Met de parameter `kwelscherm` wordt aangegeven of er al een kwelscherm aanwezig is. Wanneer deze aanwezig is wordt het kritisch verval voor deelmechanisme heave aangenomen op 0,5 in plaats van 0,3.

De te hanteren waterstand wordt afgeleid uit de waterstandsfrequentielijnen die worden afgeleid met Hydra-Ring. Daarmee wordt ook de invloed van klimaatverandering meegenomen.

Direct invoeren van de betrouwbaarheidsindex
------------------------------------------------
Een alternatief is om direct in de database de betrouwbaarheidsindex in te voeren. Dit kan handig zijn wanneer er een andersoortige berekening is uitgevoerd (bijv. een probabilistische Sellmeijer berekening of een berekening met D-Geo Flow). Dit werkt op een vergelijkbare manier als de invoer voor stabiliteit binnenwaarts. Bij gebruik van deze functie zijn 2 nadelen ten opzichte van de gebruikelijke methode op basis van de semi-probabilitische Sellmeijer berekening:

1. Omdat er geen koppeling met de waterstand is is de betrouwbaarheidsindex constant in de tijd. Effecten van klimaatverandering op de betrouwbaarheid van piping worden dus niet meegenomen.
2. Voor de maatregelen wordt het effect van een berm op piping niet meegenomen. Grondversterking verhoogt dus niet de betrouwbaarheid van piping, daarvoor zijn verticale maatregelen nodig.
