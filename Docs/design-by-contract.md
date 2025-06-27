---
title: Design by Contract
tags:
  - studies
  - programming
  - design
  - software-architecture
use: Documentation
languages: 
dependences:
---

<details> <summary>Table of Contents 🔖</summary>

- [New Note](#new-note)

</details>

---

- [i] #to_review : reler texto extraído, reescrever, conectar, tags e toc
# Design by Contract
> Reference to the 4th chapter of Pragmatic Programmer [#](https://gist.github.com/briankung/7611434#design-by-contract).
This confused the shit out of me. I wasn't entirely sure what the difference was between a contract and a unit test.
Contracts are introduced in the context of employment contracts. That is, before any work is done, the responsibilities of both parties are defined, as well as the consequences of failing. Contracts in programming are similar. As I mentioned before, I wasn't able to make a strong distinction between contracts and unit tests (given some condition, when some event, then this should happen, though I may be confusing this with [BDD](http://en.wikipedia.org/wiki/Behavior-driven_development#Behavioral_specifications)). It's all a bit jumbled in my head.
According to Bertrand Meyer's _Design by Contract_, which he developed and put into practice with the language Eiffel, there are three parts to a contract: _preconditions_, _postconditions_, and _invariants_.
**Preconditions:** What must be true before a method (routine) is called.
**Postconditions:** What must be true after a routine is called.
**Class invariants:** Seriously, what the hell does this mean?
> 	A class ensures that this condition is always true from the perspective of a caller. During internal processing of a routine, the invariant may not hold, but by the time the routine exits and control returns to the caller, the invariant must be true. (Note that a class cannot give unrestricted write-access to any data member that participates in the invariant.)
> 	-_The Pragmatic Programmer, p110_
They mention the Liskov Substitution Principle here, which is part of SOLID principles, lazy code, assertions, crashing early in order to give stack traces at the point of failure...ah, a more in-depth treatment of invariants comes in on page 116.
The example they use is a method that iterates through an array of numbers and searches for the highest value. There is a variable, let's call it a memo, that stores the highest value encountered yet. The loop invariant condition states that, by the end of the execution of the loop, the memo should contain the highest value in the array. While the memo may not contain the highest value on any given iteration of the loop, by the end of the execution of that object, the condition should be true.
In the Semantic Invariants section, the authors explain a philosophical, rather than programmatic, invariant. They describe the programming of a debit card transaction switch that. In charging a customer, the customer should never be charged unnecessarily. That is, if an error occurs during runtime, the card should not be charged. The semantic invariant was as follows: Err in favor of the customer. This invariant guided the code.

