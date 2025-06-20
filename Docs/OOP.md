---
title: Object-oriented Programming - OOP
tags:
  - studies
  - programming
  - paradigm
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [Object-oriented Programming - OOP #](#object-oriented-programming---oop-)
  - [Concepts](#concepts)
    - [Abstraction](#abstraction)
    - [Encapsulation](#encapsulation)
    - [Inheritance](#inheritance)
    - [Polymorphism](#polymorphism)
    - [Methods](#methods)
    - [Classes](#classes)
    - [Dunder Method](#dunder-method)
    - [Instances list](#instances-list)

</details>

---

# Object-oriented Programming - OOP [#](https://www.youtube.com/watch?v=Ej_02ICOIgs)

## Concepts
There's two big branches in programming, they're called Programming Paradigms.
> Paradigm is a way/method to do some task. A programming paradigm is a style/way of programming and not referring to a specific language.
> by [Gopi Gorantala](https://dev.to/ggorantala/functional-programming-and-programming-paradigms-in-java-323f)

![graph](https://res.cloudinary.com/practicaldev/image/fetch/s--NoymT3CM--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1r3e3w4xgj30b81zb4yu.png)

And as you can see (*if the image was not removed*) OOP belongs to the Imperative Paradigm, but what does it mean?
>  **Imperative programming** is a [programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm "Programming paradigm") of software that uses statements that change a program's state. In much the same way that the imperative mood in natural languages expresses commands, an imperative program consists of commands for the computer to perform. Imperative programming focuses on describing _how_ a program operates step by step.
>  *Jain, Anisha (2022-12-10). ["Javascript Promises— Is There a Better Approach?"](https://medium.datadriveninvestor.com/javascript-promises-is-there-a-better-approach-dd6a0a329131). Medium. Retrieved 2022-12-20.*

Object-Oriented Programming (OOP) ==is designed around **objects** – self-contained entities that bundle data and behaviour==. Instead of writing one long list of instructions, developers define **classes** (blueprints) and create **objects** (instances) that interact to perform the program's tasks. These objects mirrors real-world systems by breaking complex problems into smaller pieces and blocks.

Throughout, we'll highlight *why* OOP is so widely used in modern software development by correlating its principles with real-world development practices such as code reuse, modular design, and adaptability to change.
### Language Support
OOP is supported (to varying degrees) by many popular programming languages such as Python, Java, C++, C#, Ruby, and JavaScript.

### Benefits and Advantages
Improved code organization, reuse, and maintainability. By following OOP principles, teams can build modular programs that are easier to extend and reason about, which is crucial for large or evolving codebases.

## Core OOP Principles
At its core, OOP revolves around a few **basic principles** – commonly listed as **abstraction, encapsulation, inheritance,** and **polymorphism**.

### Abstraction 
The Objects translate to a imaginable entity that have an Identity, Characteristics and can perform actions. With this is possible to (*“ignore the details”*) ==**hide the complexity by focusing on the essential features of an object** relevant to the context==.
The first one gives the recognition of a unique element in the code. The characteristics are the atributes of the Object and, the actions are the methods of the Object.
> e.g. a bank account
```js
class Account {
	// attributes
	constructor() {
		this.id = 001;
		this.user = '...';
		this.agency = '...';
		this.balance = 1000.0; // private attribute
	}
	// public methods
	deposit(...) {...}
	withdraw(...) {...}
}
```

This `constructor` element (*the syntax changes from each programming language*) has the built-in attributes that define the object, it can receive methods too, but this is just a representation.

### Encapsulation
This principle refers to bundling data with the methods that operate on that data, this means that ==**all important information is contained inside an object and only select information is exposed**==.
The implementation and state (fields/properties/attributes) of each object are privately held inside a defined class. Other objects do not have access to this class or the authority to make changes. They are only able to call a list of public functions or methods, the behaviour.
This leads to better data integrity, when the object acts as a single unit with clear role, relating with the **S** letter – Single Responsibility Principle (SRP), of the [SOLID](solid.md) acronym.

### Inheritance 
==A class can be created from another, thus receiving its information==. When this happens, we say that the new Object is a child of the previous one, receiving the characteristics of the "parent" by inheritance. Note that this newly attributes belongs now to the "child", so it may have be different from other "brothers" and even the "parent".

```mermaid
classDiagram
	Animal --> Duck
	Animal --> Fish
	
	class Animal {
		canWalk = False; // (default)
		canSwim = False; // (default)
		canFly = False;  // (default)
	}

	class Duck {
		canWalk = True;
		canSwim = True;
		canFly = True;
	}
	
	class Fish {
		canWalk = False;
		canSwim = True;
		canFly = False;
	}
```

In this example:
```js
class Duck extends Animal {...}
class Fish extends Animal {...}
```

This makes reusing and organizing code by establishing an “is-a” relationship between classes more easy, by promoting codebase reuse – common functionality is defined once in the base class and shared with all derived classes.

>[!NOTE]
> In languages like Java and C#, inheritance is **single-root** (each class has one parent, ultimately inheriting from a common base like Java’s `Object`[docs.oracle.com](https://docs.oracle.com/javase/specs/jls/se12/html/jls-1.html#:~:text=Reference%20types%20are%20the%20class,which)). **C++ allows multiple inheritance** (a class can inherit from several classes), though this adds complexity and potential pitfalls like the **“diamond problem”.**

Also many languages mitigate this by offering *interfaces or mixins* – allowing a class to implement multiple sets of behaviors without multiple concrete inheritance. **Proper use of inheritance can make code more extensible:** new subclasses can be added to extend behavior with minimal changes to existing code (an application of the *Open-Closed Principle - OCP*, refer to [SOLID](solid.md)).

> [!WARNING]
> The misuse of inheritance (e.g. deep inheritance chains or inheriting just to reuse code where a different relationship is more appropriate) can lead to brittle designs. Modern best practices often advise to **favor composition over inheritance** for greater flexibility.

### Polymorphism 
 Means exactly "many forms" and allows different types of objects to pass through the same (and uniform) interface. This ==**grants the possibility that "child's" can have different behaviours of the "parents"**== typically via subclassing or interface implementation.

![polymorph](https://media.geeksforgeeks.org/wp-content/uploads/20200911171857/PolymorphisminObjectOrientedProgramming.png)

For example, if `Car` and `Bicycle` both inherit from `Vehicle` (or implement a `VehicleInterface`), you can write a function that takes a `Vehicle` reference and calls `vehicle.drive()` without caring whether it’s a Car or Bicycle. Each class implements `drive()` in its own way – this is called *dynamic dispatch* or *method overriding*. The correct method is called based on the actual object’s class at runtime (this is *subtype polymorphism*).

Another form is *parametric polymorphism* (generics or templates) where the same class or function can operate on many types. The key benefit is **flexibility and extensibility**: polymorphism, especially via interfaces/abstract classes.

#### Compile-time Polymorphism
This is resolved during compilation and includes:
- **Function Overloading**: Multiple functions with the same name but different parameter types or counts.
```cpp
class Printer {
public:
    void print(int i) { std::cout << "Printing int: " << i << std::endl; }
    void print(double d) { std::cout << "Printing double: " << d << std::endl; }
};
```

- **Operator Overloading**: Defining custom behavior for operators with user-defined types
```cpp
class Complex {
public:
    double real, imag;
    Complex(double r, double i) : real(r), imag(i) {}
	
    Complex operator+(const Complex& other) {
        return Complex(real + other.real, imag + other.imag);
    }
};
```

> [!NOTE]
> Not all languages support compile-time polymorphism directly. For example, Python and JavaScript do not support true function overloading.

#### Runtime Polymorphism
Resolved during execution, typically via:
- **Virtual Functions**: In C++, a base class can declare a function as `virtual`, allowing derived classes to override it. Calls to the function on base class pointers will invoke the derived class implementation if overridden.
```cpp
class Animal {
public:
    virtual void speak() { std::cout << "Animal sound" << std::endl; }
};

class Dog : public Animal {
public:
    void speak() override { std::cout << "Bark" << std::endl; }
};

void makeSound(Animal* a) {
    a->speak(); // will call Dog::speak if a is Dog*
}
```

- **Method Overriding**: In Java, Python, C#, and others, a child class can override methods defined in a parent class to change behavior.
```python
# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Child class
class Dog(Animal):
    # Overriding the speak method
    def speak(self):
        print("The dog barks")

# Another child class
class Cat(Animal):
    # Overriding the speak method
    def speak(self):
        print("The cat meows")

# Usage
animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Output: The animal makes a sound
dog.speak()     # Output: The dog barks
cat.speak()     # Output: The cat meows
```

### Methods 
Are functions that are defined inside a class that describe the behaviors of an object. Each method contained in class definitions starts with a reference to an instance object. Additionally, the subroutines contained in an object are called instance methods. Programmers use methods for reusability or keeping functionality encapsulated inside one object at a time.

### Classes
A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

Visit the following resources to learn more:
-   [Classes in Python](https://docs.python.org/3/tutorial/classes.html)
-   [Python Classes and Objects](https://www.geeksforgeeks.org/python-classes-and-objects/)
-   [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)

---


- `<class 'int'>` cada variável é uma instancia de uma classe de data type, esse é o resultado de

    ```python
    item = 7
    print(type(item))
    ```


    ```python
    class Item:
        def calculate_price(): # method
            pass

    item1 = Item() # create instance
    print(type(item)) # <class '__main__.Item'>
    ```

- `<class '__main__.Item'>`
- `self` parametro de um metodo que é autogerado, ele passa o próprio objeto (no caso a instancia da classe) como argumento quando o método é chamado.
    Se nenhum parametro for passado `TypeError: calculate_ price() takes 0 positional arguments but 1 was given`


### 
- instanciar a partir de um `.csv` (usando `decorators`)

    ```python
    import csv
    #[...]
    @classmethod
    def import_csv(cls):
        #[...]
    ```

   `@classmethod` ([`decorator`](../Languages/Python/README.md#decorators) [ver também](https://docs.python.org/3/library/dataclasses.html))modifica o contexto do metodo, de forma que seu parametro não é mais `self` e sim `cls` que representa a propria classe a ser recebida como argumento.
   Porem esse metodo especifico sera acessado a partir da propria classe

   ```python
   Item.import_csv()
   ```

   dessa forma, o codigo ficara assim:

    ```python
    import csv
	
    class Item:
        discount: 0.8 # 20%
        all = []
		
        def __init__(self, name: str, price: float, qtd=0):
            # validations
            assert price >= 0, F"Price {price} lesser than zero."
            assert qtd >= 0,  F"Quantity {qtd} lesser than zero."
			
            # atributes
            self.name = name
            self.price = price
            self.qtd = qtd
			
            # actions
            Item.all.append(self) # record created instances
        
        def calculate_price(self): # method
            return self.price * self.qtd
		
        def apply_discount(self):
            self.price = self.price * self.discount
		
        @classmethod
        def import_csv(cls): # this uses csv lib
            # get the info
            with open('items.csv', 'r') as file:
                reader = csv.DictReader(file)
                items = list(reader)
			
            # create new instances
            for item in items:
                Item(
                    name = item.get('name'),
                    price = float(item.get('price')),
                    qtd = int(item.get('qtd'))
                )
		
        def __repr__(self):
            return F"Item('{self.name}', {self.price}, {self.qtd})"
	
    #print(Item.all)
    for instance in Item.all:
        print(instance.name)
    
    ```
