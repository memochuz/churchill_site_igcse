---
title: 📝 Elements of Functions
date: 2026-02-16
description: |
    <p>
    In this lesson, students explore the main elements used to represent and analyze functions. Functions can be represented using mapping diagrams, tables of values, and graphs. Understanding how these representations connect helps learners interpret ordered pairs, construct graphs from tables, and extract key information such as domain and range. Students will also learn how to determine domain restrictions from algebraic rules such as square roots and divisions.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Describe</b> functions using mapping diagrams and graphs.</li>
      <li><b>Interpret</b> ordered pairs (x, f(x)) on the coordinate plane.</li>
      <li><b>Construct</b> graphs of functions by tabulating values.</li>
      <li><b>Find</b> domain and range from a graph using axis projections.</li>
      <li><b>Determine</b> domain restrictions from roots and rational expressions.</li>
    </ul>

categories: [IGCSE, Functions]
image: '/images/Functions/elements_front.png'
---

## Representations of a Function

A function can be represented in several ways. In IGCSE, the most important are:

- **Mapping diagrams**
- **Tables of values**
- **Graphs**

All of these show the same relationship between inputs and outputs — just in different formats.

---

## Mapping Diagram

A **mapping diagram** shows how each input is connected to exactly one output.

- Inputs are listed in one set
- Outputs are listed in another set
- Arrows show how each input maps to an output

Example rule:  
$f(x) = 3x+1$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/mapping_diagram.png" alt="Mapping Diagram" width="700">
</p>

Each input has only one arrow leaving it. If an input had two arrows going to different outputs, it would **not** be a function.

---

## Ordered Pairs and the Graph of a Function

A graph of a function is made of **ordered pairs**:

$$
(x, f(x))
$$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/ordered_pairs.png" alt="Ordered Pairs" width="700">
</p>


This means:

- First coordinate → input $x$
- Second coordinate → output $f(x)$

**Each ordered pair** becomes a point on the coordinate plane that **belongs to the graph.**


### How to Graph by Tabulating Values

To graph a function from its formula:

* **Step 1** — Choose input values  
    Pick several $x$ values (usually integers around 0).

    | $x$ |
    |---|
    | $0$|
    | $1$|
    | $2$|

* **Step 2**— Evaluate the function  
    Compute $f(x)$ for each value.

    | $f(x)=3x+1$ |
    |-----------|
    | $f(0) = 3(0)+1=1$ |
    | $f(1) = 3(1) +1 = 4$ |
    | $f(2) = 3(2)+1= 7$ |

* **Step 3** — Create a table  
    Make a table of $x$ and $f(x)$.

    | $x$ | $f(x)=3x+1$ |
    |---|-----------|
    | $0$| $f(0) = 3(0)+1=1$ |
    | $1$ | $f(1) = 3(1) +1 = 4$ |
    | $2$ | $f(2) = 3(2)+1= 7$ |

* **Step 4** — Plot ordered pairs  
    Plot each $(x, f(x))$ point.
    Ordered pairs:
    $$(0,1), (1,4), (2,7)$$
    <p align="center">
    <img src="{{ site.baseurl }}/images/Functions/pairs.png" alt="Ordered Pairs" width="700">
    </p>

* **Step 5** — Draw the graph  
    Connect smoothly if appropriate.
    <p align="center">
    <img src="{{ site.baseurl }}/images/Functions/ordered_pairs_line.png" alt="Ordered Pairs" width="700">
    </p>
---

## Domain from a Graph (Shadow Method)

The **domain** is all x-values used in the graph.

To find it visually: 👉 Project the graph onto the **x-axis** like a shadow.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/domain.png" alt="Domain" width="700">
</p>

- The leftmost $x$-value = domain start
- The rightmost $x$-value = domain end

**The shadow is the domain**. Sometimes the shadow on the $x$-axis is split into parts, so the domain is written as more than one interval.

For example:
* Interval 1: $[a,b)$
* Interval 2: $[c,d]$

So the domain is:

$$[a,b)\cup[c,d]$$

**Endpoint rules:**

* Open circle → value is not included → use parentheses ( )
* Closed (filled) circle → value is included → use brackets [ ]

Example description for students:

> “Imagine a light above the graph — the shadow on the x-axis shows the domain.”

---

## Range from a Graph (Shadow Method)

The **range** is all y-values produced. 

To find it visually: 👉 Project the graph onto the **y-axis**.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/range.png" alt="Range" width="700">
</p>

- Lowest $y$-value = range start
- Highest $y$-value = range end

**The shadow is the range**. If the shadow on the $y$-axis is split into parts, the range is written as more than one interval (which is not the case in this example).

---

## Finding Domain from the Rule of Correspondence

Sometimes the domain is restricted by the formula. This means we must check which values of $x$ make the formula valid.

> We look for the values of $x$ that make the formula make sense when we substitute them. In other words, after replacing $x$, the expression should not create mathematical problems.

#### When can problems appear?

* **Square Root Restrictions**:
    For even roots, the expression inside the root must be greater than or equal to zero. Otherwise, the result is not a real number.

    For expressions like:

    $$
    f(x) = \sqrt{x - 3}
    $$

    Rule:
    - The expression inside the root must be $\geq 0$

        $$x − 3 \geq 0 \Rightarrow x \geq 3$$

    - Domain: $x \geq 3$, equivalent to: $[3,\infty)$


* **Division Restrictions**:
    We cannot divide by zero. So any value of $x$ that makes the denominator equal to zero must be excluded from the domain.

    For rational expressions:

    $$
    f(x) = \frac{1}{x - 2}
    $$

    Rule:
    - Denominator cannot be zero

    $$x − 2 \neq 0  \Rightarrow x \neq 2$$

    - Domain: all real numbers except $x = 2$, equivalent to $\mathbb{R}- \{2\}$


* **Combined Restrictions**
    For expressions like:

    $$\frac{\sqrt{x}}{\sqrt{x^{2}-1}}$$

    Rule:
    - Denominator cannot be zero
    - The expressions inside the roots must be $\geq 0$

    $$ \underbrace{x \geq 0 }_{(0, \infty)} \quad \text{and} \quad x^{2}-1 >0 \Rightarrow \underbrace{x>1 \text{ or } x<-1}_{(-\infty, -1)\cup(1, \infty)}.$$

    - Domain: are the $x$ values satisfying both conditions, therefore 

    $$(0, \infty) \quad \cap \quad (-\infty, -1)\cup(1, \infty)) = \underbrace{(1, \infty)}_{\text{final answer}} $$

---
## Summary

Key elements of functions include:

- **Mapping diagrams** show input-output connections
- **Ordered pairs (x, f(x))** define graph points
- **Tables** help build graphs
- **Domain** comes from x-values (graph shadow on x-axis)
- **Range** comes from y-values (graph shadow on y-axis)
- **Roots and divisions** create domain restrictions

