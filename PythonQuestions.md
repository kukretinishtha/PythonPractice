### Python Basics
    1. What are different Data Types in Python?
        1. Text Type: 	str
        2. Numeric Types: 	int, float, complex
        3. Sequence Types: 	list, tuple, range
        4. Mapping Type: 	dict
        5. Set Types: 	set, frozenset
        6. Boolean Type: 	bool
        7. Binary Types: 	bytes, bytearray, memoryview

    2. Examples of Boolean values which will return false
        bool(False)
        bool(None)
        bool(0)
        bool("")
        bool(())
        bool([])
        bool({})

    3. What ae python arithmetic operators?
        Arithmetic operators are used with numeric values to perform common mathematical operations:
        + 	Addition 	x + y 	
        - 	Subtraction 	x - y 	
        * 	Multiplication 	x * y 	
        / 	Division 	x / y 	
        % 	Modulus 	x % y 	
        ** 	Exponentiation 	x ** y 	
        // 	Floor division 	x // y

    4. What are assignment operators?
        Assignment operators are used to assign values to variables:
        = 	x = 5 	x = 5 	
        += 	x += 3 	x = x + 3 	
        -= 	x -= 3 	x = x - 3 	
        *= 	x *= 3 	x = x * 3 	
        /= 	x /= 3 	x = x / 3 	
        %= 	x %= 3 	x = x % 3 	
        //= 	x //= 3 	x = x // 3 	
        **= 	x **= 3 	x = x ** 3 	
        &= 	x &= 3 	x = x & 3 	
        |= 	x |= 3 	x = x | 3 	
        ^= 	x ^= 3 	x = x ^ 3 	
        >>= 	x >>= 3 	x = x >> 3 	
        <<= 	x <<= 3 	x = x << 3

    5. What are compaarison operators?
        Comparison operators are used to compare two values:
        == 	Equal 	x == y 	
        != 	Not equal 	x != y 	
        > 	Greater than 	x > y 	
        < 	Less than 	x < y 	
        >= 	Greater than or equal to 	x >= y 	
        <= 	Less than or equal to 	x <= y

    6. What are logical operators?
        Logical operators are used to combine conditional statements:
            and  	Returns True if both statements are true 	x < 5 and  x < 10 	
            or 	Returns True if one of the statements is true 	x < 5 or x < 4 	
            not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)

    7. What are identity operrators?
        Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

            is  	Returns True if both variables are the same object 	x is y 	
            is not 	Returns True if both variables are not the same object 	x is not y

    8. What are membership operators?
        Membership operators are used to test if a sequence is presented in an object:
        
            in  	Returns True if a sequence with the specified value is present in the object xin y 	
            not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y

    9. What are Python Bitwise Operators?
        Bitwise operators are used to compare (binary) numbers:

            &  	AND 	Sets each bit to 1 if both bits are 1
            | 	OR 	Sets each bit to 1 if one of two bits is 1
            ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
            ~  	NOT 	Inverts all the bits
            << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
            >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

    10. What are Collections?
        There are four collection data types in the Python programming language:
            List is a collection which is ordered and changeable. Allows duplicate members.
            Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
            Set is a collection which is unordered and unindexed. No duplicate members.
            Dictionary is a collection which is ordered* and changeable. No duplicate members.

    11. List methods?
        append()	Adds an element at the end of the list
        clear()	Removes all the elements from the list
        copy()	Returns a copy of the list
        count()	Returns the number of elements with the specified value
        extend()	Add the elements of a list (or any iterable), to the end of the current list
        index()	Returns the index of the first element with the specified value
        insert()	Adds an element at the specified position
        pop()	Removes the element at the specified position
        remove()	Removes the item with the specified value
        reverse()	Reverses the order of the list
        sort()	Sorts the list

    12. Dictionary Methods?
        clear()	Removes all the elements from the dictionary
        copy()	Returns a copy of the dictionary
        fromkeys()	Returns a dictionary with the specified keys and value
        get()	Returns the value of the specified key
        items()	Returns a list containing a tuple for each key value pair
        keys()	Returns a list containing the dictionary's keys
        pop()	Removes the element with the specified key
        popitem()	Removes the last inserted key-value pair
        setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
        update()	Updates the dictionary with the specified key-value pairs
        values()	Returns a list of all the values in the dictionary
        
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


### Higher Order functions
    1. Map function
        Python’s map() is a built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop, a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
        ===> map(function, iterator)

    2. Reduce function
        Python’s reduce() is a function that implements a mathematical technique called folding or reduction. reduce() is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.
        2.1 Working:
            2.1.1 Apply a function (or callable) to the first two items in an iterable and  generate a partial result.
            2.1.2 Use that partial result, together with the third item in the iterable, to generate another partial result.
            2.1.3 Repeat the process until the iterable is exhausted and then return a single cumulative value.
            ===> map(function, [iterator1, iterator2, ...])

    3.  Filter function
            Filtering applies a predicate, or Boolean-valued, function to an iterable and generates a new iterable containing the items that satisfy the Boolean condition.
            ===> filter(function, iterable)

    4. Anonymous function
            Anonymous function is a function without a name. In Python, an anonymous function is created with the lambda keyword. More loosely, it may or not be assigned a name. Consider a two-argument anonymous function defined with lambda but not bound to a variable. 

    4. Lambda function
            A lambda function can take any number of arguments, but can only have one expression.
            ===> lambda(parameter, expression/function)
    

