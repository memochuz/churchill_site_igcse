---
title: Probability
date: 2026-04-01
description: |
    <p>
    In this lesson, students learn the fundamental concepts of probability. Probability allows us to measure how likely an event is to occur and is widely used in science, economics, and everyday decision-making.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what probability is.</li>
      <li><b>Define</b> experiments, outcomes, and sample spaces.</li>
      <li><b>Identify</b> events and calculate their probabilities.</li>
      <li><b>Apply</b> probability rules and formulas.</li>
      <li><b>Work with</b> Venn diagrams and different types of events.</li>
    </ul>

categories: [IGCSE, Probability]
image: '/images/Probability/probabilidad_portada.png'
---

## What is Probability?

**Probability** measures how likely an event is to happen.

It is a number between 0 and 1:

* 0 → something that is "impossible" to happen  
* 1 → something that "always" occurs  

The quotation marks are used because, in probability, these words are not absolute. An event with probability 0 is treated as "impossible", but in some contexts it could still occur. Similarly, an event with probability 1 is said to "always" occur, but this depends on the model we are using. 

---

## Random Experiment

A **random experiment** is an action or process where we know all the possible outcomes, but we cannot predict which specific outcome will occur.

**Examples:**

* Tossing a coin  
* Rolling a die  
* Picking a card   

---

## Outcomes

An **outcome** is a possible result of a random experiment.

**Example:**  

Rolling a die:

$$
\text{Outcomes: } \{1,2,3,4,5,6\}
$$

Observe that sets are used to represent outcomes.

---

## Sample Space

The **sample space** is the set of all possible outcomes.

It is usually denoted by $S$ or $\Omega$.

**Example:**

Rolling a die:

$$
S = \{1,2,3,4,5,6\}
$$

---

## Events

An **event** is a subset of the sample space.

**Example:**

Rolling a die:

Let $A$ = “getting an even number”

$$
A = \{2,4,6\}
$$

The set $A$ is an event because it is a subset of the sample space $S$.

---

## Probability of an Event

The probability of an event $A$ is:

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}}
$$

* number of favorable outcomes = number of outcomes in event $A$
* total number of outcomes = number of outcomes in sample space $S$

**Example:**

Probability of getting an even number when rolling a die:

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}} =\frac{3}{6} = \frac{1}{2} = 0.5
$$

---

## Properties of Probability

1. Probability is always between 0 and 1:

   $$
   0 \leq P(A) \leq 1
   $$

2. The probability of the sample space is 1:

   $$
   P(S) = 1
   $$

3. The probability of the empty set is 0:

   $$
   P(\varnothing) = 0
   $$

4. For any event $A$, the probability of its complement is:

   $$
   P(A') = 1 - P(A)
   $$

---

## Union of Events (Thinking in Areas)

The probability of the union of two events is:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

#### Intuition (Area Idea)

Think of a Venn diagram as **areas**:

* Add area of $A$  
* Add area of $B$  
* Subtract overlap (counted twice)



<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/formula.png" width="800">
</p>

---

## Mutually Exclusive Events

Two events are **mutually exclusive** (or disjoint) if they cannot happen at the same time.

$$
A \cap B = \varnothing
$$

#### Formula (Special Case)

$$
P(A \cup B) = P(A) + P(B)
$$

> This formula ONLY works if events are mutually exclusive.


<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/ajenos_formula.png" width="800">
</p>

**Example:**

Rolling a die:


* $A$ = getting a 2  
* $B$ = getting a 5  

They cannot happen together → mutually exclusive.

---

## Independent Events

Two events are **independent** if one does not affect the other.

This is very useful when calculating probabilities. In particular, it helps us find the probability of the intersection of two events. The intersection $A \cap B$ means that **both events happen at the same time**.

In the case of independent events, we have a very useful formula:

$$
P(A \cap B) = P(A) \cdot P(B)
$$

> This formula ONLY works if the events are independent.

#### Example of Independent Events

* Toss a coin and roll a die  

* $A$ = getting heads  
* $B$ = getting a 4  

The result of the coin does not affect the result of the die.

$$
P(A) = \frac{1}{2} \quad \text{and} \quad  P(B) = \frac{1}{6}
$$

Thereforme, we can use the independence formula:
$$
P(A \cap B) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}
$$

Where $P(A \cap B)$ is the probability of getting heads AND a 4 at the same time.


#### Example of NOT Independent Events

* Picking two cards from a deck **without replacement**  
* $A$ = first card is an Ace  
* $B$ = second card is an Ace  

If the first card is an Ace, there are fewer Aces left in the deck.  
This changes the probability of the second event.

So, the events are **not independent**.

$$
P(A) = \frac{4}{52}
$$

After one Ace is removed:

$$
P(B \mid A) = \frac{3}{51}
$$

Here, $P(B \mid A)$ means the probability of getting an Ace on the second draw **given that** the first card was already an Ace. We are now working with a smaller sample space (only 51 cards).

Since the probability changes depending on the first event, we **cannot** use:

$$
P(A \cap B) = P(A)\cdot P(B)
$$

---

## Complement of an Event

The **complement** of an event $A$, denoted by $A'$, is the event that **A does not occur**.

In other words, it contains all outcomes in the sample space that are **not in \(A\)**.


#### Formula

$$
P(A') = 1 - P(A)
$$



#### Intuition

Since the total probability of all possible outcomes is:

$$
P(S) = 1
$$

If event $A$ happens with probability $P(A)$, then the probability that it **does not happen** is everything else in the sample space, which is:

$$
1 - P(A)
$$



#### Example

Rolling a die:

* $A$ = getting an even number or 1 → $\{1,2,4,6\}$

$$
P(A) = \frac{4}{6} = \frac{2}{3}
$$

Complement:

* $A'$ = not getting an even number and 1 → $\{3,5\}$

$$
P(A') = 1 - \frac{2}{3} = \frac{1}{3}
$$



#### Key Idea

> The complement represents everything that is **not in the event**.


---

## Examples

**Example 1:**

Toss a coin and roll a die.  

* $A$ = getting tails → $P(A)=\frac{1}{2}$  
* $B$ = getting a 4 → $P(B)=\frac{1}{6}$  

$$
P(A \cap B) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}
$$

---

**Example 2:**

Rolling a die.

* $A$ = getting a 1  
* $B$ = getting a 2  

$$
P(A \cup B) = \frac{1}{6} + \frac{1}{6} = \frac{1}{3}
$$

In general, $A \cup B$ means A or B or both. However, in this case the events are mutually exclusive, so both cannot happen at the same time.  

Therefore, $A \cup B$ simply means getting a 1 or a 2, and we can add their probabilities.

---

**Example 3**

Rolling a die.

* $A$ = even numbers → $\{2,4,6\}$  
* $B$ = numbers greater than 3 → $\{4,5,6\}$  

Intersection:

$$
A \cap B = \{4,6\}
$$

Therefore, we can use the general formula for the union:

$$
P(A \cup B) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6} = \frac{4}{6}
$$

---

## Venn Diagrams in Probability

Venn diagrams help visualize:

* Union ($A \cup B$)
* Intersection ($A \cap B$)
* Complement ($A'$)

Think of probability as **area inside the diagram**.

---

## Common Mistakes

* Adding probabilities without subtracting overlap  
* Using independence formula when events are not independent  
* Using mutually exclusive formula incorrectly  
* Forgetting that probabilities must be between 0 and 1  
* Confusing outcomes with events  

