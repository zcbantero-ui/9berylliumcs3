# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation is used by gathering all important informaition of a product, like the product name, price, content, and etc,. This keeps the product information organized.

### 2. Abstraction
Abstraction can be used by providing simple methods such as sell() and restock() for managing products. Basically it shows only the important stuff, instead of the complicated stuff, which makes the system easier to use and understand.

### 3. Inheritance
Inheritance can be used by creating a general Product class and having more specific classes such as FoodProduct and DrinkProduct inherit from it. The child classes can reuse properties such as name, price, and stock. This reduces repeated code and makes the system easier to expand.

### 4. Polymorphism
Polymorphism can be used when different types of products have the same method but perform it differently. For example, both food and drink products can have a sell() method while handling their inventory in their own way. This allows the program to work with different product types using the same method name.

## Reflection
Among the four pillars, I think encapsulation would be the most useful for the sari-sari store inventory system. It keeps the product information and the methods that manage it together, making the program more organized. It can also make the inventory easier to update because each product manages its own information. Overall, encapsulation would make the program simpler to understand and maintain
