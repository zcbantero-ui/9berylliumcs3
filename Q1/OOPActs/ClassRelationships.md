# CLASS RELATIONSHIPS: ASSOCIATION AND MULTIPLICITY
## MY OOP SEED SYSTEM 3
## MY PREVIOUS WORK
[Part I - Classes and Objects](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/BerylliumBicycleANTERO.md)
[Part II - Class Attributes and Methods](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/classAttributesMethods.md)

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
1. "BICYCLES contain BIKE PARTS"
2. A bicycle is made up of many bike parts.

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
[View my Class Relationship.py](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/OOPActs/ClassRelationships.py)

---

## STEP 11: TEST RUN
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/TEST%20RUN.png)

---

## STEP 12: OBJECT RELATIONSHIP DIAGRAM
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/ObjectRelationshipDiagram.png)

---

## STEP 13: ANALYSIS
### 1. BICYCLES and BIKE PARTS are connected through a "contains" relationship. This is because a bicycle is made up of several parts, and having the two classes connected makes it easy to identify which parts belong to which bike whenever a repair or a renewal of gears/parts is needed. In my implementation, each BICYCLE object keeps a list of the actual BIKE PRATS attached to it, so the bike can look up its own parts directly instead of the two classes existing separately.
  
### 2. I chose a 1:many multiplicity, where one bicycle is connected to many bike parts. I chose this because, again, every bike is composed of many parts working together in order to function properly. You can't own a single wheel and call it a bike, so a bicycle will always need more than one part attached to it.
   
### 3. In my classRelationships.py file, the "BICYCLES" class stores a list attributes that holds the related "BIKE PARTS" objects. Whenever a part needs to be connected to a bike, a method is used to apend that BikePart object reference into the list, forming the actual relationship between the two classes.

### 4. Storing the object reference instead of copying its data, means the bicycle always has access to the part's current, up-to-date information. If a part's quantity or details change later, the bicycle doesn't need to be updated separately. It can just check the actual object it's already connected to.

### 5. A list is appropriate since a bicycle can have several parts, and that number can change as parts get added or removed. The list holds actual "BIKE PARTS" objects, not plain text or numbers. Looping through it lets the user to directly access each part's real attributes, like its type, color, and quantity.
