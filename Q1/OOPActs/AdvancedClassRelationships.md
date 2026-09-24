# CLASS RELATIONSHIPS: ASSOCIATION AND MULTIPLICITY
## MY OOP SEED SYSTEM 4
## MY PREVIOUS WORK
[Part II - Class Attributes and Methods](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/classAttributesMethods.md)

[Part III - Class Relationships](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/ClassRelationships.md)

---

**Section:** 9-Beryllium  
**Name:** Zanti Carlos B. Antero  
**Date:** Sep/24/2026  

---

## STEP 1: REVIEW EXISTING SYSTEMS
1. The existing classes I currently have are "BICYCLES" and "BIKE PARTS".
2. Without inheritance, creating a specific bike type would require me to copy ALL of "BICYCLES" attributes and methods, which would most likely cause a reapeating code.

---

## STEP 2: IDENTIFY PARENT CLASS
Parent Class: BICYCLES
Attributes: Frame Metal, Frame Color, Frame Brand, and Bike type

---

## STEP 3: CREATE CHILD CLASS
NEW Child Class: ELECTRIC BIKE

1. The parent class is BICYCLES
2. The new child class is ELECTRIC BIKE
3. The class ELECTRIC BIKE "is a" BICYCLES because, although electric, it still holds the same attributes as a normal bike.

---

## STEP 4: INHERITANCE UML
+ Text version:
```text
+--------------------------------------------+
|                  BICYCLES                   |
+--------------------------------------------+
| + type : string                             |
| + frame_metal : string                      |
| + frame_color : string                      |
| - __frame_brand : string                    |
| + frame : Frame                             |
| + bike_parts : list                         |
+--------------------------------------------+
| + repaint(new_color)                        |
| + get_frame_brand()                         |
| + describe()                                |
| + add_part(part_reference)                  |
| + list_parts()                              |
+--------------------------------------------+
                       |
                       |
+--------------------------------------------+
|                ELECTRICBIKE                  |
+--------------------------------------------+
| + battery_capacity_wh : int                 |
| + max_speed_kph : int                       |
| + battery_level : int                       |
+--------------------------------------------+
| + describe()  [overrides parent]            |
| + drain_battery(percent)                    |
+--------------------------------------------+
```
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/InheritanceDiagram.png)

---

## STEP 5: PYTHON FILE
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/Step%205.png)

## STEP 6: COMPOSITION OR AGGREGATION
My chosen relationship: Composition
Class containing another object: BICYCLES
Contained Object: Frame
Explanation: The parent class BICYCLES creates the frame.

---

## STEP 7: IMPLEMENT OWNERSHIP RELATIONSHIP
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/Step%207.png)

---

## STEP 8: OPTIONAL

---

## STEP 9: ADVANCED UML
+ Text version:
```text
+-------------------------+
│       BICYCLES          │      
+-------------------------+
│ - type                  │
│ - frame_metal           │
│ - frame_brand           │
│ - frame_color           │
│ - bike_parts            │
│ - frame                 │
+-------------------------+
│ + repaint()             │
│ + describe()            │
│ + add_part()            │
│ + list_parts()          │
+-------------------------+
            ◆
            │
            │ Composition
            ▼
+-------------------------+
│         Frame           │
+-------------------------+
│ - metal                 │
│ - brand                 │
│ - color                 │
+-------------------------+
│ + __str__()             │
+-------------------------+


+-------------------------+
│      ElectricBike       │
+-------------------------+
│ - battery               │
+-------------------------+
│ + describe()            │
+-------------------------+
            │         
            │
            △  
+-------------------------+
│       BICYCLES          │      
+-------------------------+
│ - type                  │
│ - frame_metal           │
│ - frame_brand           │
│ - frame_color           │
│ - bike_parts            │
│ - frame                 │
+-------------------------+
│ + repaint()             │
│ + describe()            │
│ + add_part()            │
│ + list_parts()          │
+-------------------------+

Extra:
+-------------------------+
│       BikeParts         │
+-------------------------+
│ - part_type             │
│ - color                 │
│ - quantity              │
+-------------------------+
│ + remove()              │
│ + purchase()            │
│ + sell()                │
+-------------------------+
+-------------------------+
│        Mechanic         │
+-------------------------+
│ - name                  │
+-------------------------+
│ + tune_up()             │
+-------------------------+
```
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/advancedClassDiagram.png)

---

## STEP 10: TEST
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/advancedTestRun.png)

---

## STEP 11: OBJECT RELATIONSHIP DIAGRAM
+ Text version:
```text
+---------------------------+
|          bike1            |
|       Bicycles object     |
+---------------------------+
| type: MountainBike        |
| frame_metal: Carbon       |
| frame_brand: Giant        |
| frame_color: Blue         |
+---------------------------+
            ◆
            │ owns
            ▼
+---------------------------+
|          Frame            |
+---------------------------+
| metal: Carbon             |
| brand: Giant              |
| color: Blue               |
+---------------------------+


+---------------------------+
|        electric1          |
|     ElectricBike object   |
+---------------------------+
| type: ElectricBike        |
| frame_metal: Carbon       |
| frame_brand: Giant        |
| frame_color: Blue         |
| battery: 500 Wh           |
+---------------------------+
            │
            │ inherits from
            ▼
+--------------------------+
│       BICYCLES           │      
+--------------------------+
│ - type                   │
│ - frame_metal            │
│ - frame_brand            │
│ - frame_color            │
│ - bike_parts             │
│ - frame                  │
+--------------------------+
│ + repaint()              │
│ + describe()             │
│ + add_part()             │
│ + list_parts()           │
+--------------------------+
```
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/advancedObjectDiagram.png)

---

## STEP 12: 
1. I chose ElectricBike as the child class of Bicycles because an electric bike is a type of bicycle. An ElectricBike has the same basic properties as a Bicycles object, such as type, frame, and color. Other than that also has an additional attribute, which is the battery.
2. Inheritance allowed ElectricBike to reuse the attributes and methods already written in the Bicycles class. ElectricBike can inherit type, frame_metal, frame_color, repaint(), and get_frame_brand(). This means I did not have to rewrite the same code inside the ElectricBike class.
3. My Bicycles and Frame relationship is Composition because the Bicycles object creates its own Frame object. The frame is created inside the Bicycles constructor using self.frame = Frame(something). This means the frame is part of its structure.
4. Association means that two classes are connected because one object uses or interacts with another object. The Mechanic can interact with a Bicycles object by tuning it up. Inheritance and composition create stronger relationships where ElectricBike is a type of Bicycles and Bicycles owns its Frame.
5. My design follows the DRY principle by avoiding repeated code between Bicycles and ElectricBike. Instead of rewriting the bicycle attributes and methods, ElectricBike inherits them from Bicycles. The Frame class also keeps frame-related information in one place instead of repeating it throughout the program.
