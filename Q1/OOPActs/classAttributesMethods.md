# UNDERSTANDING CLASSES AND OBJECTS
## MY OBJECT-ORIENTED PROGRAM SEED SYSTEM

---

**Section:** 9-Beryllium                                                
**Name:** Zanti Carlos B. Antero
**Date:** Sep/08/2026

---

## STEP 1: REVIEW PREVIOUS DESIGN
Changes from my previous design:
- I added a fourth property.

---

## STEP 2: PUBLIC AND PRIVATE
| ATTRIBUTE | DATA TYPE | VISIBILITY | REASON |
| --- | --- | --- | --- |
| Type of Bike | String | PUBLIC | Can be accessed to identify the bike. |
| Frame Metal | String | PUBLIC | Can be accessed to know the frame material. |
| Frame Color | String | PUBLIC | Can be accessed to identify the bike’s color. |
| Frame Brand | String | PRIVATE | Protects the bike’s brand information. |

---

## STEP 3: UML DIAGRAM
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
```

![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/ANTERO-CLASS%20DATA%20SET.png)
![Click here](https://github.com/zcbantero-ui/9berylliumcs3/blob/main/Q1/Images/OOPActProof/ANTERO-CLASS%20DATA%20SET%20OBJECTS.png)

--- 

## SHORT ANALYSIS
1. I made the attribute "frame_brand" private so that it couldn't directly be changed.
2. The repaint() method changes the frame_color attribute, when called it should change color.
3. My two bicycle objects had different information. When I changed the color of one bicycle, the other bicycle’s color stayed the same, showing that the objects are independent.
4. The class diagram shows the blueprint of my BICYCLES class, including its attributes and actions. The object diagram shows actual bicycle objects and their specific information.
