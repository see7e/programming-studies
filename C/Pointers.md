---
title: Pointers
tags: studies, programação
use: Documentation
languages: C
dependences: NULL
---

# [**Ponteiros**](https://pt.wikipedia.org/wiki/Ponteiro_(programa%C3%A7%C3%A3o))

são variáveis que armazenam endereços de memória em um programa. Um ponteiro pode ser utilizado para acessar o conteúdo da variável que está armazenada no endereço de memória apontado por ele, ou para modificar o conteúdo dessa variável.

Em C, a declaração de um ponteiro é feita utilizando o operador `*`. Por exemplo, se quisermos declarar um ponteiro para um inteiro, podemos fazer da seguinte forma:
```c
int *ptr;
```
Neste exemplo, `ptr` é um ponteiro para um inteiro. Ele pode ser inicializado com o endereço de memória de uma variável do tipo int, utilizando o operador `&`. Por exemplo:
```c
int n = 10;
int *ptr = &n;
```

Neste caso, o ponteiro ptr está sendo inicializado com o endereço de memória da variável `n`. Isso permite que o conteúdo da variável `n` possa ser acessado e modificado através do ponteiro `ptr`.

Para acessar o conteúdo da variável apontada por um ponteiro, utilizamos o operador `*`. Por exemplo:
```c
int n = 10;
int *ptr = &n;
printf("O valor de n é: %d\n", *ptr);
```
Neste exemplo, o operador `*` é utilizado para acessar o conteúdo da variável n através do ponteiro `ptr`. O resultado da execução deste código será a impressão da seguinte linha: O valor de `n` é: 10.

Também podemos utilizar um ponteiro para modificar o conteúdo da variável apontada por ele. Por exemplo:
```c
int n = 10;
int *ptr = &n;
*ptr = 20;
printf("O valor de n é: %d\n", n);
```

Neste exemplo, o valor da variável `n` é modificado para `20` utilizando o ponteiro ptr. Isso é feito na linha 3, onde o conteúdo do endereço de memória apontado por `ptr` é modificado para o valor `20`. Na linha 4, é impresso o valor da variável `n`, que agora será `20`.

Os ponteiros são muito utilizados em C para acessar e modificar variáveis de forma eficiente, especialmente em funções que precisam manipular grandes quantidades de dados. Porém, eles também podem ser uma fonte de erros e bugs, especialmente quando utilizados de forma inadequada. É importante ter cuidado ao trabalhar com ponteiros e sempre verificar se os endereços de memória estão sendo manipulados de forma correta.

## Ponteiros duplos

Um ponteiro duplo é um ponteiro que aponta para outro ponteiro. Em outras palavras, ele armazena o endereço de memória de outro ponteiro. Isso é útil em situações em que precisamos modificar o valor de um ponteiro por referência, ou seja, sem modificar o valor original da variável apontada pelo ponteiro.

Exemplo:
```c
#include <stdio.h>

int main() {
  int x = 10;
  int *p1 = &x; // ponteiro para x
  int **p2 = &p1; // ponteiro para p1

  printf("Valor de x: %d\n", x);
  printf("Valor de p1: %p\n", p1);
  printf("Valor de p2: %p\n", p2);

  **p2 = 20; // modificando o valor de x através de p2

  printf("Novo valor de x: %d\n", x);

  return 0;
}
```

Um ponteiro duplo pode ser utilizado para representar uma matriz em C. Isso ocorre porque, em essência, uma matriz em C é um bloco contíguo de memória, onde cada elemento é acessado utilizando a notação de índice.

Para representar uma matriz utilizando ponteiros duplos, podemos alocar dinamicamente um bloco contíguo de memória utilizando a função malloc, que retorna um ponteiro para o início da memória alocada. Em seguida, podemos utilizar ponteiros duplos para acessar os elementos da matriz, como se estivéssemos utilizando a notação de índice.

Exemplo:
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
  int **matriz;
  int i, j;

  // alocando memória para a matriz
  matriz = (int**) malloc(2 * sizeof(int*));
  for (i = 0; i < 2; i++) {
    matriz[i] = (int*) malloc(3 * sizeof(int));
  }

  // preenchendo a matriz
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++) {
      matriz[i][j] = i + j;
    }
  }

  // imprimindo a matriz
  for (i = 0; i < 2; i++) {
    for (j = 0; j < 3; j++) {
      printf("%d ", matriz[i][j]);
    }
    printf("\n");
  }

  // liberando a memória alocada
  for (i = 0; i < 2; i++) {
    free(matriz[i]);
  }
  free(matriz);

  return 0;
}
```

Nesse exemplo, estamos alocando dinamicamente (com o uso de [malloc](https://pt.wikipedia.org/wiki/Aloca%C3%A7%C3%A3o_din%C3%A2mica_de_mem%C3%B3ria_em_C)) uma matriz de dimensões 2x3 e preenchendo seus elementos com valores simples. Note que para acessar os elementos da matriz, estamos utilizando a notação de índice através do ponteiro duplo `matriz[i][j]`. No final do programa, estamos liberando a memória alocada utilizando a função `free`.

## Funções de ponteiros

As funções em C podem receber ponteiros como argumentos e também podem retornar ponteiros. Isso é útil em situações em que precisamos passar uma grande quantidade de dados para uma função ou quando queremos alocar dinamicamente memória dentro de uma função e retornar um ponteiro para essa memória alocada.

Exemplo:
```c
#include <stdio.h>
#include <stdlib.h>

void allocate_memory(int **p) {
  *p = (int*) malloc(sizeof(int));
}

int main() {
  int *p;

  allocate_memory(&p); // alocando memória dentro da função

  *p = 10;

  printf("Valor de p: %p\n", p);
  printf("Valor apontado por p: %d\n", *p);

  free(p); // liberando a memória alocada

  return 0;
}
```

---

> Extra

# Difference between Arrays and Pointers


![](https://files.codingninjas.in/share-26616.svg) Share

## Introduction

Array and pointer have a close relationship. Still, both are different concepts in C programming. A set of items stored in contiguous [memory](https://www.codingninjas.com/codestudio/library/main-memory) locations is called an [array](https://www.codingninjas.com/codestudio/library/introduction-to-array). In comparison, a variable whose value is the address of another variable is referred to as a pointer. 

This blog will show the concept of arrays and pointers and the difference between [arrays and pointers.](https://www.codingninjas.com/codestudio/library/array-and-pointers)