# ANNEX A
## Computational Thinking Exercise: “Smart School Canteen Queue”

---

**Section:** 9-Beryllium                                                
**Name:** Zanti Carlos B. Antero
**Date:** Aug/17/2026

---

## Step 1: The BIG problem:
### The Main Problem
The school's canteen queue is extremely slow and inefficient because students take so long to decide what they want to eat, cashiers manually calculate payments and change, and there is no system for monitoring food inventory. 

---

## Step 2: Sub problems:
1. Students take too long to decide what to eat.
2. Cashiers manually calculate expenses.
3. There is no proper system for monitoring food inventory.

---

## Step 3: Computational Thinking Approaches:

| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| Students take too long to decide what to eat | Abstraction | Create a simple menu showing the available items, and its price. |
| Cashiers manually calculate expenses. | Algorithmic Design | Create a program that automatically calculates the total, and the change.|
| There is no inventory monitoring. | Pattern Recognition | Track the quantity of each food item and update the stock after every purchase. |

---

## Step 4: Pseudocode:
START

#Display food menu and prices

#Ask customer to select food items
Store selected items

Set total = 0

FOR each selected item
    Add item price to total
END FOR

#Display total amount

#Ask customer for payment

IF payment >= total THEN
    change = payment - total
    Display change
    Print order receipt
ELSE
    Display "Insufficient payment"
END IF

END
