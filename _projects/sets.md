---
title: Sets 
date: 2026-03-27
description: |
    <p>
    In this lesson, students learn the fundamental concepts of sets. Sets are essential in most sciences for organizing information, understanding relationships, and solving problems using Venn diagrams and set notation.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> what a set is.</li>
      <li><b>Use</b> set notation correctly.</li>
      <li><b>Identify</b> subsets and universal sets.</li>
      <li><b>Work with</b> union, intersection, and complement.</li>
      <li><b>Solve</b> problems using Venn diagrams.</li>
    </ul>

categories: [IGCSE, Algebra]
image: '/images/Algebra/sets.png'
---

## What is a Set?

A **set** is a collection of **distinct objects**, called elements.

**Example:**
$$
A = \{1, 2, 3, 4\}
$$


#### Notation

* Sets are written using **curly brackets** $\\{ \quad \\}$ 
* Elements are separated by commas  
* Sets are usually denoted by capital letters.

**Example:**

$$
B = \{a, e, i, o, u\}
$$

#### Membership

We use symbols to show if an element belongs to a set:
* $ \in $ → belongs to  
* $ \notin $ → does not belong to  

**Examples:**

If $A= \{1, 2, 3, 4 \}$ and $B= \{a, e, i, o, u\}$, then

$$
3 \in A \quad \text{and} \quad  5 \notin A
$$

---

## Types of Sets

#### Finite Set
A set with a limited number of elements:

$$
C = \{1,2,3\}
$$

#### Infinite Set
A set that goes on forever:
$$
\mathbb{N}=\{1,2,3,4,\dots\}
$$

#### Empty Set
A set with no elements:

$$
\varnothing = \{ \, \}
$$

---

## Universal Set

The **universal set** contains all possible elements within a given context. For example, if we are working **only** with the first $10$ natural numbers, then our universal set is:

$$
U = \{1,2,3,4,5,6,7,8,9,10\}
$$

In this case, we are going to think that, besides these ten numbers, there is nothing else. That’s why it is called the universal set.


<p align="center">
   <img src="{{ site.baseurl }}/images/Numbers/universal_set.png" width="600">
</p>

---

## Subsets

A set $A$ is a subset of $B$ if all elements of $A$ are in $B$. It is denoted by:

$$
A \subset B
$$

You can think of a subset as a smaller bag made up of elements from a larger bag. In a Venn diagram, subsets appear as one set inside another. For example:

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/subset.png" width="600">
</p>

---

## Number of Elements

The number of elements in a set is written as:

$$
n(A)
$$

**Example:**

$$
A = \{1,2,3,4\} \Rightarrow n(A) = 4
$$

---

## Venn Diagrams

A Venn diagram is a visual representation of sets using circles, where each circle represents a set and overlapping regions show the relationships between sets, such as common elements. In a Venn diagram, the universal set is always represented by the rectangle that contains all the circles. It is usually denoted by the letters $U$, $\Omega$ or $\xi$

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/union.png" width="600">
</p>


---

## Operations with Sets

Just as we have operations when working with numbers, we can also define operations with sets to obtain new sets from those already given. The most common operations are:

#### Union

The union operation combines two sets to form a new set that contains all elements from both, without repeating any.

$$
A \cup B
$$

For example, if $A=\{1,2,3,4,5\}$ and $B=\{3,4,5,6,7\}$

then 

$$
A\cup B = \{1,2,3,4,5,6,7\}
$$

Imagine that instead of numbers, we are working with teams of people. Even if the members are listed in a different order, it is still the same team. Also, a person can belong to two different teams, but if we combine both teams into one larger team, that person is only counted once, not twice.

In a Venn diagram, the union is represented as follows:

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/union.png" width="600">
</p>

---

#### Intersection

The intersection operation creates a new set using the elements that both sets have in common.

$$
A \cap B
$$

For example, if $A=\{1,2,3,4,5\}$ and $B=\{3,4,5,6,7\}$

then 

$$
A \cap B = \{3,4,5\}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/intersection.png" width="600">
</p>


---


#### Complement

The complement is an operation involving a single set. It consists of all elements in the universal set that are not in that set.

$$
A'
$$

For example, if $U = \{1,2,3,4,5,6,7,8,9,10 \}$ and $A = \{1,2,3,4,5\}$

then 

$$
A' = \{6,7,8,9,10 \}
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/complement.png" width="600">
</p>

---

## Examples

Let:
$$
A = \{1,2,3,4\}, \quad B = \{3,4,5,6\}, \quad U = \{ 1,2,3,4,5,6,7,8,9,10\}
$$

Find $A\cup B$, $A\cap B$, $A'$ and  $A' \cap B'$

* $A \cup B = \{1,2,3,4,5,6\}$
* $A \cap B = \{3,4\}$
* $A' = \{5,6,7,8,9,10 \}$
* $A'\cap B' = \{ 5,6,7,8,9,10 \} \cap \{ 1,2,7,8,9,10\} = \{ 7, 8, 9, 10 \}$
 


---

## Two-Set Formula

When we want to calculate the number of elements in a set, especially when working with unions and intersections, we can use a very useful formula:


$$
n(A \cup B) = n(A) + n(B) - n(A \cap B)
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Geometry/formula_sets.png" width="600">
</p>

To understand this formula, think about areas instead of the number of elements. If we consider a Venn diagram, we can find the area of the union by adding the area of $A$ and the area of $B$. However, if we do this, we end up counting the intersection twice. That is why we must subtract it once. Now replace the word area with number of elements, and this is exactly how the formula works.


---

## Common Mistakes

* Forgetting that sets do not repeat elements  
* Confusing union and intersection  
* Not subtracting the intersection  
* Writing elements outside the universal set  

