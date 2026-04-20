---
title: Quadratic Inequalities
date: 2026-04-20
description: |
    <p>
    In this lesson, students learn how to solve quadratic inequalities. 
    These involve finding ranges of values that satisfy an inequality 
    instead of a single solution.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> quadratic inequalities.</li>
      <li><b>Find</b> roots of quadratic expressions.</li>
      <li><b>Use</b> number lines to determine solution regions.</li>
      <li><b>Solve</b> inequalities using factorization.</li>
      <li><b>Interpret</b> solutions as intervals.</li>
    </ul>

categories: [IGCSE, Algebra]
image: '/images/Functions/quadratic_ine_portada.png'
---

## What is a Quadratic Inequality?

A **quadratic inequality** is an inequality that involves a quadratic expression:

$$
\begin{align*}
ax^2 + bx + c & > 0 \\ 
ax^2 + bx + c & < 0 \\
ax^2 + bx + c & \geq 0 \\
ax^2 + bx + c & \leq 0
\end{align*}
$$



Instead of finding exact values, we are looking for **intervals of $x$** that make the expression true.

---

## Method to Solve

To make the method easier to understand, we will go through an example.

Solve the inequality:

$$
x^2 - x - 6 < 0
$$


#### Step 1: Factorize the quadratic

Write the expression as a product of two linear factors (check the the factorization topic) **or use the quadratic formula**.

$$
(x - 3)(x + 2) < 0
$$

#### Step 2: Find the roots

Looking at the factors, we can find the values of $x$ that make the expression equal to zero.

$$
x = 3, \quad x = -2
$$

These values divide the number line into intervals. Could be 1 , 2, or 3 intervals depending on the number of roots. 

* If we have no roots, there is only one interval.  
* If we have one root, there are two intervals.
* If we have two roots, there are three intervals.

In this case, we have 3 intervals:

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/intervals.png" width="600">
</p>

#### Step 3: Sign Analysis

Test each interval or use a sign diagram to determine whether the expression is positive or negative. We do this by:

* picking a test point from each interval and substituting it back into the factored form.
* the sign of the product will tell us whether the expression is positive or negative in that interval.

For our example consider the following test points:

* $-3 \in (-\infty, -2)$
* $0 \in (-2, 3)$
* $4 \in (3, \infty)$

Substituting these into the factored form:

* $f(-3) = (-3 - 3)(-3 + 2) = (-6)(-1) = 6 > 0$
* $f(0) = (0 - 3)(0 + 2) = (-3)(2) = -6 < 0$
* $f(4) = (4 - 3)(4 + 2) = (1)(6) = 6 > 0$

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/signs.png" width="600">
</p>

#### Step 4: Choose the correct intervals

Based on the inequality ($>$, $<$, $\geq$, $\leq$), select the intervals that satisfy the condition.

In our example, we want the expression to be strictly less than zero, so we choose the interval where the expression is negative:

$$\text{Solution: } (-2, 3)$$

---

## Common Mistakes

* Forgetting to factor correctly  
* Choosing the wrong intervals  
* Including/excluding endpoints incorrectly  
 
