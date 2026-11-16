# Zanti Carlos B. Antero
# 9 - Beryllium
# Nov/16-17/2026


1. Answer the following questions:
  a. What is duck typing, as explained in the video?
    Duck typing means Python doesn’t care what class an object is. It only cares whether the object has the method or attribute you’re trying to use. The name comes from the saying: “If it walks like a duck and quacks like a duck, it must be a duck.”
  b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
    An alive attribute which is false since it doesn't inherit from the given animals class in the video, and the same method child classes Dog and Cat have which in the video was speak().

2. Create the Python code that:
  a. Creates three classes: Car, Boat, and Drone with a method move().
    move() in the Car class prints "The car drives on the road."
    move() in the Boat class prints "The boat sails on water."
    move() in the Drone class prints "The drone flies in the sky."
  b. Has a function named start_trip(vehicle), with a parameter vehicle, that simply calls the
    move() method: vehicle.move().
  c. Creates one object of each class.
  d. Calls the start_trip() method for each object.

4. How does the code in 2.2 demonstrate polymorphism?
