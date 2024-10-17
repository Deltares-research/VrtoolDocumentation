Piping
======================

De betrouwbaarheid voor piping wordt bepaald met een semi-probabilitische Sellmeijer berekening. De relevante formules zijn terug te vinden in de betreffende technische leidraden/schematiseringshandleiding.

Belangrijk om op te merken is dat er in de VRTOOL een paar extra parameters worden gehanteerd:

* Voor de kwelweglengte worden 2 lengtes gehanteerd: :math:`L_{voor}` en :math:`L_{achter}`. Deze geven de kwelweglengte van intredepunt tot binnenteen respectievelijk binnenteen tot uittredepunt.

* Met de parameter :math:`dh_{exit}` wordt de jaarlijkse bodemdaling van het achterland ingevoerd. Deze parameter wordt gebruikt om de bodemhoogte bij het uittredepunt te verlagen wat resulteert in een hogere stijghoogte en daarmee een hogere kans op piping.

* Met de parameter `kwelscherm` wordt aangegeven of er al een kwelscherm aanwezig is. Wanneer deze aanwezig is wordt het kritisch verval voor deelmechanisme heave aangenomen op 0.5 in plaats van 0.3.

De te hanteren waterstand wordt afgeleid uit de waterstandsfrequentielijnen die worden afgeleid met Hydra-Ring. Daarmee wordt ook de invloed van klimaatverandering meegenomen.
