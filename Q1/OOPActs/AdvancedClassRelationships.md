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
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/Advance%20Class%20Relationships.png)

---

## STEP 10: TEST
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/Step%2010%20-%20TEST%20RUN.png)

---

## STEP 11: 
