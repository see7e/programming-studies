---
title: Dunder Methods
tags:
  - studies
  - programming
  - builtin
  - python
  - OOP
use: Documentation, Coding
languages: Python
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---
- [i] #to_review : Aprimorar texto, conectar, toc, tags
# Dunder Method
**Are methods that allow instances of a class to interact with the built-in functions and operators** of the language. The word “dunder” comes from “double underscore”, because the names of dunder methods start and end with two underscores, for example `__str__` or `__add__`. Typically, dunder methods are not invoked directly by the programmer, making it look like they are called by magic. That is why dunder methods are also referred to as “magic methods” *sometimes*.

Dunder methods are not called magically, though. They are just called implicitly by the language, at specific times that are well-defined, and that depend on the dunder method in question.
> The dunder method everyone knows

If you have defined classes in Python, you are bound to have crossed paths with a dunder method: `__init__`. **It's responsible for initialising your instance of the class** (like the `constructor` in JS, which is why it is in there that you usually set a bunch of attributes related to arguments the class received.

For example, if you were creating an instance of a class `Square`, you would create the attribute for the side length in `__init__`:

```python
>>> class Square:
	    def __init__(self, side_length):
	        """__init__ is the dunder method that INITialises the instance.

	        To create a square, we need to know the length of its side,
	        so that will be passed as an argument later, e.g. with Square(1).
	        To make sure the instance knows its own side length,
	        we save it with self.side_length = side_length.
	        """
	        print("Inside init!")
	        self.side_length = side_length

>>> sq = Square(1)
# Inside init!
```

Like any other constructor it receives the argument (if needed), at the creation of their instance, including `self`.
> como qualquer função pode ser definido um valor `defaut` para algum parâmetro recebido

```python
class Item:
    def __init__(self, name, price, qtd=0):
        print(F"Instance created - {name}")
        self.name = name
        self.price = price
        self.qtd = qtd
        
    def calculate_price(self): # method
        return self.price * self.qtd

item = Item("pen", 1.5, 2) # create instance and recieve arguments
print(item.name, item.price, item.qtd)
print(item.calculate_price())
```

- para restringir o argumento recebido pelo metodo, pode ser tipando o parametro na definição do metodo
    `def __init__(self, name: str, price: float, qtd=0):`
    caso o parametro tenha um valor defaut python ja reconhece o tipo daquele atributo

- `assert` statement
    é outra forma de restingir a entrada de dados através dos parametros `assert price >= 0`

    caso a determinação nao seja atendida sera retornado `AssertionError` por defaut, mas essa mensagem pode ser editada
    
    ```python
    class Item:
        def __init__(self, name: str, price: float, qtd=0):
            # validations
            assert price >= 0, F"Price {price} lesser than zero."
            assert qtd >= 0,  F"Quantity {qtd} lesser than zero."

            # atributes
            self.name = name
            self.price = price
            self.qtd = qtd
        
        def calculate_price(self): # method
            return self.price * self.qtd
    ```

- Class Atributes, funciona como uma variável local que pode ser acessada através da instancia de um objeto (lembra a ligação `__proto__` em JS)

    ```python
    class Item:
        discount: 0.8 # 20%

        def __init__(self, name: str, price: float, qtd=0):
            # validations
            assert price >= 0, F"Price {price} lesser than zero."
            assert qtd >= 0,  F"Quantity {qtd} lesser than zero."

            # atributes
            self.name = name
            self.price = price
            self.qtd = qtd
        
        def calculate_price(self): # method
            return self.price * self.qtd
    ```

    - `__dict__` (dictionary) lista todos os atributos do objeto seja ele uma classe ou uma instancia da classe

- chamando a própria classe (`Item.`) pode-se acessar os atibutos que pertencem somente a ela, porem, como boa pratica aconselha-se usilizar `self` para se referir ao atributo pertencido pela propria instancia

    ```python
    class Item:
        discount: 0.8 # 20%

        def __init__(self, name: str, price: float, qtd=0):
            # validations
            assert price >= 0, F"Price {price} lesser than zero."
            assert qtd >= 0,  F"Quantity {qtd} lesser than zero."

            # atributes
            self.name = name
            self.price = price
            self.qtd = qtd
        
        def calculate_price(self): # method
            return self.price * self.qtd

        def apply_discount(self):
            self.price = self.price * self.discount

    item = Item("pen", 1.5, 2) # instance
    item.apply_discount()
    print(item.price())
    ```

    porem se chamarmos o atributo da classe e modificar seu valor, esse novo valor será aplicado somente para aquela instancia

    ```python
    # [...]
    item2 = Item("rubber", 0.5, 1) # instance
    item2.discount = 0.9
    item2.apply_discount()
    print(item2.price)
    ```

### Instances list

```python
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
		
    item1 = Item("Phone", 100, 1)
    item2 = Item("Notebook", 1000, 3)
    item3 = Item("Mouse", 10, 5)
    item4 = Item("Keyboard", 75, 5)
	
    #print(Item.all)
    for instance in Item.all:
        print(instance.name)
```

- `__repr__` (represent) retorna o objeto com a formatação desejada
    uma boa prática é retornar da forma mais parecedia com a que foi criada:
    ```python
    def __repr__(self):
        return F"Item('{self.name}', {self.price}, {self.qtd})"
    ```


## `__mro__`
