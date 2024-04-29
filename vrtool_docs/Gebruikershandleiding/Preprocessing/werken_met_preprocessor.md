# Werken met de preprocessor


Alle workflows (de blauwe rechthoeken in de figuur van de preprocessor) gebruiken dezelfde drie stappen.

#### 1. Om workflows te draaien moet Anaconda prompt worden opgestart

![Opening_Anaconda_promt.PNG](Opening_Anaconda_promt.PNG)

#### 2. Daarna moet het environment worden geactiveerd

Het activeren van een environment kan op twee manieren:

a) Ga naar de juiste directory en activeer daarna het environment. Dit kan door de volgende commanda in Anaconda in te voeren. 

```cd C:/link_naar_ZIP_file_map```

```conda activate .env/```

b) Activeer direct je environment door de volgende commando in te voeren in Anaconda:

```conda activate C:/link_naar_ZIP_file_map.env/```

*Vervang "C:/link_naar_ZIP_file_map" met de locatie van de map waar de ZIP file is uitgepakt.*

**Let op:** als je het environment een andere naam hebt gegeven, vervang ".env" dan door de naam die je aan het environment gegeven hebt.

#### 3. Als laatste kan de workflow gedraaid worden

Het draaien van de workflow gebeurd altijd met dezelfde commando. Alleen de naam van de workflow moet steeds aangepast worden en de invoerparameters moeten aangeleverd worden.

```python -m preprocessing workflow_naam {input arguments}```

Met de volgende commando kan alle benodigde invoerparameters van een workflow gevonden worden.

```python -m preprocessing workflow_naam --help``` 

Meer informatie over de invoerparameters per workflow: 
- [Vakindeling](Vakindeling.md)
- [Overslag](Overtopping.md)
- [Waterstand](Waterstand.md)
- [Bekleding](Bekleding.md)
- [Bebouwing](Bebouwing.md)
- [Dijkprofielen](Dijkprofielen.md)
- [Teenlijn](Teenlijn.md)
- [Genereren database](Genereren_database.md)