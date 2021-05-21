### MVC architecture
    1. A user requests to view a page by entering a URL.
    2. The application matches the URL to a predefined route.
    3. The controller action associated with the route is called.
    4. The controller action uses the models to retrieve all of the necessary data from database, places the data in an array, and loads a view, passing along the data structure.
    5. The view accesses the structure of data and uses it to render the requested page, which is then presented to the user in their browser.

    [LINKS](https://realpython.com/the-model-view-controller-mvc-paradigm-summarized-with-legos/)

### OOPS
    1. What is Class?
        Class is the blueprint of object.
    
    2. What is Object?
        Object is the instance.

    3. What are Properties?
        Properties define the state of the object.

    4. What are Behaviours?
        Behaviors are the actions our object can take. 

    5. What is isinstance()?
        Check if an object inherits from another class.
    
    6. What is Inheritace?
        Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.

    7. What is super()?
        Super() search the parent class for a method or an attribute. It traverses the entire class hierarchy for a matching method or attribute.
        Calling the previously built methods with super() saves you from needing to rewrite those methods in your subclass, and allows you to swap out superclasses with minimal code changes.

    8. What is MRO?
        MRO is Method Resolution Order. The MRO tells you exactly where Python will look for a method you’re calling with super() and in what order.

    9. What are Instance Methods?
        Regular Methods of class are Instance Methods. They can modify class and object state.
        ** Instance methods need a class instance and can access the instance through self.

    10. What are Class Methods?
        A @classmethod decorator flag is a class method. Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called. Class methods can still modify class state that applies across all instances of the class but not the object instance.
        ** Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.

    11. What are Static Methods?
        A @staticmethod decorator flag is a static method. This type of method takes neither a self nor a cls parameter. Therefore a static method can neither modify object state nor class state. Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.
        ** Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.

    12 . Function overloading
        https://realpython.com/operator-function-overloading/

    13. What are decorator?
        Decorators wrap a function, modifying its behavior. Python allows you to use decorators in a simpler way with the @ symbol. Decorators should use the @functools.wraps decorator, which will preserve information about the original function.
        https://realpython.com/primer-on-python-decorators/
