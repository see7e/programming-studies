---
title: Python - Hash Table - Implementation
tags: studies, programação
use: Documentation
languages: Python
dependences: NULL
---

<details> <summary>Table of Contents</summary>

- [oop](#oop)
  - [instances list](#instances-list)
  - [Static Methods](#static-methods)

</details>

---

# [oop](https://www.youtube.com/watch?v=Ej_02ICOIgs)

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

- constructor / magic methods (`__init__`) quando a classe for instanciada esse metodo será executado automaticamente

    ele pode receber `self` e outros parametros como argumentos na inicialização da classe.
    > como qualquer função pode ser definido um valor `defaut` para algum parametro recebido

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

## instances list

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

- instanciar a partir de um `.csv` (usando `decorators`)

    ```python
    import csv
    #[...]
    @classmethod
    def import_csv(cls):
        #[...]
    ```

   `@classmethod` modifica o contexto do metodo, de forma que seu parametro não é mais `self` e sim `cls` que representa a propria classe a ser recebida como argumento.
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

## Static Methods