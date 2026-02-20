---
title: 📝 Composition, Inverse, Logarithms and Range of Functions
date: 2026-02-20
description: |
    <p>
    In this lesson, students explore how functions can be combined, reversed, and analysed in more depth. They learn that composing functions means substituting one function into another, and that the order of composition matters. Students also study inverse functions using mapping diagrams, graphs, and algebraic methods. Finally, they are introduced to logarithmic functions as the inverse of exponential functions and learn how to determine the range of a function using its inverse.
    </p>
    <hr>
    <h1>Class Objectives</h1>
    <ul>
      <li><b>Understand</b> function composition as substitution using mapping diagrams and algebra.</li>
      <li><b>Interpret</b> the notation <i>fog</i> and <i>gof</i> and recognise that they are not always equal.</li>
      <li><b>Apply</b> step-by-step methods to find compositions of functions.</li>
      <li><b>Understand</b> inverse functions as functions that reverse a mapping.</li>
      <li><b>Find</b> inverse functions using graphs, the line <i>$y = x$</i>, and algebraic methods.</li>
      <li><b>Recognise</b> logarithmic functions as the inverse of exponential functions.</li>
      <li><b>Define</b> logarithms and evaluate them using different bases.</li>
      <li><b>Use</b> the laws of logarithms to simplify expressions and solve exponential equations.</li>
      <li><b>Determine</b> the domain and range of functions, including using inverse functions.</li>
    </ul>

categories: [IGCSE, Functions]
image: '/images/Functions/composition_inverse_log_range_front.png'
---

## Composition of Functions

#### What is Composition?

To **compose functions** means to substitute one function into another.

In simple words:

> Doing a composition means replacing the variable $x$ with another expression.

#### Mapping Diagram Idea

If we have:

$$
x \rightarrow f(x) \rightarrow g(f(x))
$$

That means:

1. Start with $x$
2. Apply $f$
3. Then apply $g$ to the result

So:

$$
g(f(x)) = g\circ f (x)
$$

means **put $f(x)$ wherever you see $x$ inside $g$**.

If we swap the role of $g$ with $f$, we obtain $f(g(x))$

This means **replacing $x$ with $g(x)$ inside $f$**.


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/composition_mapping.png" width="600">
</p>



#### Simple Example of Substitution

Let:

$$
f(x) = x^2
$$

Then:

$$
f(1) = 1^2 = 1
$$

$$
f(\pi) = \pi^2
$$

$$
f(\star) = (\star)^2
$$

Notice:

We are simply replacing $x$ with whatever is inside the parentheses.


#### Now With Two Functions

Let:

$$
f(x) = 2x+1
$$

$$
g(x) = x^2
$$


#### Step-by-step: Find $f(g(x))$

**Step 1:** Write $f(x)$

$$
f(x) = 2x+1
$$

**Step 2:** Replace $x$ with $g(x)$

$$
f(g(x)) = 2(\underbrace{x^2}_{g(x)})+1
$$

$$
f(g(x))=f\circ g(x) = 2x^2+1
$$


#### Step-by-step: Find $g(f(x))$

**Step 1:** Write $g(x)$

$$
g(x) = x^2
$$

**Step 2:** Replace $x$ with $f(x)$

$$
g(f(x)) = (\underbrace{2x+1}_{f(x)})^2
$$

$$
g(f(x))=g \circ f = 4x^2+4x+1
$$


#### Important

$$
f \circ g \neq g \circ f
$$

Composition is **not commutative**. From the previous examples, we know that most of the times

$$
f(g(x)) \neq g(f(x))
$$

---

## Inverse Function

### What is an Inverse?

In words:

> The inverse function undoes what the original function does.

If $f$ sends $x$ to $y$, then $f^{-1}$ sends $y$ back to $x$.


#### Mapping Diagram Idea

$$
x \rightarrow f(x)
$$

Inverse:

$$
f(x) \rightarrow x
$$

It reverses the arrows.

<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/mapping_diagram_inverse.png" width="600">
</p>

#### Finding the Inverse from a Graph

The inverse is the reflection across the line:

$$
y = x
$$

To sketch it:

1. Draw $y=x$
2. Reflect the graph over that line


<p align="center">
   <img src="{{ site.baseurl }}/images/Functions/inverse_graph.png" width="600">
</p>


#### Finding the Inverse Algebraically (Step-by-step)

Given:

$$
f(x)=2x+3
$$

**Step 1**: Replace $f(x)$ with $y$:

$$
y = 2x+3
$$

**Step 2**: Solve for $x$:

$$
y-3=2x
$$

$$
x=\frac{y-3}{2}
$$

**Step 3**: Replace $x$ with $f^{-1}(x)$ and $y$ with $x$:

$$
f^{-1}(x)=\frac{x-3}{2}
$$

---

## Inverse of Exponential → Logarithm

The inverse of:

$$
f(x) = a^x
$$

is

$$
f^{-1}(x) = \log_a (x)
$$

---

## Definition of Logarithm

$$
\log_{a} (b) = x
$$

means:

> To what power must I raise $a$ to get $b$?

$$
a^x = b
$$


#### Examples

1. Find $\log_{2} (8)$:
    $$
    \log_{2} (8) = 3
    $$
    because:

    $$
    2^{3} = 8
    $$


2. Find $\log_{3} (9)$

    $$
    \log_{3} (9) = 2
    $$

    because:

    $$
    3^2 = 9
    $$


3. Find $\log_{10} (1000)$
    
    $$
    \log_{10} (1000) = 3
    $$
    
    because:
    
    $$
    10^3 = 1000
    $$


#### Logarithm Properties

1. **Product Rule**

    $$
    \log_a (xy) = \log_a x + \log_a y
    $$

1. **Quotient Rule**

    $$
    \log_a \left(\frac{x}{y}\right) = \log_a x - \log_a y
    $$

1. **Power Rule**

    $$
    \log_a (x^n) = n\log_a x
    $$

1. **Change of Base Rule**

    $$
    \log_{a}(x)=\dfrac{\log_{b}(x)}{\log_{b}(a)}
    $$

#### Examples 

1. Simplify $\log_2 (8x)$:

    $$
    \log_{2} (8x)= \log_{2} (8) + \log_{2} (x) = 3 + \log_{2} (x)
    $$



1. Find $x$.

    $$
    3^{x} = 20
    $$

    Take $\log$:

    $$
    x\log (3) = \log (20),
    $$

    therefore

    $$
    x = \frac{\log 20}{\log 3}
    $$

---

## Domain and Range of Logarithms

For:

$$
y = \log_{a} (x)
$$

#### Domain:

$$
x > 0
$$

#### Range:

All real numbers.

---

## Using the Inverse to Find the Range

Important idea:

> The range of a function is the domain of its inverse.



#### Examples

1. Consider the following function

    $$
    f(x)=x^2 \quad \text{for } x \geq 0
    $$

    Inverse:

    $$
    f^{-1}(x)=\sqrt{x}
    $$

    Domain of inverse:

    $$
    x \geq 0
    $$

    Therefore:

    $$\text{Range$(f)$}=[0,\infty)$$



2. Consider the following function

    $$
    f(x)=e^x
    $$

    Inverse:

    $$
    f^{-1}(x)=\ln x
    $$

    Domain of inverse:

    $$
    x>0
    $$

    Therefore:

    $$\text{Range$(f)$}=(0,\infty)$$

---

##  Final Key Ideas

- Composition = substitution.
- Order matters in composition.
- Inverse undoes a function.
- Inverse graph is reflection over $y=x$.
- Logarithm is the inverse of exponential.
- Range of a function = Domain of its inverse.