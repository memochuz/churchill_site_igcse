---
title: Tree Diagrams
date: 2026-04-01
description: |
    <p>
    In this lesson, students learn how to use tree diagrams to represent multi-step experiments. Tree diagrams help us visualize outcomes and calculate probabilities in a clear and structured way.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what a tree diagram is.</li>
      <li><b>Construct</b> tree diagrams for multi-step experiments.</li>
      <li><b>Calculate</b> probabilities along branches.</li>
      <li><b>Find</b> probabilities of events involving multiple outcomes.</li>
    </ul>

categories: [IGCSE, Probability]
image: '/images/Probability/tree_diagram_portada.png'
---

## Multi-Step Experiments

Some random experiments happen in **stages**.

**Examples:**
* Tossing a coin twice  
* Picking two cards  
* Rolling two dice  

These experiments can be harder to analyze, but we can organize them using **tree diagrams**.

---

## What is a Tree Diagram?

A **tree diagram** is a visual way to represent all possible outcomes of a multi-step experiment.

* Each **branch** represents a possible outcome  
* Each **level** represents a stage of the experiment  
* The diagram shows all possible **paths**

---

## How to Construct a Tree Diagram

1. Start with a point (the starting position)  
2. Draw branches for all possible outcomes of the first step  
3. From each branch, draw new branches for the next step  
4. Continue until all stages are represented  
5. Label each branch with its probability  


---

## Calculating Probabilities with Tree Diagrams

Once the tree diagram is complete, we can use it to calculate probabilities.


* **Probability Along a Path**: To find the probability of a **single path**, multiply the probabilities along the branches. This represents the probability that **all events in that path happen**.
* **Events with Multiple Paths**: Sometimes an event can happen in **more than one way** (more than one branch). In this case, we add the probabilities of all relevant paths.


---

## Example: Tossing a coin Three Times

* First toss: H or T  
* Second toss: H or T  
* Third toss: H or T

Possible outcomes:

$$
\begin{align*}
\{ & (H,H,H), (H,H,T), (H,T,H), (H,T,T), \\
  & (T,H,H), (T,H,T), (T,T,H), (T,T,T)\}
\end{align*}
$$

Each outcome can be represented as a path in the tree diagram and as a triplet of H and T that represents the sequence of outcomes.

Assume the coin is **not fair**, and the probability of Heads is $\frac{1}{3}$ and Tails is $\frac{2}{3}$. Each branch has probability $\frac{1}{3}$ or $\frac{2}{3}$.



<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/example_coin.png" width="600">
</p>

If we want to calculate the probability of getting exactly two Heads, we look at the branches that correspond to that outcome:

<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/example_coin_2.png" width="600">
</p>

In this case, we have three branches that correspond to getting exactly two Heads: $(H,H,T)$, $(H,T,H)$, and $(T,H,H)$. Each of these paths has a probability of:  $\frac{1}{3} \cdot \frac{1}{3} \cdot \frac{2}{3} = \frac{2}{27}$. Since there are three such branches, we add their probabilities:

$$
P(\text{exactly 2 Heads}) = \frac{2}{27} + \frac{2}{27} + \frac{2}{27} = \frac{6}{27} = \frac{2}{9}
$$  

---

## Example: Without Replacement

* Picking two cards from a deck  
* $A$ = first card is an Ace  
* $B$ = second card is an Ace  


<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/example_cards.png" width="600">
</p>

First draw:

$$
P(\text{first card is an Ace }) = \frac{4}{52}
$$

Second draw (depends on first):

$$
P(\text{second card is an Ace given that the first card is an Ace }) = \frac{3}{51}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Probability/example_cards_2.png" width="600">
</p>

So:

$$
P(A \cap B) = \frac{4}{52} \cdot \frac{3}{51}
$$

---

## Common Mistakes

* Not completing all branches  
* Forgetting to multiply along a path  
* Adding probabilities incorrectly  
* Assuming independence when it is not true  
* Not updating probabilities (without replacement cases)  

