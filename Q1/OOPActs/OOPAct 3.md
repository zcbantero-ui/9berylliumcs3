# CONNECTING MY OBJECTS
## MY OOP SEED SYSTEM 3

---

**Section:** 9-Beryllium                                                
**Name:** Zanti Carlos B. Antero
**Date:** Sep/11/2026

---

## STEP 1: REVIEW EXISTING CLASS
1. Class "BICYCLES"
2. It represents a basic mode of transportation.
3. The attribute that could still be useful on other classes would probably be the Bike Type, since with that information figuring the type of parts it may need would be easily accesible. While the method repair() could be used on other classes which have the capability of breaking down.

---

## STEP 2: CREATE A NEW CLASS
1. New class "BIKE PARTS".
2. Bicycles are composed of many parts which are needed for the bike to function properly in correlation to the bike type.
3. These two classes should be connected so that when a bike requires reparations, or renewal of gears/parts, the identification process would be much easier.

---

## STEP 3: IDENTIFY THE ASSOCIATION
"BICYCLES contain BIKE PARTS"

---

## STEP 4: DECIDE MULTIPLICITY
1. Option B - 1:many
  BICYCLE 1 ----- BIKE PARTS many
2. All bikes are composed of many parts. I chose this multiplicity because for every one bike there is always many parts present for it to function properly, you can't own a wheel and call it a bike.

---

## STEP 5: UPDATE UML DIAGRAM 
+ Text version:
```text
+--------------------------------------------+
|                  BICYCLES                   |
+--------------------------------------------+
| + type : string                             |
| + frame_metal : string                      |
| + frame_color : string                      |
| + frame_brand : string                      |
+--------------------------------------------+
| + ride()                                    |
| - repair(bike: string)                      |
| - repaint(bike_color : string)              |
| + sell()                                    |
+--------------------------------------------+
                       1
                       |
                       |
                       | contains
                       |
                       |
                       *
+--------------------------------------------+
|                 BIKE PARTS                  |
+--------------------------------------------+
| + type : string                             |
| + color : string                            |
| + quantity : int                            |
+--------------------------------------------+
| + install(quantity : int)                   |
| + remove(quantity : int)                    |
| + purchase(quantity : int)                  |
| + sell()                                    |
+--------------------------------------------+
```
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/BICYCLES%20and%20BIKE%20PARTS%20-%20ASSOCIATION.png)


---

## STEP 6: CLASS RELATIONSHIPS
[View my Chinese Zodiac Program](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/ClassRelationships.py)

---

## STEP 11: TEST RUN