### Python Environments [Dependency and Workspace Management]
    1. What is pyenv?
        pyenv is tool that simplifies installing and switching between different versions of Python on the same machine. It keeps the system version of Python intact, which is required for some operating systems to run properly, while still making it easy to switch Python versions based on a specific project's requirements.
        ** Unfortunately, pyenv does not work on Windows outside the Windows Subsystem for Linux.

    2. Need of Virtual Environment?
        Virtual environments prevent dependency version conflicts. You can install different versions of the same dependency in different virtual environments.

    3. What is poetry?
        Poetry is arguably the most feature-rich dependency management tool for Python. It comes with a powerful CLI used for creating and managing Python projects.

    4. What is pip?
        pip is package installer for python.

    
### Test-Driven Development in Python

    1. What is conftest.py? 
        conftest.py file is used for storing pytest fixtures.

    2. What is pytest.py?
        pytest.ini is a pytest configuration file to the "tests" folder.

    3. What is  Active Record-style model?
        Active Record-style model provides methods for storing, fetching a single article, and listing all articles.

    4. What are fixtures?
        To clear the database after each test and create a new one before each test we can use pytest fixtures. These are functions decorated with a @pytest.fixture decorator. They are usually located inside conftest.py but they can be added to the actual test files as well. These functions are executed by default before each test.

    5. What are JSONSchemas?
        JSON Schemas are used to define the responses from API endpoints.

    6. What is pytest-cov?
        pytest code coverage is given by pytest-cov?

### Security Vulnerability

    1. What is Bandit?
        Bandit is a tool designed to find common security issues in Python code such as hardcoded password strings, deserializing untrusted code, using pass in except blocks, to name a few.
    
    2. What is Safety?
        Safety is another tool that comes in handy for keeping your code free of security issues.
        It's used to check your installed dependencies for known security vulnerabilities against Safety DB, which is a database of known security vulnerabilities in Python packages.


### Code Formatters
    1. What is isort?
        isort is used to automatically separate imports in your code into the following groups:
        3.1 standard library
        3.2 third-party
        3.3 local

    2. What is Black?
        Black is a Python code formatter that's used to reformat your code based on the Black's code style guide, which is pretty close to PEP-8.

    3. What is Flake8?
        Flake8 is a wrapper around Pyflakes, pycodestyle, and McCabe.


### Development with Dockerizing Django with Postgres, Gunicorn, and Nginx
    Follow the Link:
    https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

### Securing a Containerized Django application
    Follow the link:
    https://testdriven.io/blog/django-lets-encrypt/

### Deploying a Django to AWS
    Follow the link:
    https://testdriven.io/blog/django-docker-https-aws/

### Asynchronous Task with Django and
    Follow the link:
    https://testdriven.io/blog/django-and-celery/


### Handling Periodic Task with Django
    Follow the link:
    https://testdriven.io/blog/django-celery-periodic-tasks/

### Automatically retrying celeri Task
    Follow the link:
    https://testdriven.io/blog/retrying-failed-celery-tasks/

## Advanced Questions in Python
    1. Relation between Metaclass, Class and object
        create Classes and Classes creates objects.

    2. What are Process?
        A process is an instance of a computer program that is being executed. 
        2.1 An executable program.
        2.2 The associated data needed by the program (variables, work space, buffers, etc.)
        2.3 The execution context of the program (State of process)

    3. What are Threads?
        A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).
        A thread contains all this information in a Thread Control Block (TCB):

        Thread Identifier: Unique id (TID) is assigned to every new thread
        Stack pointer: Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
        Program counter: a register which stores the address of the instruction currently being executed by thread.
        Thread state: can be running, ready, waiting, start or done.
        Thread’s register set: registers assigned to thread for computations.
        Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

        Multiple threads can exist within one process where:

        Each thread contains its own register set and local variables (stored in stack).
        All thread of a process share global variables (stored in heap) and the program code.

        https://www.geeksforgeeks.org/multithreading-python-set-1/?ref=lbp

    4. What is Multithreading?
        Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
    
### Data Science Questions
    1. What are the benefits to vectorization?
        1. Using vectorization saves you the work of writing loops.

        2. NumPy are written in languages like C++, which are less convenient to code in, but produce faster-running results. So if you can have NumPy automatically loop over your data, rather than writing a loop in Python, the code will execute faster.

    2. What is Binding arguments in the function?
        When some parameters values are fixed and dont change throughout the lifetime of code. Then the such arg are called Binding arguments in the function.

    3. What is partial tool in python?
        The partial tool built into Python only works if you want to bind the first arguments of the function. If you need to bind later ones, then you can do it yourself using a lambda.

    4. What is the diffrence between model and fit model?
        Models are general descriptions of how a real-world system behaves, typically expressed using mathematical formulas. Each model can be used on many datasets, and a statistician or data scientist does the work of choosing the model they think suits their data.
        A fit model is the specific version of the general model that’s been tailored to suit your data. We create it from the general model by binding the values of the βs to specific numbers.
        