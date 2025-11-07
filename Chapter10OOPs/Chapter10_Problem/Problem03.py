#create a class with a class attribute a;
# create an object from it and set a directly using onjecta=0 
# Does it change the class attribute a?

class MyClass:
    a=10
obj=MyClass()
obj.a=0
print("Class dict:", MyClass.__dict__)  # Shows class-level attributes
print("Class attribute remain same",MyClass.a) 
print("Instance dict:", obj.__dict__)  # Shows only object-specific attributes
print("Object attribute changed ",obj.a)    
